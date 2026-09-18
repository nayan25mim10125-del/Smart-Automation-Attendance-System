# Project Statement

## Problem
Manual classroom attendance can be time-consuming and can record attendance when a student is not physically present in the assigned classroom.

## Objective
Develop a command-line intelligent attendance system that checks the scheduled class and classroom proximity before marking a student present.

## Scope
The project uses student records, timetable information and classroom coordinates. A rule-based intelligent agent makes the final attendance decision.

## Functional Requirements
1. Read student information.
2. Read timetable information.
3. Determine whether a class is active.
4. Identify the assigned classroom.
5. Calculate distance from the student to the classroom.
6. Mark attendance only when the distance is within 30 meters.
7. Store attendance results.

## Non-Functional Requirements
1. Usable from the command line.
2. Simple and maintainable Python structure.
3. Input validation and graceful handling of missing classrooms.
4. Repeatable testing through command-line time/location arguments.

## AI Mapping
The system acts as a rational, rule-based agent. It observes timetable and location information, evaluates conditions, and performs an attendance action.
