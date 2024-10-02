from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home_func():
    return render_template("home.html")

@app.route("/register_page")
def register_page_funt():
    return render_template("register.html")

@app.route("/register_user", methods=["post"])
def consult_page_funt():
    data = request.form 
    id = data["id"]
    name = data["name"]
    lastname = data["lastname"]
    birthday = data["birthday"]
    add_user(id, name, lastname, birthday)
    print(data)
    return "The user was adder"

@app.route("/consult_page")
def consult_page_func():
    return "vista de consulta"

if __name__ == "__main__" :
    host = "127.0.0.1"
    port = "3000"
    app.run(host, port)