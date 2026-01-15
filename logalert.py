from collections import defaultdict
from datetime import datetime

log_file = input("Enter the path to the log file: ")
threshold = 5

failed_attempts = defaultdict(list)

if log_file:
    with open(log_file, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) < 2:
                continue
            timestamp_str = " ".join(parts[0:2])
            timestamp = datetime.strptime(
                timestamp_str, "%Y-%m-%d %H:%M:%S"
            )

            ip = None
            status = None

            for part in parts:
                if part.startswith("IP="):
                    ip = part.split("=")[1]
                elif part.startswith("STATUS="):
                    status = part.split("=")[1]

            if ip and status == "401":
                failed_attempts[ip].append(timestamp)
else:
    print(f"[ERROR] Log file '{log_file}' not found.")

print("\nLogalert Threat Report\n")

threat_found = False

for ip, timestamps in failed_attempts.items():
    if len(timestamps) >= threshold:
        timestamps.sort()

        time_diffs = [
            (timestamps[i + 1] - timestamps[i]).total_seconds()
            for i in range(len(timestamps) - 1)
        ]

        if len(set(time_diffs)) == 1:
            threat_found = True
            print(f"[ALERT] Possible Brute Force Attack Detected!")
            print(f"IP Address      : {ip}")
            print(f"Failed Attempts : {len(timestamps)}")
            print("Timestamps:")
            for time in timestamps:
                print(f"  - {time}")
            print("-" * 55)

if not threat_found:
    print("No brute-force attacks detected.")