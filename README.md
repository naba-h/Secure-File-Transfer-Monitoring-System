# Secure File Transfer Monitoring System  

A defensive cybersecurity monitoring tool developed in Python to detect unauthorized file access, modification, movement, and deletion in real time. This project implements host-based file system monitoring, alert generation, and cryptographic integrity verification techniques commonly used in enterprise security environments.

---

## 📖 Overview  

Modern organizations depend heavily on secure file handling and controlled data movement. Unauthorized modification, deletion, or transfer of sensitive files can result in data breaches, insider threats, and compliance violations.  

The Secure File Transfer Monitoring System is a Python-based application that continuously observes file system activity within a protected directory. It detects file creation, modification, movement, and deletion events, identifies sensitive file operations, and generates security alerts along with cryptographic integrity verification.  

This project simulates the behavior of a lightweight Host-Based Intrusion Detection System (HIDS) and demonstrates practical defensive security monitoring concepts used in real-world environments.

---

## 🎯 Objectives  

- Monitor file system activity in real time  
- Detect operations performed on sensitive and protected files  
- Generate alerts for unauthorized access and modification  
- Verify file integrity using cryptographic hash functions  
- Maintain structured audit logs for forensic analysis  

---

## 🔐 Core Security Features  

- Real-time file system monitoring  
- Classification and tracking of sensitive files  
- Automatic security alert generation  
- SHA-256 based integrity verification  
- User activity tracking  
- Detailed audit logging for incident investigation  

---

## 🛠️ Technologies Used  

- Programming Language: Python  
- Operating System: Windows  
- Libraries and Modules:  
  - watchdog – file system event monitoring  
  - hashlib – cryptographic hashing (SHA-256)  
  - logging – structured security logging  
  - os, time, getpass – system utilities  

---

## 📂 Project Structure

Secure-File-Transfer-Monitoring-System  
├── config.py        # Configuration and sensitive file list
├── monitor.py       # Monitoring engine and alert logic
├── logs/
│   └── activity.log # Security audit log
├── monitored/       # Protected directory
├── screenshots/     # Execution evidence
└── reports/         # Final project documentation

---

## ▶️ How to Run  

1. Install required dependency:
   pip install watchdog
   
2. Navigate to the project directory:
   cd Secure-File-Transfer-Monitoring-System
   
3. Start the monitoring service:
   python monitor.py

4. Perform file operations inside the `monitored` directory and observe alerts and log entries.

---

## 📸 Execution Screenshots  

Below are key execution proofs captured during testing:

### 1️⃣ Monitoring Service Started  
![](screenshots/1_monitoring_started.png)

### 2️⃣ Normal File Creation Detected  
![](screenshots/2_normal_file_created.png)

### 3️⃣ Sensitive File Alert Triggered  
![](screenshots/3_sensitive_file_alert.png)

### 4️⃣ Activity Log with Integrity Verification  
![](screenshots/4_activity_log.png)

## 🧪 Testing and Validation  

The following scenarios were tested successfully:  

- Normal file creation detection  
- Sensitive file modification alert generation  
- File movement and deletion monitoring  
- File integrity verification using SHA-256 hashing  
- User activity logging and event correlation  

Execution screenshots and audit logs are available in the `screenshots` and `reports` directories.

---

## 🔍 Security Relevance  

This project demonstrates key defensive cybersecurity concepts including:  

- File Integrity Monitoring (FIM)  
- Host-Based Intrusion Detection  
- Insider Threat Detection  
- Audit Logging and Forensic Readiness  
- Incident Detection and Response Support  

Such mechanisms are widely used in enterprise Security Operations Centers (SOC) and compliance monitoring systems.

---

## 🚀 Future Enhancements  

- Email and real-time alert notifications  
- Centralized log storage and SIEM integration  
- GUI-based monitoring dashboard  
- Pattern-based sensitive data detection  
- Digital signatures for log protection  
- Network file transfer monitoring  

---

## 👩‍💻 Author  

**Naba Hanfi**  
Cybersecurity Intern – Unified Mentor  

---

## 📜 License  

This project is licensed under the MIT License.  

---

⭐ If you find this project useful, feel free to star the repository.

