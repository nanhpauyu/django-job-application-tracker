# Django Job Application Tracker

Tracking job applications can be tedious, so I created the **Django Job Application Tracker** to help job hunters stay organized.

## Features
This is a responsive web application built using the Django framework. It helps track job applications and provides statistics for better analysis. Additionally, it integrates **Gemini AI** to summarize job descriptions, offering concise insights.

**Note:** This tool must be used alongside the [Job Application Chrome Plugin](https://github.com/nanhpauyu/job-application-plugin).

## Technologies Used
- **Backend:** Python, Django, Django REST Framework
- **Frontend:** HTML5, CSS, Tailwind, JavaScript
- **Database:** PostgreSQL
- **Hosting & Development:** Vercel, GitHub, VS Code

## Installation and Usage

### Method 1: Running Locally

#### Prerequisites
- Install Python on your machine.
- Create an account on [aiven.io](https://aiven.io/) to set up a free PostgreSQL server.
- Obtain a [Gemini AI API Key](https://ai.google.dev/gemini-api/docs) from Google.

#### Setup Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nanhpauyu/django-job-application-tracker.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd django-job-application-tracker
   ```
3. **Create a Virtual Environment:**
   ```bash
   python -m venv env_name
   ```
   - **Activate the Virtual Environment:**
     - Windows (Command Prompt): `path\to\venv\Scripts\activate`
     - Windows (PowerShell): `./path/to/venv/Scripts/Activate`
     - macOS/Linux: `source path/to/venv/bin/activate`

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Configure the Database:**
   - Create a **PostgreSQL service** on Aiven.io (free version).
   - Create a `.env` file and add the following:
     ```python
     DB_USER='your_db_user'
     DB_PASSWORD='your_db_password'
     DB_HOST='your_db_host'
     DB_PORT='your_db_port'
     API_KEY_G='your_gemini_api_key'
     ```
6. **Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
7. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the instructions to create an admin account.

8. **Run the Application:**
   ```bash
   python manage.py runserver
   ```
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
   - Log in with the username and password you created.

9. **Update the Plugin URL** in [Job Application Chrome Plugin](https://github.com/nanhpauyu/job-application-plugin).

---

### Method 2: Deploying on Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fdjango&demo-title=Django%20%2B%20Vercel&demo-description=Use%20Django%204%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fdjango-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994241/random/django.png)

#### Steps to Deploy
1. **Fork the Repository** to your GitHub or upload the project to your GitHub repo.
2. **Create an Account on Vercel** if you don’t have one.
3. **Go to Vercel Dashboard** → Click **Add New Project**.
4. **Connect Vercel with GitHub** and select your repository.
5. **Add Environment Variables**
   - Copy the contents of your `.env` file and add them to Vercel’s **Environment Variables** section.
6. **Deploy the Application** by clicking **Deploy**.

7. **Update the Plugin URL** in [Job Application Chrome Plugin](https://github.com/nanhpauyu/job-application-plugin).

---

### 🎉 Congratulations! You have successfully set up the Django Job Application Tracker.


![Login](/images/a.png)

![Overview](/images/b.png)

![Applications](/images/c.png)

![Application](/images/d.png)

![Detailpage](/images/e.png)

![UpdateStatus](/images/f.png)