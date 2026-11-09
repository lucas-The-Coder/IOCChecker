import requests
import sys
import os

API_KEY = os.getenv("ABUSEIPDB_API_KEY")
URL = "https://api.abuseipdb.com/api/v2/check"

def check_ip(ip):
    headers = {"Key": API_KEY, "Accept": "application/json"}

    params = {"ipAddress": ip, "maxAgeInDays": 90}

    response = requests.get(URL, headers=headers, params=params)

    data = response.json()

    score = data["data"]["abuseConfidenceScore"]

    return score

def check_all_ips(filename):
    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()

            score = check_ip(ip)
            if score > 75:
                print(ip, score, "MALICIOUS")
            else:
                print(ip, score, "CLEAN")

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "iocs.txt"

    check_all_ips(filename)

if __name__ == "__main__":
    main()
