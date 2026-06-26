import builtins
import io
import json
import os
import sys
import fee_balance_check as fbc


def capture_output(func, *args, **kwargs):
    old_stdout = sys.stdout
    buffer = io.StringIO()
    sys.stdout = buffer
    try:
        func(*args, **kwargs)
    finally:
        sys.stdout = old_stdout
    return buffer.getvalue()


def run_tests():
    print('Running non-interactive test runner (emails disabled)...')

    # Use a temporary default path and disable email sending.
    fbc.EMAIL_SENDING_ENABLED = False

    # Validate date formatting helpers.
    assert fbc.validate_date_format('2026-08-01')
    assert not fbc.validate_date_format('01-08-2026')

    # Test loading student data from JSON file.
    data_path = os.path.join(os.path.dirname(__file__), 'students.json')
    data = fbc.load_student_data(data_path)
    assert isinstance(data, dict)
    assert 'ALG001' in data

    # Test student fee status output for a fully-paid student.
    fbc_input = builtins.input
    try:
        builtins.input = lambda prompt='': '2026-09-01'
        paid_output = capture_output(fbc.check_student, 'ALG005')
        assert 'Fee fully paid' in paid_output

        # Test student with a pending balance.
        unpaid_output = capture_output(fbc.check_student, 'ALG004')
        assert 'Fee pending' in unpaid_output
        assert 'Reminder email' in unpaid_output
    finally:
        builtins.input = fbc_input

    # Test non-existent student handling.
    missing_output = capture_output(fbc.check_student, 'UNKNOWN')
    assert 'Student ID not found' in missing_output

    print('All tests passed.')


if __name__ == '__main__':
    run_tests()

