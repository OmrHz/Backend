# Hospital DPI Management System

This project is a web application for managing **Dossier Patient Informatisé (DPI)**, which centralizes patient information like medical history, treatments, examination results, and prescriptions. It is designed to improve the quality of healthcare services and facilitate collaboration among medical staff.

---

## Features

- **Patient Management**:
  - Create, view, update, and delete patient records.
  - Search patient records by NSS or QR code.
- **Medical Operations**:
  - Record medical history, prescriptions, and examination summaries.
  - Generate trend graphs for patient data (e.g., blood pressure, cholesterol).
- **Personnel Module**:
  - Manage roles for doctors, nurses, pharmacists, and lab technicians.
- **Pharmacy Integration (SGPH)**:
  - Validate and track medication prescriptions.
  - RESTful API for inter-system communication.
- **Other Features**:
  - Responsive, ergonomic user interface.
  - Secure authentication and role-based access.

---

## Tech Stack

- **Backend**: Django with Python
- **Database**: MySQL
- **APIs**: RESTful architecture
- **Testing**: 
  - Unit testing with `pytest`
  - Functional testing with `Selenium`

---

## Installation

1. Clone the repository
2. create a virtual environment python -m venv .venv
3. activate the environment source .venv/bin/activate (linux) .venv\Scripts\Activate (windows)
4. update pip python -m pip install --upgrade pip
5. install requirements pip install -r requirements.txt
6. run the server python manage.py runserver 