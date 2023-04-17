## Instructions

Always in the project root directory, follow these steps:

1. First, install Python packages needed for this project, by running the following command:
    `pip install -r requirements.txt`
2. Set .env file variable values (head to sample.env to check which variables are needed)
3. Once .env variables are in place it's time to setup and seed the database, by running the following command:
    `python3 -m data.setup_db`
3. All set, now run the following command to start the API service (available on your localhost on port 4000 (if free)):
    `python3 app.py`

## Observations (important)
- Branch ***master*** was created, since branch **main** is protected and it wouldn't let me push anything
- **.env** file was purposely not excluded from version control, to make it easier for you guys to run (and since there's no sensitive information in it)