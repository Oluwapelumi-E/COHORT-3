#env\scripts\activate
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app=FastAPI()

# @app.get("/")
# def rootAPI():
#   return{
#     "message":"This is the first fastAPI class"
#   }
templates=Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles( directory="static"), name="static")
@app.get("/response", response_class=HTMLResponse)
def basicRendering(request: Request):
   return templates.TemplateResponse("home.html",
                                      {"request": request, "name":"Ijesha Grandland Association Development"})


# templates=Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles( directory="static"), name="static")
# @app.get("/response", response_class=HTMLResponse)
# def basicRendering(request: Request):
#    return templates.TemplateResponse("home.html",
#                                       {"request": request, "name":"Amusan Oluwapelumi Esther"})

@app.get("/name")
def rootAPI():
  return[{
    "Fullname": "AMUSAN OLUWAPELUMI ESTHER"
  },
  {
    "testing":"test me"
  }]
# @app.get("/tiktok")
# def tiktok():
#   print("tiktok")
# @app.get("/user")
# def user(): 
#  return{
#    "user":"this is real me"
# }









#write an API that returns:
# 1 - string as a key and integer as a value
# 2 - string as a key and bool as a value
# 3 - string as a key and float as a value
# @app.get("/israel")
# def israel():
#   return[{
#     "Biscuit":3
#   },
#   {
#     "Two_orange":False
#   },
#   {
#     "Decimal_point":0.1
#   }]

class Items (BaseModel):
  name:str
  price:float
  is_available:bool=True

  class payment(BaseModel):
    address:str
    phone_num:int
    price:float
    vat:float
    total:float

class productionDetails(BaseModel):
    image:str
    price:float
    description:str
    rating:float 
Usernames=[]
  
@app.post("/user")
def create_user (username: str):
    Usernames.append(username)
    return Usernames

# ASSIGNMENT ARRAY
CarBrands=[]

@app.post("/CarModel")
def create_Model (CarBrand: str):
    CarBrands.append(CarBrand)
    return CarBrands

# RETURNS VALUE
@app.post("/name")
def MyName():
   return{
      "AMUSAN OLUWAPELUMI ESTHER"
   }
   
  #  DICTIONARY
# Biodata={
#   "Fullname":"Amusan Oluwapelumi",
#   "Phone Number":"07050834499",
#   "Gender":"Female",
#   "Bio": "Software Developer",
#   }
Biodatas=[]
@app.post("/Biodata")
def create_data(Biodata: str):
   Biodatas.append(Biodata)
   return Biodatas

# model
class Agent(BaseModel):
   fullname:str
   Business_name:str
   email:str
   phone_num:int
   review:int
   address:str
   next_of_kin:str
   business_verification:bool
   gender:str
class Landlord(BaseModel):
   Fullname:str
   gender:str
   property_address:str
   address:str
   phone_num:int
   review:str
class buyer(BaseModel):
   Fullname:str
