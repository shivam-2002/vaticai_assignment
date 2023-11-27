This is a Demo project usin FastAPI, mysql-connector, and Jinja2 Template. In this Project a new user will be created and during initialization of mysql-connector and that user will be able to add multiples users and the details of added user will be added in a table called vaticai_users.

steps involved during creation of this project:
1. Create Virtual Environment: python -m venv C:\Users\shiva\OneDrive\Desktop\UserLogin\venv
2. Activate Virtual Environment: & C:\Users\shiva\OneDrive\Desktop\UserLogin\venv\Scripts\Activate.ps1
3. install uvicorn: pip3 install uvicorn
4. install fastapi and jinja2: pip install uvicorn jinja2       
5. pip install python-multipart
6. pip install --upgrade mysql-connector-python

7. start server: uvicorn main:app --reload
	main is the file name of python file