# IOCSentinel - IOC Checker

Junior SOC Analyst project. Checks if attacker IPs are known bad on AbuseIPDB.

## What it does

Takes list of IPs from iocs.txt, calls AbuseIPDB API, prints MALICIOUS if abuseConfidenceScore > 75 else CLEAN.

Think like SOC: BruteGuard finds attacker IP, IOCSentinel checks if IP is known bad on internet.

## Files

- checker.py - Checker code
- iocs.txt - IPs to check, one per line
- README.md - This file

## How to run

export ABUSEIPDB_API_KEY="your key"
python3 checker.py iocs.txt

## Tests

iocs.txt:
8.8.8.8
1.2.3.4
192.168.1.50

Expected:
8.8.8.8 0 CLEAN
1.2.3.4 76 MALICIOUS
192.168.1.50 0 CLEAN

## How it works

- check_ip(ip) - Headers with Key, params with ipAddress, requests.get, data["data"]["abuseConfidenceScore"], return score
- check_all_ips(filename) - Open file, loop lines, strip, call check_ip, if score > 75 print MALICIOUS else CLEAN
- main() - Get filename from sys.argv or iocs.txt, call check_all_ips

## Skills

Python, REST API, requests, JSON, Env vars, SOC threat intel
