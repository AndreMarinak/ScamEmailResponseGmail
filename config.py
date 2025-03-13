"""
Configuration utilities for the ScamEmailResponse project.
This module handles loading environment variables and configuration settings.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
env_path = Path('.') / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

# API Keys
VIRUSTOTAL_API_KEY = os.environ.get("VIRUSTOTAL_API_KEY", "")

# Gmail API configuration
GMAIL_SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'

# Check if credentials exist
def check_credentials():
    """Check if necessary credential files exist."""
    missing_files = []
    
    if not os.path.exists(CREDENTIALS_FILE):
        missing_files.append(CREDENTIALS_FILE)
    
    if not os.path.exists(TOKEN_FILE):
        missing_files.append(TOKEN_FILE)
    
    if not VIRUSTOTAL_API_KEY:
        missing_files.append("VIRUSTOTAL_API_KEY (environment variable)")
    
    if missing_files:
        print("Warning: The following credentials are missing:")
        for file in missing_files:
            print(f"  - {file}")
        print("Please refer to the README.md for setup instructions.")
    
    return len(missing_files) == 0

if __name__ == "__main__":
    # When run directly, check if all credentials are set up
    if check_credentials():
        print("All credentials are properly set up!")
    else:
        print("Some credentials are missing. See warnings above.") 