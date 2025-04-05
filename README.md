
# 📦 SupplySage

SupplySage is a Django-based inventory management system designed to help small businesses track stock levels, generate reports, and streamline day-to-day inventory tasks.

---

## 🚀 Features

- 🔧 Add, edit, and delete inventory items
- 🔍 Filter and search by name or category
- 📉 Automatic low-stock detection
- 📬 Email alerts when stock drops below threshold
- 📊 Dashboard with total inventory value
- 📥 Export reports to CSV and PDF
- 🔒 Role-based access (admin/staff)
- 🧪 Full test suite for reliability

---

## 🛠 Tech Stack

- **Backend**: Django 5.1+
- **Frontend**: Bootstrap 5
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Exporting**: `csv`, `reportlab`
- **Auth**: Django’s built-in user system

---

## ⚙️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/supplysage.git
   cd supplysage
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

---

## 🔐 Admin Access

- Visit `http://localhost:8000/admin`
- Use your superuser credentials to log in
- You can configure inventory settings, users, and permissions here

---

## 📝 Usage Notes

- The app's main entry is at `/items/`
- Admins and staff can be created through the Django admin interface
- To receive low-stock email alerts:
  - Set email backend in `settings.py`
  - Enable notifications in the **Inventory Settings** panel

---

## 📁 Project Structure

```
supplysage/
├── inventory/         # Core app: models, views, forms, templates
├── templates/         # Shared HTML templates
├── static/            # Static files (CSS, JS)
├── manage.py
└── requirements.txt
```

---

## 🧪 Running Tests

```bash
python manage.py test inventory
```

Tests cover:
- Inventory filtering
- Low stock flags
- Email notifications
- Value calculations

---

## 📨 Email Setup (Dev Mode)

To see emails in the console, add to `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'admin@supplysage.com'
ADMINS = [('Admin', 'admin@example.com')]
```

---

## 📌 To-Do / Future Ideas

- 📦 Inventory import via CSV
- 📱 Mobile-friendly layout
- 📈 Analytics dashboard (daily movement, best sellers)
- 🌐 Multi-language support
- 🧾 Barcode/QR code scanning for quick item lookup and stock updates

---

## 🧑‍💻 Author

Made with love by **Patrick Kelly**  
[GitHub](https://github.com/Kuscko)

---

## 📄 Proprietary License

Copyright © 2025 Patrick Kelly

This software is proprietary and confidential. You may not use, copy, distribute, or modify any part of this code without explicit written permission from the author.

All rights reserved.

