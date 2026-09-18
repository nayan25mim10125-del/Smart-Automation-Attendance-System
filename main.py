import argparse
import csv
from datetime import datetime
from pathlib import Path
import pandas as pd
from geopy.distance import geodesic

BASE_DIR = Path(__file__).resolve().parent
DISTANCE_LIMIT_METERS = 30

def parse_args():
    parser = argparse.ArgumentParser(
        description="Smart Automation Attendance System - AI rule-based attendance agent"
    )
    parser.add_argument("--time", help="Testing time in HH:MM format (example: 21:30)")
    parser.add_argument("--lat", type=float, default=23.1820,
                        help="Student latitude (default is demo location)")
    parser.add_argument("--lon", type=float, default=79.9870,
                        help="Student longitude (default is demo location)")
    return parser.parse_args()

def time_to_minutes(value):
    hour, minute = map(int, value.split(":"))
    return hour * 60 + minute

def is_class_active(start, end, current):
    current_m = time_to_minutes(current)
    return time_to_minutes(start) <= current_m <= time_to_minutes(end)

def mark_attendance(student_id, name, room, status):
    path = BASE_DIR / "attendance.csv"
    with path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            student_id, name, datetime.now().date(),
            datetime.now().strftime("%H:%M"), room, status
        ])

def intelligent_attendance_decision(distance, class_active):
    # Rule-based rational-agent decision:
    # attend only when a scheduled class is active and the student is
    # physically within the configured classroom radius.
    if not class_active:
        return "NO_CLASS"
    if distance <= DISTANCE_LIMIT_METERS:
        return "PRESENT"
    return "OUTSIDE_CLASSROOM"

def main():
    args = parse_args()
    students = pd.read_csv(BASE_DIR / "students.csv")
    timetable = pd.read_csv(BASE_DIR / "timetable.csv")
    classroom = pd.read_csv(BASE_DIR / "classroom.csv")

    current_time = args.time or datetime.now().strftime("%H:%M")
    student_location = (args.lat, args.lon)

    print("=" * 60)
    print("SMART AUTOMATION ATTENDANCE SYSTEM")
    print("AI Concept: Rule-Based Intelligent Agent")
    print("=" * 60)
    print(f"Checking time: {current_time}")
    print(f"Student location: {student_location}")
    print(f"Attendance radius: {DISTANCE_LIMIT_METERS} meters")

    for _, student in students.iterrows():
        student_id = student["student_id"]
        name = student["name"]

        print(f"\nChecking Student: {student_id} - {name}")

        rows = timetable[
            (timetable["student_id"] == student_id) &
            (timetable.apply(
                lambda row: is_class_active(row["start"], row["end"], current_time),
                axis=1
            ))
        ]

        if rows.empty:
            print("Decision: NO_CLASS")
            print("Reason: No scheduled class at this time.")
            continue

        room = rows.iloc[0]["room"]
        room_data = classroom[classroom["room"] == room]

        if room_data.empty:
            print(f"Decision: ERROR - classroom {room} not found.")
            continue

        class_location = (
            float(room_data.iloc[0]["lat"]),
            float(room_data.iloc[0]["lon"])
        )
        distance = geodesic(student_location, class_location).meters
        decision = intelligent_attendance_decision(distance, True)

        print(f"Classroom: {room}")
        print(f"Distance: {distance:.2f} meters")
        print(f"Decision: {decision}")

        if decision == "PRESENT":
            mark_attendance(student_id, name, room, "Present")
            print("Attendance marked successfully.")
        else:
            print("Attendance not marked: student is outside classroom.")

if __name__ == "__main__":
    main()
