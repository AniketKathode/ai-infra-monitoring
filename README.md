# Smart Monitor – Real-Time System Monitoring Dashboard

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-API-black)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Deployment-Live-green)

## About This Project

I built **Smart Monitor** to understand how real-world infrastructure monitoring systems work.  
The project collects live system metrics (CPU, memory, disk), stores them in a database, displays them on a dashboard, and detects unusual behaviour using statistical data science techniques.

This project helped me combine:
- backend development
- system monitoring
- data science
- and cloud deployment

---

## Live Demo

Dashboard:  
https://ai-infra-monitoring.onrender.com

---

## What Problem This Project Solves

When managing servers or applications, it is important to know:
- CPU usage
- memory consumption
- disk space

This project simulates how tools like Prometheus and Grafana monitor infrastructure in real time.

---

## Data Science Techniques Used

Instead of using heavy machine learning models, I implemented lightweight statistical anomaly detection.

The anomaly detection is based on:
- moving average calculation
- deviation threshold comparison
- time-series trend analysis

If a metric value deviates significantly from its recent historical average, it is flagged as an anomaly.

This approach is widely used in real monitoring systems because it is fast and efficient.

---

## System Architecture

![System](https://github.com/AniketKathode/ai-infra-monitoring/blob/main/Cloud%20Monitering/System%20Achi.png)
```
+-------------------+
|   System Metrics  |
| (CPU, Memory,Disk)|
+---------+---------+
          |
          v
+-------------------+
|  monitor.py       |
|  (psutil collector)|
+---------+---------+
          |
          v
+-------------------+
|   SQLite Database |
+---------+---------+
          |
          v
+-------------------+
|      Flask API    |
|  app.py           |
+---------+---------+
          |
          v
+-------------------+
|   Web Dashboard   |
| (HTML, JS, Charts)|
+-------------------+
```

---

## Project Features

- real-time metric collection every 5 seconds
- persistent storage of metrics
- interactive dashboard with charts
- anomaly detection based on statistical analysis
- Docker container support
- deployed on cloud (Render)

---

## Screenshots

### Local Monitoring
![Local](https://github.com/AniketKathode/ai-infra-monitoring/blob/main/Local%20System%20images/Local1.png)
![Local](https://github.com/AniketKathode/ai-infra-monitoring/blob/main/Local%20System%20images/Local2.png)
![Local](https://github.com/AniketKathode/ai-infra-monitoring/blob/main/Local%20System%20images/Local3.png)

### Cloud Monitoring
![Render](https://github.com/AniketKathode/ai-infra-monitoring/blob/main/Cloud%20Monitering/Cloud1.png)
![Render](https://github.com/AniketKathode/ai-infra-monitoring/blob/main/Cloud%20Monitering/Cloud2.png)
![Render](https://github.com/AniketKathode/ai-infra-monitoring/blob/main/Cloud%20Monitering/Cloud3.png)
---

## Why Local and Cloud Metrics Look Different

When running locally, the application monitors my laptop.  
When deployed, it monitors the cloud container instead.

Since the container has different CPU, memory, and disk limits, the graphs behave differently.  
This confirmed that the monitoring system is working correctly.

---

## Tech Stack

Backend:
- Python
- Flask

Monitoring:
- psutil

Database:
- SQLite

Frontend:
- HTML
- CSS
- JavaScript
- Chart.js

Deployment:
- Docker
- Render

---

## Project Structure

```
smart-monitor/
│
├── analytics/
│   └── anomaly.py
│
├── dashboard/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── app.py
├── monitor.py
├── metrics.db
└── Dockerfile
```

---

## API Endpoints

Get latest metrics:
```
/metrics/history
```

Get anomaly detection results:
```
/metrics/anomalies
```

Health check:
```
/healthz
```

---

## How Real-Time Updates Work

1. `monitor.py` collects system metrics using psutil.
2. Metrics are stored in SQLite.
3. Flask API exposes endpoints to fetch data.
4. The dashboard fetches data every few seconds and updates charts.

---

## Running the Project Locally

Install dependencies:
```
pip install -r requirements.txt
```

Run:
```
python app.py
```

Open:
```
http://localhost:5000
```

---

## Running with Docker

Build image:
```
docker build -t smart-monitor .
```

Run container:
```
docker run -p 5000:5000 smart-monitor
```

---

## What I Learned from This Project

While building this system, I learned:

- how real-time monitoring pipelines work
- how to collect system metrics using Python
- how to design REST APIs with Flask
- how to run background threads safely
- how containers behave differently from local environments
- how statistical methods can be applied to time-series anomaly detection

---

## Future Improvements

I plan to extend this project on next level by:
- adding email alerts for anomalies
- switching from SQLite to PostgreSQL
- integrating Prometheus metrics export
- applying machine learning models like Isolation Forest

---

## Author

Aniket  
Aspiring DevOps and Data Science Engineer

This project is part of my effort to build practical, production-like systems while learning backend engineering, cloud deployment, and data science.
