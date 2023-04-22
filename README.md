Plant Monitoring System
This project is a Plant Monitoring System, which uses FastAPI for the backend and a microcontroller to collect data from various sensors.

Prerequisites
Make sure you have the following installed on your system:

Python 3.9+
Heroku CLI
Docker
Git
Setting up the project
Clone the repository and navigate to the project folder:
bash
Copy code
git clone https://github.com/yourusername/plant.git
cd plant
Create a virtual environment and activate it:
bash
Copy code
python -m venv env
For Windows:

bash
env\Scripts\activate
For macOS/Linux:

bash
source env/bin/activate

Install the required dependencies:
pip install -r requirements.txt

Running the application locally
Start the FastAPI server:
css
Copy code
uvicorn main:app --reload
Open your browser and navigate to http://127.0.0.1:8000 to access the application.
Deploying changes to Heroku
Ensure that you have the Heroku CLI installed and are logged in:
Copy code
heroku login
Pull the latest changes from your GitHub repository:
css
Copy code
git pull origin main
Build and push the updated container to Heroku:
lua
Copy code
heroku container:push web --app kplant
Release the updated container to your Heroku app:
sql
Copy code
heroku container:release web --app kplant
Your changes should now be reflected in the Heroku application.


Database Migrations
This project uses Alembic for handling database migrations. Here's a guide to managing migrations:

Setting Up Alembic
Install Alembic using pip: pip install alembic
Run alembic init alembic to create a new Alembic configuration in your project.
Creating a New Migration
Make changes to your SQLAlchemy models in your FastAPI application.
Run alembic revision --autogenerate -m "Your migration message" to create a new migration file with the changes detected from your models.
Review the generated migration file in the alembic/versions directory and make any necessary adjustments to the upgrade() and downgrade() functions.
Applying Migrations
To apply pending migrations, run alembic upgrade head. This command will upgrade your database schema to the latest version.
Rolling Back Migrations
To undo the last applied migration, run alembic downgrade -1. This command will downgrade your database schema by one version.
Viewing Migration History
To view the migration history and the current status of your database schema, run alembic history --verbose.