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

### For Administrators
To run this service on your own Gmail account:

1. Follow the setup instructions below
2. Keep the script running to continuously monitor for new emails
3. The system will automatically process incoming emails and send responses

## Setup and Security

### Credentials and API Keys
This project requires several credential files and API keys that should NOT be committed to GitHub:

1. **Google API Credentials**:
   - `credentials.json` - OAuth 2.0 credentials for Gmail API
   - `token.json` and `gmail_token.json` - Authentication tokens

2. **VirusTotal API Key**:
   - Set as an environment variable: `VIRUSTOTAL_API_KEY`

### Setting Up Environment Variables
Create a `.env` file in the project root (this file is ignored by Git):

```
VIRUSTOTAL_API_KEY=your_api_key_here
```

Then load this file in your Python scripts or set the environment variables manually.

### First-Time Setup
1. Create your Google API credentials at the [Google Cloud Console](https://console.cloud.google.com/)
2. Download the credentials as `credentials.json`
3. Run the authentication flow to generate token files
4. Get a VirusTotal API key from [VirusTotal](https://www.virustotal.com/)
5. Set up your environment variables

### .gitignore
A `.gitignore` file has been set up to prevent sensitive files from being committed to GitHub. Always check that your credential files are properly excluded before pushing to a public repository.

## Running the Service

To provide continuous email monitoring and response, you'll need to keep the script running. Here are some options:

### Option 1: Run on a Server or Cloud Instance
Deploy the script on a server or cloud instance (like AWS EC2, Google Cloud Compute, or a VPS) to run continuously.

```bash
# Install dependencies
pip install -r requirements.txt

# Run the main script
python SendEmailBack.py
```

### Option 2: Scheduled Execution
Use cron jobs (Linux/Mac) or Task Scheduler (Windows) to run the script at regular intervals:

```bash
# Example cron job to run every 5 minutes
*/5 * * * * cd /path/to/ScamEmailResponse && python SendEmailBack.py
```

### Option 3: Simple Local Execution
For testing or personal use, you can run it manually:

```bash
# Run the script
python SendEmailBack.py
```

## Future Enhancements

- Improved scam detection algorithms
- Machine learning-based classification
- Support for analyzing email attachments
- Web interface for viewing scam reports
- Scanning images for QR codes that might lead to malicious sites
