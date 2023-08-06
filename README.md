# Django-CRUD-demo

I have developed this based on the tutorial of https://github.com/flatplanet/Django-CRM. Django-CRUD-demo is a CRM dashboard built with Django and MySQL. It allows users to perform CRUD (Create, Read, Update, Delete) operations on data stored in a MySQL database.

## Features

- **Edit data**: Edit any data from the table.
- **Add data**: Add single data or bulk data.
- **Retrieve data**: Retrieve data in bulk by querying any field.
- **User login**: User login is timed and the timer is displayed on the webpage.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up a MySQL database and update the `DATABASES` setting in `settings.py` with your database credentials.
4. Run `python manage.py migrate` to create the necessary database tables.
5. Start the development server by running `python manage.py runserver`.

## Usage

Once the development server is running, you can access the CRM dashboard by visiting `http://localhost:8000` in your web browser. Log in with your username and password to access the dashboard and start using the CRUD features.

## Screenshots

Include screenshots of your project here to give users a visual overview of what your project looks like and how it works.


![Login Page](/screenshots/login_page.png)

![Registration Page](/screenshots/register_page.png)

![Dashboard Page](/screenshots/main_page.png)

![Showing Single Page](/screenshots/showing_single_record.png)

![Updating Single Page](/screenshots/updating_single_record.png)

![Addition of Single Record](/screenshots/adding_single_record.png)
