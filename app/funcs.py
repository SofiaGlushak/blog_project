import smtplib
import os

MY_ADDRESS = os.environ.get("MY_ADDRESS")
PASSWORD = os.environ.get("PASSWORD")


def send_email(data):
    text = f"Name: {data['name']}\n" \
            f"Email: {data['email']}\n" \
            f"Phone: {data['phone']}\n" \
            f"Message: {data['message']}\n"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_ADDRESS, password=PASSWORD)
        connection.sendmail(from_addr=MY_ADDRESS,
                            to_addrs=MY_ADDRESS,
                            msg=f"Subject:User message\n\n{text}")
