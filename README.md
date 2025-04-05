
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

## 🐳 Docker Deployment (Production)

This project supports containerized deployment using Docker and PostgreSQL.

---

### 🔧 Prerequisites

- Docker installed
- Docker Compose installed

---

### 📁 Environment Setup

1. Copy the example environment file:
   ```bash
   cp .env.template .env
   ```

2. Fill in your secrets in `.env`. Example:

   ```env
   DEBUG=False
   SECRET_KEY=your-secret-key

   DATABASE_ENGINE=django.db.backends.postgresql
   DATABASE_NAME=supplysage
   DATABASE_USER=postgres
   DATABASE_PASSWORD=postgres
   DATABASE_HOST=db
   DATABASE_PORT=5432

   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.mailtrap.io
   EMAIL_PORT=587
   EMAIL_HOST_USER=your_user
   EMAIL_HOST_PASSWORD=your_pass
   EMAIL_USE_TLS=True
   DEFAULT_FROM_EMAIL=admin@supplysage.com
   EMAIL_SUBJECT_PREFIX=[SupplySage]
   ```

---

### 🚀 Build & Run

From the project root, run:

```bash
docker-compose up --build
```

This will:
- Build the Django image
- Start the PostgreSQL container
- Inject environment variables from `.env`
- Serve your app at `http://localhost:8000`

---

### 🛠 Common Management Commands

Run migrations:

```bash
docker-compose exec web python manage.py migrate
```

Create an admin user:

```bash
docker-compose exec web python manage.py createsuperuser
```

Access the Django shell:

```bash
docker-compose exec web python manage.py shell
```

View the PostgreSQL database:

```bash
docker-compose exec db psql -U $DATABASE_USER -d $DATABASE_NAME
```

---

### ✅ Web Access

- Visit `http://localhost:8000/items/` — main dashboard
- Visit `http://localhost:8000/admin/` — admin panel

Use your superuser credentials to log in.

---

### 🧪 Tip: Verify PostgreSQL is Running

Check logs:

```bash
docker-compose logs db
```

Access the DB directly:

```bash
docker-compose exec db psql -U postgres -d supplysage
```

List tables:

```sql
\dt
```

---

### 📦 Notes

- The app uses `gunicorn` as the WSGI server in production.
- Environment variables are injected via `.env` at **runtime** (not during build).
- The PostgreSQL volume persists data even across container restarts.

---

Happy Deploying! 🐳🔥

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

## 📄 License

This project is **proprietary**. All rights reserved.

You may not use, copy, distribute, or modify any part of this code without explicit written permission from the author.

Contact: [Email](mailto:contact@kuscko.com) or [GitHub](https://github.com/Kuscko)

