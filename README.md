# Password Strength Checker

A Python tool to enforce strong passwords for cybersecurity practice.  
This program helps users create secure passwords by checking multiple security requirements and providing feedback until all criteria are met.

## Features

The password checker validates passwords for:

- Minimum **8 characters**  
- Includes both **uppercase and lowercase letters**  
- Contains **numbers and special characters**  
- No **three or more identical characters** in a row (e.g., 'aaa')  
- No **three or more sequential characters** in keyboard or number order (e.g., 'qwe', '123', 'edc')  

It provides **real-time feedback** and allows the user to re-enter the password until it meets all security requirements.

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/JohnRom21/Password-Strength-Checker.git
```

2. Navigate into the project folder:
```bash
cd Password-Strength-Checker
```
3. Run the Python script
```bash
python password_checker.py
```
