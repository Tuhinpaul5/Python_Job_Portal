This is a FastAPI postgresql backend for a job portal website with sign up, log in and job posting api endpoints.


# Setting Up PostgreSQL and pgAdmin

This guide will help you install PostgreSQL and pgAdmin, and configure your application's database connection settings.



## Installation Steps

### Download PostgreSQL

- Visit the official PostgreSQL download page: [PostgreSQL Downloads](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- Choose the appropriate installer for your operating system and follow the installation prompts. This should usually download pgadmin4 along with it. You can use pgadmin4 to create and manage your databases.


## Configuration

Once PostgreSQL and pgAdmin are installed, you need to update your application's database connection settings in the `config.json` file.

### 1.Install `requirements.txt`

- Open a terminal window and navigate to the project directory.
- Run `pip install -r requirements.txt` to install the required packages.

### 2.Update `config.json`

Locate the `config.json` file in the project directory. Update the following fields with your PostgreSQL server details:

- **db_host**: The host where your PostgreSQL server is running. Use `"localhost"` if it's running on your local machine.
- **db_user**: Your PostgreSQL username. The default is usually `"postgres"`.
- **db_password**: Your PostgreSQL password. Leave it empty if you haven't set one yet.
- **db_name**: The name of the database you want to connect to. In this example, it's `"career"`.

This uses smtp to send emails for otps.

add the credentials in config.json file:

- **"hr_email"**: "add your hr email address",
- **"hr_password"**: "add the stmp app password for that email",
- **"email_subject"**: "your desired subject"

You can watch this video to know how to get your smtp password:

https://youtu.be/I9x0w8cjR_o?si=7dENqbnl-m2fBEei

## 4.Create a database named "career" 
(Note. Remember to change the name of the database in the config.json file if you use a database with a different name)

## 5.Run main.py

After updating the `config.json` file, run main.py to apply the changes and create the tables in the database automatically. Ensure that your PostgreSQL service is running and accessible. (You can acess your db using either pgadmin4 or the sql Shell).


## 6. Testing

You can test the API endpoints using postman or the frontend in the frontend folder.

## 1. User Enpoints : 

### 1. sending otp to the user email :
[POST]
http://localhost:8000/send_otp

{
    "email":"user.log.in@email.com"
}

### 2. Verify otp sent to the user's email :
[POST]
http://localhost:8000/verify_otp

{
    "email":"user.log.in@email.com", 
    "otp":"1234"
}

### 3. Setting user profile data :
[POST]
http://localhost:8000/profile_data

{
    "name": "user1",
    "phone": "1234567890",
    "email": "user.log.in@email.com",
    "address": "New York"
}

### 4. Fetches all user data from the database :
[GET]
http://localhost:8000/get_user_data


### 5. Update a specific user data (uses id to specify):
[POST]
http://localhost:8000/get_user_data

{
    "id": "915117",
    "name": "user2",
    "phone": "1234567890",
    "address": "Delhi"
}


## 2. Admin Endpoints :

### 1. Add jobs to the database :
[POST]
http://localhost:8000/admin/jobs/add_jobs

{
    "job_title": "Python Developer",
    "location": "Delhi",
    "department": "Production",
    "salary": "50-60k",
    "employment_type": "Full-Time",
    "responsibilities": "A lot",
    "requirements": "Python",
    "experience": "Too much"
}

### 2. Update an existing job :
[POST]
http://localhost:8003/admin/jobs/update_jobs

{
    "pk": "Production_5552",
    "job_title": "Javascript Dev",
    "location": "Delhi",
    "department": "Production",
    "salary": "50-60k",
    "employment_type": "Full-Time",
    "responsibilities": "NA"
}

### 3. Get all existing jobs :
[GET]
http://0.0.0.0:8000/admin/jobs/get_jobs

### 4. Delete posted jobs from database :
[POST]
http://0.0.0.0:8003/admin/jobs/delete_jobs

{
    "pk": "Production_5552"
}