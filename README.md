
---

# 🍴 Django ORM Project

This project demonstrates how to use **Django ORM** to create models, run migrations, and add data using scripts.

---

## ⚙️ Setup Steps

1. **Create a new app (Core)**

   ```bash
   python manage.py startapp core
   ```

   ✅ This creates a folder called **core**.

2. **Add apps in `settings.py`**
   Inside your main project folder (`orm_django/settings.py`), add:

   ```python
   INSTALLED_APPS = [
       # ...
       'django_extensions',  # for running scripts easily
       'core',               # our main app
   ]
   ```

3. **📖 Learn Models**
   To understand Django models, visit the official docs:
   👉 [https://docs.djangoproject.com/en/5.2/topics/db/models/](https://docs.djangoproject.com/en/5.2/topics/db/models/)

---

## 🧱 Database Migrations

If you create or modify models in `core/models.py`, you must **propagate changes** to the database using migrations.

### 🔹 1. Create migrations

```bash
python manage.py makemigrations
```

➡️ Generates migration files based on model changes.

### 🔹 2. Apply migrations

```bash
python manage.py migrate
```

➡️ Updates the database structure.

💡 **Rule:**
Every time you edit `models.py`
→ run `makemigrations` → then `migrate`

---

## 🧑‍💻 Admin Panel

To register models in the Django Admin, open `core/admin.py` and register your models.

Example:

```python
from django.contrib import admin
from .models import Restaurant

admin.site.register(Restaurant)
```

Then create a **superuser**:

```bash
python manage.py createsuperuser
```

---

## 🧩 Scripts Folder

Create a folder named **scripts** inside the `core` app.
We use this to add or manipulate data directly from scripts.

**Folder structure:**

```
core/
 ├── models.py
 ├── admin.py
 ├── scripts/
 │    └── orm_script.py
```

---

## 🧠 Running Scripts

Make sure your script has a `run()` function like this:

```python
from core.models import Restaurant

def run():
    print("Saving data...")
    Restaurant.objects.create(name="Domino's", city="Pune")
```

Then run the script using:

```bash
python manage.py runscript orm_script
```

---

## 🧾 ORM Basics

| Action              | Command                                 | Description         |
| ------------------- | --------------------------------------- | ------------------- |
| 🔍 Get all data     | `Restaurant.objects.all()`              | Returns all records |
| 🥇 Get first record | `Restaurant.objects.first()`            | Returns first row   |
| 💾 Add data         | `Restaurant.objects.create(name="ABC")` | Adds new record     |

---

## 🐚 Using Django Shell

To query the database interactively:

```bash
python manage.py shell_plus --print-sql
```

This opens an advanced shell showing SQL queries being executed.

---

## ✅ Summary

* `startapp core` → create the core app
* Add `'django_extensions'` and `'core'` to `INSTALLED_APPS`
* `makemigrations` → create migration files
* `migrate` → apply changes
* `createsuperuser` → access admin panel
* `runscript` → run custom scripts
* `shell_plus` → interact with ORM

