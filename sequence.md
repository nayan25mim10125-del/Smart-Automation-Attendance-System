```mermaid
sequenceDiagram
Student->>System: Submit location
System->>Timetable: Check active class
Timetable-->>System: Assigned room
System->>Classroom: Get coordinates
Classroom-->>System: Room location
System->>System: Calculate distance and apply rules
System-->>Student: Attendance decision
System->>AttendanceDB: Save result
```