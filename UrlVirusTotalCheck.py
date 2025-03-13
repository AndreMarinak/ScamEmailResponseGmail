import requests
import time
import os
from config import VIRUSTOTAL_API_KEY, check_credentials

API_URL = "https://www.virustotal.com/vtapi/v2/url/report"

# Check if credentials are properly set up
if not VIRUSTOTAL_API_KEY:
    print("Warning: No VirusTotal API key found. Set the VIRUSTOTAL_API_KEY environment variable.")

def analyze_url_with_virustotal(url):
    """Check URL safety using VirusTotal API."""
    params = {
        "apikey": VIRUSTOTAL_API_KEY,  # Your API key
        "resource": url     # The URL to check
    }

    try:
        # Make the request to VirusTotal
        print(f"Analyzing URL: {url}")
        response = requests.get(API_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            # Check if the URL has been analyzed before
            if data.get("response_code") == 1:  # URL is in VirusTotal's database
                positives = data.get("positives", 0)
                total = data.get("total", 0)
                scans = data.get("scans", {})
                malicious_scanners = [
                    f"{scanner} ({result.get('result', 'Unknown')})"
                    for scanner, result in scans.items() if result.get("detected")
                ]

                # Print the result
                print("\n--- Analysis Result ---")
                if positives > 0:
                    print(f"🔴 Unsafe: Reported as malicious by {len(malicious_scanners)} scanners.")
                    print(f"Threat Types: {', '.join(malicious_scanners)}")
                else:
                    print("🟢 Safe: No reports of malicious activity.")

                print(f"\nDetection Ratio: {positives} / {total}")
            elif data.get("response_code") == 0:  # URL not in VirusTotal's database
                print("\n--- Analysis Result ---")
                print("The URL has not been analyzed by VirusTotal before.")
                print("You may submit it for scanning via the VirusTotal platform.")
            else:
                print("\n--- Error ---")
                print(f"Unexpected response from VirusTotal: {data.get('verbose_msg', 'No message')}")

        else:
            print("\n--- Error ---")
            print(f"Failed to connect to VirusTotal. HTTP Status Code: {response.status_code}")
            print(f"Response: {response.text}")

    except Exception as e:
        print("\n--- Exception ---")
        print(f"An error occurred while analyzing the URL: {str(e)}")

if __name__ == "__main__":
    # Check credentials before running
    check_credentials()
    
    # URL to analyze
    test_url = "http://sub.aakv.net/JElI.CVwy?od=1syy677c0e05a26c4t0t_outvl_Active22.vlgro.O2n9crg2jmk2c5g00q_xe1674.g2jmkMTRtZ2YtMGltM2ZtMQ0n4dTb"  # Replace with the URL you want to check

    # Check URL safety
    analyze_url_with_virustotal(test_url)
