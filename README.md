# 🧠 MindMate - AI Powered Mental Wellness Assistant

> **An AI-powered mental wellness assistant built using Flask, Amazon Bedrock (Amazon Nova 2 Lite), and the YouTube Data API.**

MindMate is an intelligent web application that provides personalized motivational newsletters and recommends educational and wellness videos based on a user's mood, goals, and interests.

---

# 🌟 Features

## 🤖 AI Newsletter Generation

Generate personalized newsletters based on:

* User Name
* Current Mood
* Personal Goal
* Interests

Each newsletter includes:

* Personalized Greeting
* Motivation
* Productivity Tip
* Wellness Tip
* Motivational Quote
* Positive Closing Message

---

## 📺 AI YouTube Recommendations

MindMate intelligently recommends YouTube videos.

Instead of searching YouTube directly,

Amazon Bedrock:

* Understands the user's situation
* Generates intelligent search queries

Then

The YouTube Data API fetches:

* Video Title
* Thumbnail
* Channel Name
* Watch URL

This ensures users receive real and up-to-date recommendations.

---

## ☁ AWS Bedrock Integration

MindMate uses

**Amazon Bedrock**

Model:

**Amazon Nova 2 Lite**

Features:

* Prompt Engineering
* JSON Structured Responses
* Personalized AI Generation

---

# 🏗 System Architecture

```text
                         USER
                           │
                           ▼
                HTML / CSS / JavaScript
                           │
                   Fetch() / AJAX Request
                           │
                           ▼
                    Flask REST API
                           │
                /generate-dashboard
                           │
                           ▼
                 Prompt Builder Service
                           │
                           ▼
             Amazon Bedrock (Nova 2 Lite)
                           │
          ┌────────────────┴───────────────┐
          │                                │
          ▼                                ▼
 AI Newsletter                    YouTube Search Queries
          │                                │
          └───────────────┬────────────────┘
                          ▼
                  YouTube Data API
                          │
                          ▼
                  Video Recommendations
                          │
                          ▼
                    JSON Response
                          │
                          ▼
                 MindMate Dashboard
```

---

# 📂 Project Structure

```text
mindmate/

│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env
│
├── routes/
│   ├── chat.py
│   ├── dashboard.py
│   ├── newsletter.py
│   └── youtube.py
│
├── services/
│   ├── bedrock_service.py
│   ├── youtube_service.py
│   ├── prompt_builder.py
│
├── utils/
│   └── json_parser.py
│
├── templates/
│   └── dashboard.html
│
├── static/
│   ├── css/
│   └── js/
│
└── screenshots/
```

---

# 🚀 Technologies Used

## Backend

* Python
* Flask
* REST API
* Boto3

---

## Frontend

* HTML5
* CSS3
* JavaScript
* Fetch API

---

## Artificial Intelligence

* Amazon Bedrock
* Amazon Nova 2 Lite
* Prompt Engineering
* JSON Structured Output

---

## Cloud

* AWS IAM
* Amazon Bedrock Runtime
* AWS Credentials

---

## External APIs

* YouTube Data API v3

---

# 🔄 Application Workflow

## Step 1

User enters

* Name
* Mood
* Goal
* Interest

---

## Step 2

Frontend sends

```text
POST /generate-dashboard
```

---

## Step 3

Flask receives the request.

---

## Step 4

Prompt Builder creates a personalized prompt.

---

## Step 5

Amazon Bedrock generates:

* Newsletter
* Productivity Tip
* Wellness Tip
* Quote
* Five YouTube Search Queries

---

## Step 6

Flask extracts the generated YouTube queries.

---

## Step 7

The YouTube API searches for real videos.

---

## Step 8

Flask combines:

* Newsletter
* Videos

into one JSON response.

---

## Step 9

Dashboard displays

* AI Newsletter
* Recommended Videos

---

# 📊 API Endpoints

## Generate Dashboard

```
POST /generate-dashboard
```

Request

```json
{
    "name":"Sakthi",
    "mood":"Stress",
    "goal":"Become DevOps Engineer",
    "interest":"AWS"
}
```

Response

```json
{
    "newsletter": {
        "greeting":"...",
        "motivation":"...",
        "productivity_tip":"...",
        "wellness_tip":"...",
        "quote":"...",
        "closing":"..."
    },
    "videos":[
        {
            "title":"...",
            "channel":"...",
            "thumbnail":"...",
            "url":"..."
        }
    ]
}
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/mindmate.git

cd mindmate
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Linux

```bash
source venv/bin/activate
```

Windows

```cmd
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python app.py
```

---

# 🔐 Environment Variables

Create

```
.env
```

```env
SECRET_KEY=your_secret_key

AWS_ACCESS_KEY_ID=xxxxxxxx

AWS_SECRET_ACCESS_KEY=xxxxxxxx

AWS_REGION=ap-south-1

BEDROCK_MODEL_ID=global.amazon.nova-2-lite-v1:0

YOUTUBE_API_KEY=xxxxxxxx
```

---

# 📈 Future Improvements

* User Authentication
* Journal Analysis
* Mood Tracking
* Daily Wellness Plan
* AI Chat Assistant
* PostgreSQL Database
* Docker Support
* Kubernetes Deployment
* AWS EC2 Deployment
* CI/CD using GitHub Actions
* CloudWatch Monitoring
* Prometheus & Grafana
* Terraform Infrastructure
* HTTPS using Nginx

---

# 🎯 Learning Outcomes

This project demonstrates:

* Flask REST API Development
* AWS Bedrock Integration
* Amazon Nova 2 Lite
* Prompt Engineering
* JSON Parsing
* API Integration
* YouTube Data API
* Frontend–Backend Communication
* AI Application Architecture
* Python Project Organization

---

# 📸 Screenshots

Add screenshots here.

```
screenshots/
```

* Dashboard
* AI Newsletter
* Recommended Videos

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sakthi Velan**

AWS Certified Cloud Practitioner

Artificial Intelligence & Data Science Student

Cloud | DevOps | AI | Open Source
