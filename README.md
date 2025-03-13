# ScamEmailResponse
IN PROGRESS

## Project Summary

ScamEmailResponse is an automated email scam detection service that analyzes incoming emails and responds with an assessment of their likelihood of being a scam. The system uses the Gmail API to monitor a dedicated Gmail account, automatically analyzing any email sent to it and sending back a detailed scam analysis report.

### How It Works:

1. Anyone can send an email to your designated Gmail account
2. The system automatically detects new emails
3. It analyzes the email content, URLs, and other elements for signs of scam/phishing
4. It sends back an automated response with a scam likelihood assessment

### Key Features:

- **Automated Scam Detection**: Analyzes emails for common scam indicators
- **Email Monitoring**: Continuously monitors your Gmail inbox for new messages
- **URL Extraction & Analysis**: Identifies URLs in emails and checks them against VirusTotal's database for malicious content
- **Instant Response**: Automatically sends back a detailed analysis report to the sender
- **Security Analysis**: Provides information about potentially malicious elements in emails

### Components:

- `SendEmailBack.py`: Analyzes emails and sends back a summary with scam assessment
- `SendBackUrls.py`: Extracts URLs from emails, analyzes them, and includes results in the response
- `ForwardEmails.py`: Can optionally forward suspicious emails to a specified email address for further review
- `UrlVirusTotalCheck.py`: Analyzes URLs using the VirusTotal API to check for malicious content

This service is designed to be a public resource that anyone can use by simply sending an email to your designated Gmail address. It's particularly useful for individuals who want to verify if an email they received elsewhere might be a scam.

## How to Use

### For End Users
To check if an email is a scam:

1. Forward the suspicious email to: [your-gmail-address@gmail.com]
2. Wait for an automated response (usually within minutes)
3. Review the analysis report that will be sent back to you

The response will include:
- Overall scam likelihood assessment
- Analysis of any URLs found in the email
- Identification of common scam indicators
- Security recommendations
