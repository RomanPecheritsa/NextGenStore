# NextGen Store

## Project Description

An online store project that will be finalized in each lesson throughout the course.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/RomanPecheritsa/NextGenStore
cd NextGenStore
```
### 2. Copy the env.example file to .env:

Open.env and replace the values of the variables with your own

```bash
cp env.example .env
```

### 3. Install Dependencies
The project uses Poetry for dependency management. Ensure Poetry is installed, then run the following command to install all dependencies:
```bash
poetry install
```
### 4. Run the Project
To start the server and start migrations, use the following command:
```bash
python3 manage.py migrate
python3 manage.py runserver
```
The server will be available at http://127.0.0.1:8000