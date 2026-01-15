🛡️ LogAlert – Brute Force Attack Detector:

LogAlert is a simple Python script that analyzes authentication log files to detect possible brute-force login attacks based on failed login attempts and timing patterns.


📌 Features:

Detects failed login attempts (HTTP 401)

Groups attempts by IP address

Flags potential brute-force attacks when:

An IP has 5 or more failed attempts

The time difference between attempts is constant


🧾 Log File Format:

Each log entry must start with a timestamp and include an IP address and status code.

Example:
"2025-01-14 10:00:00 INFO Login failed IP=192.168.1.50 STATUS=401"

Required fields:

Timestamp: YYYY-MM-DD HH:MM:SS

IP address: IP=<address>

Status code: STATUS=401

Blank or malformed lines are safely ignored.


🚀 How It Works:

Reads the log file line by line

Extracts timestamps, IP addresses and associated status codes

Stores failed attempts (401) per IP

Checks for:

At least 5 failed attempts

Equal time intervals between attempts

Raises an alert if both conditions are met


📚 Technologies Used:

Visual Studio Code

Python 3


⚠️ Limitations:

Assumes consistent log format

Detects only constant-interval brute force
