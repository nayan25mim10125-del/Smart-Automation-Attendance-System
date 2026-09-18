# Smart Automation Attendance System Using Intelligent Agent

## 1. Project Overview
This project is a command-line attendance automation system based on a rule-based intelligent agent. It checks a student's scheduled class and classroom proximity before making an attendance decision.

The project demonstrates course concepts from Fundamentals of AI and ML:
- Intelligent Agents
- PEAS representation
- Task Environment
- Rational decision making
- Rule-based problem solving

## 2. Main Modules
1. **Student Management** - reads student records.
2. **Timetable Management** - identifies whether a class is active.
3. **Classroom Validation** - reads classroom coordinates.
4. **Location/Distance Calculation** - calculates distance using geographic coordinates.
5. **Intelligent Attendance Decision** - applies rules to decide Present / Outside / No Class.
6. **Attendance Storage** - records valid attendance in `attendance.csv`.

## 3. Requirements
- Python 3.10 or later
- pandas
- geopy

## 4. Installation

Open a terminal in the project folder:

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## 5. Run the Project

Normal run using the computer's current time:
```bash
python main.py
```

For a predictable demonstration, use the supplied test class time:
```bash
python main.py --time 21:30 --lat 23.1820 --lon 79.9870
```

The demo location is within 30 meters of classroom A101, so the scheduled students are marked Present.

To demonstrate an outside-classroom case:
```bash
python main.py --time 21:30 --lat 23.1900 --lon 79.9950
```

## 6. Input Files
- `students.csv` - student ID and name
- `timetable.csv` - student schedule, classroom, start and end time
- `classroom.csv` - classroom latitude and longitude
- `attendance.csv` - attendance output/history

## 7. Decision Logic

```text
Is there an active scheduled class?
       |
   No  |----> NO_CLASS
       |
      Yes
       |
Calculate distance to assigned classroom
       |
Distance <= 30 m?
   |           |
  Yes         No
   |           |
PRESENT    OUTSIDE_CLASSROOM
```

## 8. PEAS

| Element | Project Specification |
|---|---|
| Performance | Correct attendance decisions and reduced manual work |
| Environment | Students, classrooms, timetable and attendance records |
| Actuators | Mark attendance / reject attendance |
| Sensors | Timetable data and student location coordinates |

## 9. Limitations
The submitted version uses a simulated student location for command-line testing. A production version could obtain live device location and integrate an institutional timetable system.

## 10. Project Structure

```text
Smart-Automation-Attendance-System/
├── README.md
├── statement.md
├── requirements.txt
├── main.py
├── students.csv
├── timetable.csv
├── classroom.csv
├── attendance.csv
├── docs/
└── tests/
```
