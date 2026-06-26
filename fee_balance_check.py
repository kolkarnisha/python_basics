from datetime import datetime, date
import json
import os
import smtplib
import ssl
from email.message import EmailMessage

# Email settings.
# For security, set these in environment variables instead of hardcoding them.
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "solutions@algonex.co.in")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
EMAIL_SENDING_ENABLED = os.getenv("EMAIL_SENDING_ENABLED", "false").lower() in {"1", "true", "yes"}
STUDENT_DATA_FILE = os.getenv("STUDENT_DATA_FILE", "students.json")

DEFAULT_STUDENTS_DB = {
    "ALG001": {
        "name": "Nisha Zareentaj",
        "email": "neeshakolkar@gmail.com",
        "total_fee": 25000,
        "fee_paid": 5000,
        "training_start": "2026-08-01",
        "training_days": 60,
    },
    "ALG002": {
        "name": "KARTHIK PASALA",
        "email": "karthik@example.com",
        "total_fee": 15000,
        "fee_paid": 10000,
        "training_start": "2026-08-05",
        "training_days": 60,
    },
    "ALG003": {
        "name": "KEERTHI REDDY",
        "email": "keerthi@example.com",
        "total_fee": 15000,
        "fee_paid": 5000,
        "training_start": "2026-08-10",
        "training_days": 60,
    },
    "ALG004": {
        "name": "RAGIRI INDHU",
        "email": "ragiri@example.com",
        "total_fee": 15000,
        "fee_paid": 0,
        "training_start": "2026-08-15",
        "training_days": 60,
    },
    "ALG005": {
        "name": "SOWMYA REDDY",
        "email": "sowmya@example.com",
        "total_fee": 15000,
        "fee_paid": 15000,
        "training_start": "2026-08-20",
        "training_days": 60,
    },
}

def load_student_data(filename=STUDENT_DATA_FILE):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = filename if os.path.isabs(filename) else os.path.join(script_dir, filename)
    if not os.path.isfile(data_path):
        return DEFAULT_STUDENTS_DB.copy()

    try:
        with open(data_path, encoding="utf-8") as handle:
            data = json.load(handle)
        if isinstance(data, dict):
            print(f"Loaded student records from {data_path}")
            return data
        print(f"Warning: {filename} does not contain a JSON object. Using built-in student records.")
    except Exception as error:
        print(f"Warning: Could not load {filename}: {error}. Using built-in student records.")

    return DEFAULT_STUDENTS_DB.copy()


STUDENTS_DB = load_student_data()


def format_currency(amount):
    return f"Rs{amount:,}"


def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def calculate_days_remaining(start_date_str, total_days):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    today = date.today()

    if today < start_date:
        return total_days

    days_passed = (today - start_date).days
    days_remaining = total_days - days_passed
    return max(days_remaining, 0)


def send_fee_reminder_email(name, receiver_email, balance):
    if not EMAIL_SENDING_ENABLED:
        print(f"(Simulation) Would send email to {receiver_email} with balance {format_currency(balance)}")
        return True

    subject = "Fee Balance Reminder"
    body = (
        f"Hello {name},\n\n"
        f"Your fee balance is {format_currency(balance)}. Please pay the remaining amount as soon as possible.\n\n"
        "Thank you,\n"
        "Algonex IT Solutions"
    )

    message = EmailMessage()
    message["From"] = EMAIL_SENDER
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(body)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(message)
        return True
    except Exception as error:
        print(f"Could not send email: {error}")
        return False


def check_student(student_id):
    student = STUDENTS_DB.get(student_id)
    if not student:
        print("Error: Student ID not found. Please check and try again.")
        return

    name = student["name"]
    total_fee = student["total_fee"]
    fee_paid = student["fee_paid"]
    balance = total_fee - fee_paid
    days_left = calculate_days_remaining(student["training_start"], student["training_days"])

    print(f"\n--- Welcome {name} ---")
    print(f"Student ID: {student_id}")
    print(f"Total Fee: {format_currency(total_fee)}")
    print(f"Fee Paid: {format_currency(fee_paid)}")
    print(f"Balance Remaining: {format_currency(balance)}")
    print(f"Training Days Remaining: {days_left} days")
    print("------------------------")

    if balance <= 0:
        print("Fee fully paid. You are allowed to the class.")
        print("Thank you for your payment!")
        return

    print("Fee pending. Class access is restricted until payment is complete.")
    if student.get("email"):
        if send_fee_reminder_email(name, student["email"], balance):
            print(f"Reminder email sent to {student['email']}.")
        else:
            print("Reminder email could not be sent. Check email settings.")
    else:
        print("No email address found for this student. Add email in the database to send reminders.")

    payment_date = input("Enter the date you will pay the remaining fee (YYYY-MM-DD): ").strip()
    if validate_date_format(payment_date):
        print(f"\nNoted. You are expected to pay on {payment_date}.")
        print("Please keep this commitment and contact Mentor Ganesh Pasala if you need help.")
    else:
        print("Invalid date format. Please use YYYY-MM-DD.")


def display_header():
    print("=== Algonex IT Solutions - Fee Management System ===")
    print("Mentor: Ganesh Pasala\n")


def display_menu():
    print("\nOptions: 1. Check Fee Status  2. Exit")


def main():
    display_header()
    while True:
        display_menu()
        option = input("Enter option: ").strip()

        if option == "1":
            sid = input("Enter your Student Unique ID: ").upper().strip()
            check_student(sid)
        elif option == "2":
            print("Thank you. Have a great day!")
            break
        else:
            print("Invalid option. Please enter 1 or 2.")


if __name__ == "__main__":
    main()