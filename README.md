# EchoPulse 🎶

## Description
**EchoPulse** is a dynamic Django web application designed to connect music fans with the latest band events, albums, and fan voting features. It offers a seamless user experience with full user authentication, profile management, and interactive content like event listings and albums.

Whether you're promoting your band or building a fanbase, EchoPulse helps manage everything from event announcements to community engagement—all through a stylish, mobile-friendly interface.

---

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

---

## Features
- 🎤 User Registration & Login
- 🎵 Band Albums Display
- 📅 Event Listings
- 🧑‍💼 User Profile Management
- 🗳️ Fan Voting Options
- 🎨 Custom CSS Styling with Bootstrap
- 🔐 Authenticated Redirects

---

## Installation

### Requirements
- Python 3.10+
- Django 4+
- Git

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/R-B427/echopulse.git
   cd echopulse

2. **Create and Activate Virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply Migrations**
```bash
python manage.py migrate
```

### Docker Usage
1. **Build Docker Image**
```bash
docker build -t echopulse
```

2. **Run Docker Container:**
```bash
docker run -d -p 8080:8000 --name echopulse_container echopulse
```

3. **Access the App in Browser:**
```bash
Visit http://localhost:8080
```

4. **Stop Container**
```bash
docker stop echopulse_container
```


### Usage

1. **Run the Development Server:**
```bash
python manage.py runserver
```

2. **Open in Browser**
```bash
isit http://127.0.0.1:8080
```

3. **Explore Features**
-Register/Login

-Browse albums and events

-Favorite albums

-View event details

### Credits
Developed By: Ruben Brown
GitHub: https://github.com/R-B427/ConsolidationTask