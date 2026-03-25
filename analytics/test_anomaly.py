from analytics.anomaly import detect_anomalies

anomalies = detect_anomalies()

print("\nDetected anomalies:\n")

for row in anomalies:
    print(row)
