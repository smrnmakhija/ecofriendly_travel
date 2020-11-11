Running project:

Install Python3

Install requirements

	pip install -r requirement.txt

Set up a venv

	pip install virtualenv
	python3 -m venv recipe_venv
	Activate : .\recipe_venv\Scripts\activate
	
	
Migrations for DB

	python3 manage.py makemigrations
	python3 manage.py migrate
	
	
Run server
		
    python3 manage.py runserver