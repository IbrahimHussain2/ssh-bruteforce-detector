# SSH Brute-Force Detector

A Python script that reads a Linux SSH login log and flags IP addresses that look like they're trying to brute-force their way in.

I built this to learn how SOC analysts spot brute-force attacks in auth logs, and to practise Python.

## What it does
It counts failed logins for each IP address. If an IP has 3 or more failures, it's flagged as a possible brute-force. If that same IP also logged in successfully, it's flagged as critical, because the attacker probably guessed the password.

## Example
```
=== SSH Brute-Force Report ===
[OK] 192.168.1.20: 1 failed attempt(s)
[WARNING] 203.0.113.45: 6 failed attempts - possible brute-force
[CRITICAL] 198.51.100.7: 5 failed attempts, then a successful login - likely compromised
```

## Running it
```
python3 detector.py
```
It uses `sample_auth.log`, which is written in the same format as `/var/log/auth.log` on Ubuntu.

## What I learned
- How SSH logs record failed and successful logins
- Pulling the IP out by finding the word "from" instead of a fixed position, because "invalid user" lines have extra words
- Using a dictionary to count and a set to track successful logins

## What I'd improve
- It doesn't check the order of events, so a successful login before the failures would still show as critical
- It doesn't look at timing (5 failures in 5 seconds vs over a week)
- The file name and threshold are hardcoded
