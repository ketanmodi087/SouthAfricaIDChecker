# SouthAfricaIDChecker

This web page allows you to enter your South African ID number to uncover key information and check if any significant public holidays fall on your date of birth.

# Getting Started
1. Download Docker
2. Clone repo
3. cd to the repo base folder
4. create .env file at root directory and set it.
bash
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
API_KEY=<Your API Key>

5. run the following

bash
docker compose build
docker compose up


# Code Structure - Django App
1. idvault -  The method validates the SA ID, extracts details, updates the database, and fetches public holiday data for new records.