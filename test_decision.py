from main import intelligent_attendance_decision

def test_present():
    assert intelligent_attendance_decision(10, True) == "PRESENT"

def test_outside():
    assert intelligent_attendance_decision(50, True) == "OUTSIDE_CLASSROOM"

def test_no_class():
    assert intelligent_attendance_decision(10, False) == "NO_CLASS"
