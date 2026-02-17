# PSUSphere

### Short Description
PSUSphere is a Django project I built to manage student organizations at Palawan State University. It handles data for colleges, courses (programs), student lists, and organization memberships. It was created to replace manual tracking with a clean, centralized database.

### Features
* **Custom Data Script**: I used the `Faker` library to write a management command that automatically generates 50 students and 10 organizations so the app isn't empty during testing.
* **Admin Refactor**: I updated `admin.py` to include search bars for names/IDs and filters for different colleges to make navigation faster.
* **Dashboard UI**: Instead of the default Django look, I integrated the `Jazzmin` theme for a better, more modern sidebar layout.
* **Relationship Mapping**: The system links students to their specific programs and organizations, tracking exactly when they joined.
* **Activity Logs**: All records automatically track when they were created or last updated.

### Authors
* **[LanceSthur Keith Tapaya]**
* BS in Information Technology
* Palawan State University

---

### Quick Setup for Testing
1. Activate environment: `source psusenv/bin/activate`
2. Install requirements: `pip install -r requirements.txt`
3. Migrate & Load Data: `python manage.py migrate` then `python manage.py create_initial_data`
4. Run: `python manage.py runserver`