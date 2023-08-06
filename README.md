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

Here we have included screenshots for this website's different page.

- **Login Page**: This is the login page for the CRM dashboard. Users can enter their username and password to log in and access the dashboard.
![Login Page](/screenshots/login_page.png)

- **Login Page**: This is the login page for the CRM dashboard. Users can enter their username and password to log in and access the dashboard.
![Registration Page](/screenshots/register_page.png)

- **Login Page**: This is the login page for the CRM dashboard. Users can enter their username and password to log in and access the dashboard.
![Dashboard Page](/screenshots/main_page.png)

- **Login Page**: This is the login page for the CRM dashboard. Users can enter their username and password to log in and access the dashboard.
![Showing Single Page](/screenshots/showing_single_record.png)

- **Updating Single Page**: This page allows users to update a single record in the database. Users can edit the fields of the record and save their changes.
![Updating Single Page](/screenshots/updating_single_record.png)

- **Addition of Single Record**: This page allows users to add a new record to the database. Users can enter the details of the new record and save it to the database.
![Addition of Single Record](/screenshots/adding_single_record.png)

- **Addition of Bulk Record with Excel**: This page allows users to add multiple records to the database at once by uploading an Excel file. Users can select an Excel file containing their data and upload it to add the records to the database.
![Addition of Bulk Record with Excel](/screenshots/adding_bulk_excel.png)

- **Download all Records in Excel**: This page allows users to download all records from the database in an Excel file. Users can click the "Download" button to download an Excel file containing all of their data.
![Download all Records in Excel](/screenshots/download_all_excel.png)

- **Download any Record in Excel**: This page allows users to download specific records from the database in an Excel file. Users can enter a query to search for records and download an Excel file containing the matching records.
![Download any Record in Excel](/screenshots/download_query_excel.png)


