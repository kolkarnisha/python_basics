from datetime import datetime, date
import smtplib
import ssl
from email.message import EmailMessage

# Replace these with your sending email credentials.
# For example, if using Gmail, enable "App Passwords" or "Less secure apps" depending on your account.
EMAIL_SENDER = "solutions@algonex.co.in"
EMAIL_PASSWORD = "221027"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
EMAIL_SENDING_ENABLED = True

print("=== Algonex IT Solutions - Fee Management System ===")
print("Mentor: Ganesh Pasala\n")
students_db = {
    "ALG001": {
        "name": "Nisha Zareentaj",
        "email": "neeshakolkar@gmail.com",
        "total_fee": 25000,
        "fee_paid": 5000,
        "training_start": "2026-08-01",
        "training_days": 60
    },
    "ALG002": {
        "name": "KARTHIK PASALA",
        "email": "karthik@example.com",
        "total_fee": 15000,
        "fee_paid": 10000,
        "training_start": "2026-08-05",
        "training_days": 60
    },
    "ALG003": {
        "name": "KEERTHI REDDY",
        "email": "keerthi@example.com",
        "total_fee": 15000,
        "fee_paid": 5000,
        "training_start": "2026-08-10",
        "training_days": 60
    },
    "ALG004": {
        "name": "RAGIRI INDHU",
        "email": "ragiri@example.com",
        "total_fee": 15000,
        "fee_paid": 0,
        "training_start": "2026-08-15",
        "training_days": 60
    },
    "ALG005": {
        "name": "SOWMYA REDDY",
        "email": "sowmya@example.com",
        "total_fee": 15000,
        "fee_paid": 15000,
        "training_start": "2026-08-20",
        "training_days": 60
    }
}

def calculate_days_remaining(start_date_str, total_days):
    """Calculate how many training days are left"""
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    today = date.today()
    days_passed = (today - start_date).days
    days_remaining = total_days - days_passed
    return max(days_remaining, 0) # don't show negative


def send_fee_reminder_email(name, receiver_email, balance):
    """Send a simple fee balance reminder email."""
    if not EMAIL_SENDING_ENABLED:
        print(f"(Simulation) Would send email to {receiver_email} with balance Rs{balance}")
        return True
    subject = "Fee Balance Reminder"
    body = (
        f"Hello {name},\n\n"
        f"Your fee balance is Rs{balance}. Please pay the remaining amount as soon as possible.\n\n"
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
    """Main function to check student fee status"""
    if student_id not in students_db:
        print("Error: Student ID not found. Please check and try again.")
        return
    
    student = students_db[student_id]
    name = student["name"]
    total_fee = student["total_fee"]
    fee_paid = student["fee_paid"]
    balance = total_fee - fee_paid
    days_left = calculate_days_remaining(student["training_start"], student["training_days"])
    
    print(f"\n--- Welcome {name} ---")
    print(f"Student ID: {student_id}")
    print(f"Total Fee: Rs{total_fee}")
    print(f"Fee Paid: Rs{fee_paid}")
    print(f"Balance Remaining: Rs{balance}")
    print(f"Training Days Remaining: {days_left} days")
    print("------------------------")
    
    if balance == 0:
        print("Fee fully paid. You are allowed to the class.")
        print("Thank you for your payment!")
    else:
        print("Fee pending. Class access restricted until payment.")
        if student.get("email"):
            if send_fee_reminder_email(name, student["email"], balance):
                print(f"Reminder email sent to {student['email']}.")
            else:
                print("Reminder email could not be sent. Check email settings.")
        else:
            print("No email address found for this student. Add email in the database to send reminders.")

        payment_date = input("Enter the date you will pay the remaining fee (YYYY-MM-DD): ")
        
        # Basic date validation
        try:
            datetime.strptime(payment_date, "%Y-%m-%d")
            print(f"\nNoted. You should definitely pay your fee on {payment_date}.")
            print("Please do not break your promise.")
            print("Contact Mentor Ganesh Pasala for any issues.")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    # Main program loop
    while True:
        print("\nOptions: 1. Check Fee Status  2. Exit")
        option = input("Enter option: ")
        
        if option == "1":
            sid = input("Enter your Student Unique ID: ").upper().strip()
            check_student(sid)
        elif option == "2":
            print("Thank you. Have a great day!")
            break
        else:
            print("Invalid option. Try again.")