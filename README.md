# Gerbang TETI - Web Exploitation CTF Challenge

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-black)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A Web Exploitation Capture The Flag (CTF) challenge that simulates a vulnerable university login portal. Participants are provided with a leaked credential list and must perform **Credential Stuffing** to discover the valid administrator credentials and retrieve the flag.

This challenge is designed for educational purposes, especially for learning:

- Web Exploitation
- HTTP Request Automation
- Credential Stuffing
- Python Requests
- Basic Brute Force Techniques

---

## Challenge Overview

A university portal named **Gerbang TETI** has suffered a credential leak.

Participants are given:

- A running web service
- A file named `credentials.txt`

Only **one** username-password pair is valid.

The goal is to automate login attempts until the correct credentials are found.

Successful authentication reveals the flag.

---

## Learning Objectives

After completing this challenge, participants should be able to:

- Understand HTTP POST authentication
- Automate web requests using Python
- Parse leaked credential datasets
- Perform Credential Stuffing attacks
- Understand why password reuse is dangerous

---

## Repository Structure

```
.
├── app.py
├── Dockerfile
├── requirements.txt
├── credentials.txt          # Distributed to participants
├── admin_creds.txt          # Secret (DO NOT distribute)
├── flag.txt                 # Secret (DO NOT distribute)
├── templates/
│   ├── login.html
│   ├── success.html
│   └── error.html
├── static/
└── README.md
```

---

## Running Locally

Clone the repository

```bash
git clone https://github.com/<username>/Gerbang-TETI-webEx-CTF-.git
cd Gerbang-TETI-webEx-CTF-
```

Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python app.py
```

Open

```
http://localhost:5000
```

---

## Running with Docker

Build image

```bash
docker build -t gerbang-teti .
```

Run container

```bash
docker run -d \
    --name gerbang-teti \
    -p 5000:5000 \
    gerbang-teti
```

Open

```
http://localhost:5000
```

---

## Deploy Using Cloudflare Tunnel

Expose the local service

```bash
cloudflared tunnel --url http://localhost:5000
```

Cloudflare will generate a public HTTPS URL similar to:

```
https://purple-tree-ab12.trycloudflare.com
```

Participants can access the challenge through this URL.

---

## Challenge Files

### Released to Participants

```
credentials.txt
```

### Secret Files

```
admin_creds.txt
flag.txt
```

Never distribute the secret files.

---

## Technologies Used

- Python 3
- Flask
- Gunicorn
- Docker
- Cloudflare Tunnel

---

## Educational Disclaimer

This project is intended **solely for educational purposes** in cybersecurity training and Capture The Flag competitions.

Do not use the techniques demonstrated here against systems without explicit authorization.

---
