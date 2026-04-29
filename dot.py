# from fastapi import FastAPI
 
# app = FastAPI()
 
# @app.get("/sample")
 
# def first():
#      return{"hello"}

# @app.get("/view/{id}")

# def second(id):
#      return f"id:{id}"

# @app.get("/viewquery")

# def third(id):
#      return f"id:{id}"

from fastapi import FastAPI
 
emp=[
    {"id":101, "name":"Jenish", "Rank":"1"}
]
 
app = FastAPI()
 
@app.get("/sample/{id}")
 
def view(id:int):
    for i in emp:
        if i[ "id" ]==:
            return i