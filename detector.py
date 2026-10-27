THRESHOLD = 3
failed_counts = {}
successful_logins = set()

# Read the log and record failed and successful logins per IP
with open("sample_auth.log") as log_file:
    for line in log_file:
        parts = line.split()
        if "Failed password" in line:
            ip = parts[parts.index("from") + 1]
            failed_counts[ip] = failed_counts.get(ip, 0) + 1
        elif "Accepted password" in line:
            ip = parts[parts.index("from") + 1]
            successful_logins.add(ip)

# Report on each IP
print("=== SSH Brute-Force Report ===")
for ip, count in failed_counts.items():
    if count >= THRESHOLD and ip in successful_logins:
        print(f"[CRITICAL] {ip}: {count} failed attempts, then a successful login - likely compromised")
    elif count >= THRESHOLD:
        print(f"[WARNING] {ip}: {count} failed attempts - possible brute-force")
    else:
        print(f"[OK] {ip}: {count} failed attempt(s)")

