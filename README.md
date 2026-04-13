# 🔐 Secure File Transfer Monitoring System

A **real-time file monitoring and integrity verification system** built using Python.
This project tracks file activities, detects sensitive files, and verifies file integrity using SHA-256 hashing — all visualized through a modern web dashboard.

---

## 📌 Features

* 📂 **Real-time file monitoring**

  * Detects file creation, modification, deletion, and movement
* 🔍 **Sensitive file detection**

  * Based on file extensions and keywords
* 🔐 **Integrity verification**

  * Uses SHA-256 hashing to detect changes
* 🧾 **Event logging**

  * Logs stored in CSV format
* 🌐 **Web dashboard**

  * Clean UI to visualize activity
* ⚡ **Lightweight & modular design**

---

## 🛠️ Tech Stack

* Python
* Flask (Web framework)
* Watchdog (File monitoring)
* Hashlib (SHA-256 hashing)
* CSV / JSON (Data storage)
* HTML + CSS (Frontend dashboard)

---

## 📁 Project Structure

```id="t9cazw"
secure-file-monitor/
│
├── monitor.py          # File monitoring system
├── logger_util.py      # Logging system (CSV)
├── helper.py           # Sensitive file detection
├── integrity.py        # Hash calculation & storage
├── config.py           # Configurations
│
├── app.py              # Flask web app
├── requirements.txt    # Dependencies
├── Procfile            # Render deployment
│
├── templates/
│   └── index.html      # Dashboard UI
│
├── file_events.csv     # Generated logs
├── hashes.json         # Stored hashes
```

---

## 📊 How It Works

1. **Watchdog** monitors a folder (`C:\SFTMSTest`)
2. Events are captured (create, modify, delete, move)
3. Logs are saved into `file_events.csv`
4. Sensitive files are detected using rules
5. SHA-256 hashes are generated and stored
6. Flask dashboard displays activity

---

## 🔐 Sensitive File Rules

Defined in `config.py`:

* Extensions:

  ```
  .pdf, .docx, .xlsx, .csv, .env, .key
  ```
* Keywords:

  ```
  confidential, secret, password, salary, private
  ```

---

## 🧪 Example Log Entry

```id="y4jqax"
timestamp,event_type,source_path,destination_path
2026-04-13 20:10:15,created,C:\SFTMSTest\file.txt,
```

---

## 🚀 Future Improvements

* 🔴 Real-time dashboard updates
* 📊 Graph visualization
* 🔔 Alert system (Email/Webhook)
* 👤 User activity tracking
* ☁️ Cloud storage integration

---

## 👩‍💻 Author

**Pratiksha Dutta**

---

## 📜 License

Licensed under the **Apache License 2.0**

```id="0lpft6"
Copyright 2026 Pratiksha Dutta

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0
```

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
