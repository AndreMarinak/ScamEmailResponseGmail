from googleapiclient.discovery import build
import base64
import email
from email.mime.text import MIMEText
import re

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_service():
    """Return the Gmail API service assuming authentication is already completed."""
    from google.oauth2.credentials import Credentials
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    return build('gmail', 'v1', credentials=creds)

def get_unread_emails(service):
    """Retrieve all unread emails."""
    results = service.users().messages().list(userId='me', q='is:unread').execute()
    return results.get('messages', [])

def extract_links(content):
    """Extract all links from the email content."""
    return re.findall(r'https?://[^\s]+', content)

def analyze_email(message):
    """Analyze the email by breaking it into parts."""
    raw_message = base64.urlsafe_b64decode(message['raw']).decode('utf-8')
    msg = email.message_from_string(raw_message)

    sender = msg.get('From', 'Unknown Sender')
    subject = msg.get('Subject', 'No Subject')
    content = ""

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                content = part.get_payload(decode=True).decode('utf-8')
                break
    else:
        content = msg.get_payload(decode=True).decode('utf-8')

    links = extract_links(content)
    return sender, subject, content, links

def send_analysis_response(service, sender, subject, links):
    """Send a response back to the sender with all links found."""
    response_body = f"""
    Hello,

    Here are the links we found in your email:

    {chr(10).join(links)}

    Thank you!
    """
    message = MIMEText(response_body)
    message['to'] = sender
    message['subject'] = f"Links Found in Your Email: {subject}"

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    try:
        service.users().messages().send(
            userId='me',
            body={'raw': encoded_message}
        ).execute()
        print(f"Response sent to {sender}.")
    except Exception as e:
        print(f"Failed to send response to {sender}: {e}")

def mark_email_as_read(service, message_id):
    """Mark an email as read."""
    print(f"Marking email with ID {message_id} as read...")
    service.users().messages().modify(
        userId='me',
        id=message_id,
        body={'removeLabelIds': ['UNREAD']}
    ).execute()
    print(f"Email with ID {message_id} marked as read.")

def main():
    service = get_service()

    # Get all unread emails
    unread_emails = get_unread_emails(service)
    if not unread_emails:
        print("No unread emails found.")
        return

    for email_meta in unread_emails:
        message_id = email_meta['id']
        print(f"Processing email with ID {message_id}...")

        # Fetch the full email
        message = service.users().messages().get(userId='me', id=message_id, format='raw').execute()

        # Analyze the email
        sender, subject, content, links = analyze_email(message)
        print(f"Sender: {sender}")
        print(f"Subject: {subject}")
        print(f"Links: {links}")

        # Send the response back to the sender with the links
        send_analysis_response(service, sender, subject, links)

        # Mark the email as read
        mark_email_as_read(service, message_id)

if __name__ == '__main__':
    main()
