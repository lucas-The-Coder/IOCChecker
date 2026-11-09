# FILE: checker.py - IOC Checker
# THINK LIKE SOC: BruteGuard found attacker IP, now check if IP is known bad on internet
# Our job: Call AbuseIPDB API for each IP, read abuseConfidenceScore, print MALICIOUS or CLEAN

# IMPORTS TO CREATE:
# Import requests for API calls
# Import sys for reading file name if given
import requests
import sys
import os

API_KEY = os.getenv("ABUSEIPDB_API_KEY")
URL = "https://api.abuseipdb.com/api/v2/check"


# FUNCTION TO CREATE: check_ip(ip)
# INPUT: ip - string, e.g. "8.8.8.8"
# OUTPUT: score int, e.g. 0 or 95
# STEP 1: Make headers dict with Key = API_KEY, Accept = application/json
# STEP 2: Make params dict with ipAddress = ip, maxAgeInDays = 90
# STEP 3: Call requests.get(URL, headers=headers, params=params)
# STEP 4: Parse response.json() to get data -> abuseConfidenceScore
# STEP 5: Return score
def check_ip(ip):
    headers = {"Key": API_KEY, "Accept": "application/json"}

    params = {"ipAddress": ip, "maxAgeInDays": 90}

    response = requests.get(URL, headers=headers, params=params)

    data = response.json()

    score = data["data"]["abuseConfidenceScore"]

    return score


# FUNCTION TO CREATE: check_all_ips(filename)
# INPUT: filename - string, e.g. "iocs.txt"
# STEP 1: Open filename, loop lines, strip whitespace to get ip
# STEP 2: Call check_ip(ip) to get score
# STEP 3: If score > 75, print IP + score + MALICIOUS, else print IP + score + CLEAN
def check_all_ips(filename):
    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()

            score = check_ip(ip)
            if score > 75:
                print(ip, score, "MALICIOUS")
            else:
                print(ip, score, "CLEAN")


# FUNCTION TO CREATE: main()
# VARIABLE: filename = sys.argv[1] if given else "iocs.txt"
# CALL: check_all_ips(filename)
def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "iocs.txt"

    check_all_ips(filename)


# BOTTOM: Call main() if run directly
if __name__ == "__main__":
    main()
