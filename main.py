from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

# This module contains all functionality required for db operation
from db_connector import My_DB

app = FastAPI()
my_db = My_DB()

templates = Jinja2Templates(directory="templates")

# It will show Login Page
@app.get('/')
async def name(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#This api will be called when a user wants to login after filling username and password, it will show two options to logined user, add user and view existing user
@app.post('/login')
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    status = my_db.validate_user(username, password)

    if status == "Success":
        return templates.TemplateResponse("action.html", {"request": request})
    else:
        return templates.TemplateResponse("loginError.html", {"request": request, "error": status})

# This api will be called if user want to add a new user    
@app.post('/add')
async def add(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

#This api will be called when user have filled details about new user and clicked on add user button
@app.post('/add_user')
async def add_user(request: Request, username: str = Form(...), password: str = Form(...)):
    my_db.add_user(username, password)
    return templates.TemplateResponse("userAdded.html", {"request": request})

#This api will be called when user clickedn on view user button
@app.post('/list_user')
async def list_user(request: Request):
    users = my_db.getAllUsers()
    return templates.TemplateResponse("users.html", {"request": request, "users": users})
