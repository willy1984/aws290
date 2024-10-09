from flask import Flask, render_template, request
from databases.db import *
from controller.admin_s3 import *

app = Flask(__name__)

@app.route("/")
def home_func():
    return render_template("home.html")

@app.route("/register_page")
def register_page_funt():
    return render_template("register.html")

@app.route("/register_user", methods=["post"])
def register_render_funt():
    data = request.form
    file = request.files
    id = data["id"]
    name = data["name"]
    lastname = data["lastname"]
    birthday = data["birthday"]
    photo = file["photo"]
    #add_user(id, name, lastname, birthday) esto solo lo comentamos para saber si se guarda la foto
    upload_file_s3(photo, id)
    return "The user was adder"

@app.route("/consult_page")
def consult_page_func():
    return "vista de consulta"

if __name__ == "__main__" :
    host = "127.0.0.1"
    port = "3000"
    app.run(host, port, debug=True)