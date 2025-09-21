# 🏢 HR Dashboard

A simple **HR Management Dashboard** built with **Django**, designed for managing employees and tracking attendance.  
Admins can manage employee records, while employees can log their attendance via a clean, responsive interface.

---

## ✨ Features

- 👨‍💼 **Employee Management**
  - Add, edit, delete employees  
  - Store details: department, role, salary, contact info, hire date  

- ⏰ **Attendance Tracking**
  - Employees can **Check-In / Check-Out**  
  - Daily attendance log linked to employee profiles  

- 📊 **Admin Dashboard**
  - View all employees  
  - Track attendance history  

- 🔐 **Authentication**
  - Admins and employees have separate dashboards  
  - Secure login/logout system  

- 📱 **Responsive UI**
  - Built with **Bootstrap 5** for mobile-friendly layouts  

---

## 🛠️ Technologies Used

- [Django](https://www.djangoproject.com/) (Python-based web framework)  
- [SQLite](https://www.sqlite.org/) (default database)  
- [Bootstrap 5](https://getbootstrap.com/) for styling  
- [Whitenoise](https://whitenoise.readthedocs.io/) for static file management  
- [dotenv](https://pypi.org/project/python-dotenv/) for environment variables  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/sawpaingchitmin/hr-dashboard.git
cd hr-dashboard
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
Create a .env file in the project root:
```bash
SECRET_KEY=your_secret_key
DEBUG=True
```

### 5. Apply migrations
```bash
python manage.py migrate 
# (If you modify models, run 'python manage.py makemigrations' before migrate)
```


### 6. Create a superuser (Admin)
```bash
python manage.py createsuperuser
```

### 7. Run the app
```bash
python manage.py runserver
```

## 📂 Project Structure 
```bash
hr_dashboard/
│── hr_core/
│   ├── templates/hr_core/
│   │   ├── add_employee.html
│   │   ├── attendance_history.html
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── edit_employee.html
│   │   ├── employee_dashboard.html
│   │   ├── employee_list.html
│   │   └── login.html
│   ├── models.py        # Employee & Attendance models
│   ├── urls.py          # App routes
│   ├── views.py         # HR dashboard logic (auth, attendance, employees)
│
│── hr_dashboard/
│   ├── settings.py      # Project settings
│   ├── urls.py          # Main project routes
│   └── wsgi.py
│
│── db.sqlite3
│── manage.py
│── requirements.txt
```

## 🌍 Live Demo

You can try the live version here:  
👉 [HR Dashboard on Render](https://hr-dashboard-3j8c.onrender.com)

### 🔑 Demo Credentials
- **Admin Login**
    - **Username:** `admin`  
    - **Password:** `password`  

> Use the above account to log in as an **Admin** and explore features like:
> - Adding, editing, and deleting employees  
> - Viewing attendance history  
> - Accessing the admin dashboard  

> After logging in as Admin, you can:  
> - Add new employee accounts  
> - Log out and re-login with an employee account to test the **Employee Dashboard** features.  




