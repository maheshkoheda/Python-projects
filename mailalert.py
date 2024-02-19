import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import ssl

def send_email(subject, message, sender_email, receiver_email, password):
    """
    Send an email alert.

    Parameters:
        subject (str): The subject of the email.
        message (str): The content of the email.
        sender_email (str): The sender's email address.
        receiver_email (str): The receiver's email address.
        password (str): The sender's email password.
    """
    try:
        # Set up the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Create SSL context
        context = ssl.create_default_context()

        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.set_debuglevel(1)
            smtp.login(sender_email, password)
            smtp.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

def monitor_cpu_threshold(threshold, interval=1):
    """
    Monitor CPU usage and send email alert if it exceeds the threshold.

    Parameters:
        threshold (float): The CPU usage threshold above which an alert will be sent.
        interval (float): The time interval (in seconds) between each monitoring iteration.
    """
    try:
        print(f"Monitoring CPU usage (Threshold: {threshold}%):")

        while True:
            # Fetch CPU usage percentage
            cpu_percent = psutil.cpu_percent(interval=interval)
            print(f"Current CPU Usage: {cpu_percent}%")

            # Send email alert if CPU usage exceeds the threshold
            if cpu_percent > threshold:
                subject = "High CPU Usage Alert"
                message = f"CPU usage is at {cpu_percent}%, which exceeds the threshold of {threshold}%."
                sender_email = "xxxx@gmail.com"  # Change this to your sender email
                receiver_email = "xxxx@gmail.com"  # Change this to your recipient email
                password = "xxxx xxxx xxxx xxxx"  # Change this to your email password from Security-> App-> password generated. Note, 2 factor authentication is required on gmail.

                send_email(subject, message, sender_email, receiver_email, password)

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    # Example usage: Monitor CPU usage with a threshold of 5%
    monitor_cpu_threshold(4)
