import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from myforms.forms import ChangePassForm, RegistrationForm,\
Add_CheckForm, LoginForm

if os.path.exists("env.py"):
    import env
    

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")


@app.route("/get_checks")
def get_checks():
    checks = mongo.db.checks.find()
    return render_template("checks.html", checks=checks)

@app.route("/get_manager_checks")
def get_manager_checks():
    checks = mongo.db.checks.find()
    return render_template("manager_checks.html", checks=checks)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    checks = list(mongo.db.checks.find({"$text": {"$search": query}}))
    return render_template("checks.html", checks=checks)

'''
The Register function calls RegistrationForm class from forms.py. 
form.py checks that the username and passwords are valid 
Checks if the username already exists in database. 
Hashes the entered password and adds a new user to session.
'''

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST" and form.validate():
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "fname": request.form.get("fname"),
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("home", username=session["user"]))
    return render_template("register.html", form=form)

'''
The login function calls LoginForm class from forms.py. 
form.py checks that the username and passwords 
are valid. User is added to the session. 

'''

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})


        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "home", username=session["user"]))

                        
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html",form=form)



@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    user = mongo.db.users.find_one({"username": username.lower()})
    check = mongo.db.checks.find_one({"username": username.lower()})

    if "user" in session:
        return render_template(
           "profile.html", user=user, check=check)
        
        
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

#The function calls Add_CheckForm class from forms.py
@app.route("/add_check", methods=["GET", "POST"])
# form variable to initialise the form

def add_check():
    form = Add_CheckForm()
    if request.method == "POST" and form.validate():
        screen_q1 = True if request.form.get("screen_q1") else False
        screen_q2 = True if request.form.get("screen_q2") else False
        chair_q1 = True if request.form.get("chair_q1") else False
        chair_q2 = True if request.form.get("chair_q2") else False
        keyboard_q1 = True if request.form.get("keyboard_q1") else False
        keyboard_q2 = True if request.form.get("keyboard_q2") else False
        mouse_q1 = True if request.form.get("mouse_q1") else False
        mouse_q2 = True if request.form.get("mouse_q2") else False
        environment_q1 = True if request.form.get("environment_q1") else False
        environment_q2 = True if request.form.get("environment_q2") else False
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        check = {
            "manager_name": request.form.get("manager_name"),
            "dept_name": request.form.get("dept_name"),
            "max_total_time": request.form.get("max_total_time"),
            "max_continuous_time": request.form.get("max_continuous_time"),
            "screen_q1": screen_q1,
            "screen_q2": screen_q2,
            "chair_q1": chair_q1,
            "chair_q2": chair_q2,
            "keyboard_q1": keyboard_q1,
            "keyboard_q2": keyboard_q2,
            "mouse_q1": mouse_q1,
            "mouse_q2": mouse_q2,
            "environment_q1": environment_q1,
            "environment_q2": environment_q2,
            "image": request.form.get("image"),
            "created_by": session["user"],
            "created_date": (dt_string),
            "dsp_created_date": (dt_string)
        }
        mongo.db.checks.insert_one(check)
        flash("Assessment Successfully Added")
        return redirect(url_for("get_checks"))
        
    managers = mongo.db.managers.find().sort("manager_name", 1)
    departments = mongo.db.departments.find().sort("dept_name", 1)
    return render_template("add_check.html", managers=managers, departments=departments, form=form)

@app.route("/edit_check/<check_id>", methods=["GET", "POST"])
def edit_check(check_id):
    if request.method == "POST":
        screen_q1 = True if request.form.get("screen_q1") else False
        screen_q2 = True if request.form.get("screen_q2") else False
        chair_q1 = True if request.form.get("chair_q1") else False
        chair_q2 = True if request.form.get("chair_q2") else False
        keyboard_q1 = True if request.form.get("keyboard_q1") else False
        keyboard_q2 = True if request.form.get("keyboard_q2") else False
        mouse_q1 = True if request.form.get("mouse_q1") else False
        mouse_q2 = True if request.form.get("mouse_q2") else False
        environment_q1 = True if request.form.get("environment_q1") else False
        environment_q2 = True if request.form.get("environment_q2") else False
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        submit = {
            "manager_name": request.form.get("manager_name"),
            "dept_name": request.form.get("dept_name"),
            "max_total_time": request.form.get("max_total_time"),
            "max_continuous_time": request.form.get("max_continuous_time"),
            "created_date": request.form.get("created_date"),
            "dsp_created_date": request.form.get("created_date"),
            "screen_q1": screen_q1,
            "screen_q2": screen_q2,
            "chair_q1": chair_q1,
            "chair_q2": chair_q2,
            "keyboard_q1": keyboard_q1,
            "keyboard_q2": keyboard_q2,
            "mouse_q1": mouse_q1,
            "mouse_q2": mouse_q2,
            "environment_q1": environment_q1,
            "environment_q2": environment_q2,
            "image": request.form.get("workstation_image"),
            "created_by": session["user"],
            "updated_date": (dt_string)
        }
        mongo.db.checks.update({"_id": ObjectId(check_id)}, submit)
        flash("Assessment Successfully Updated")
        return redirect(url_for("get_checks"))

    check = mongo.db.checks.find_one({"_id": ObjectId(check_id)})
    managers = mongo.db.managers.find().sort("manager_name", 1)
    departments = mongo.db.departments.find().sort("dept_name", 1)
    return render_template("edit_check.html", check=check, managers=managers, departments=departments)


@app.route("/delete_check/<check_id>")
def delete_check(check_id):
    mongo.db.checks.remove({"_id": ObjectId(check_id)})
    flash("Assessment Successfully Deleted")
    return redirect(url_for("get_checks"))


@app.route("/get_managers")
def get_managers():
    managers = list(mongo.db.managers.find().sort("manager_name", 1))
    return render_template("managers.html", managers=managers)


@app.route("/get_departments")
def get_departments():
    departments = list(mongo.db.departments.find().sort("dept_name", 1))
    return render_template("departments.html", departments=departments)


@app.route("/get_users")
def get_users():
    users = mongo.db.users.find()
    return render_template("users.html", users=users)

@app.route("/add_manager", methods=["GET", "POST"])
def add_manager():
    if request.method == "POST":
        manager = {
            "manager_name": request.form.get("manager_name")
        }
        mongo.db.managers.insert_one(manager)
        flash("New Manager Added")
        return redirect(url_for("get_managers"))

    return render_template("add_manager.html")


@app.route("/add_department", methods=["GET", "POST"])
def add_department():
    if request.method == "POST":
        department = {
            "dept_name": request.form.get("dept_name")
        }
        mongo.db.departments.insert_one(department)
        flash("New Department Added")
        return redirect(url_for("get_departments"))

    return render_template("add_department.html")


@app.route("/edit_manager/<manager_id>", methods=["GET", "POST"])
def edit_manager(manager_id):
    if request.method == "POST":
        submit = {
            "manager_name": request.form.get("manager_name")
        }
        mongo.db.managers.update({"_id": ObjectId(manager_id)}, submit)
        flash("Manager Successfully Updated")
        return redirect(url_for("get_managers"))

    manager = mongo.db.managers.find_one({"_id": ObjectId(manager_id)})
    return render_template("edit_manager.html", manager=manager)


@app.route("/edit_department/<department_id>", methods=["GET", "POST"])
def edit_department(department_id):
    if request.method == "POST":
        submit = {
            "dept_name": request.form.get("dept_name")
        }
        mongo.db.departments.update({"_id": ObjectId(department_id)}, submit)
        flash("Department Successfully Updated")
        return redirect(url_for("get_departments"))

    department = mongo.db.departments.find_one({"_id": ObjectId(department_id)})
    return render_template("edit_department.html", department=department)


@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if request.method == "POST":
        is_admin = True if request.form.get("is_admin") else False
        submit = {
            "username": request.form.get("username"),
            "fname": request.form.get("fname"),
            "password": request.form.get("password"),
            "is_admin": is_admin
        }
        mongo.db.users.update({"_id": ObjectId(user_id)}, submit)
        flash("User Successfully Updated")
        return redirect(url_for("get_users"))

    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("edit_user.html", user=user)

@app.route("/change_password/<user_id>", methods=["GET", "POST"])
def change_password(user_id):
    form = ChangePassForm()
    if request.method == "POST" and form.validate():
        is_admin = True if request.form.get("is_admin") else False
        submit = {
            "username": request.form.get("username"),
            "fname": request.form.get("fname"),
            "password": generate_password_hash(request.form.get("password")),
            "is_admin": is_admin
        }
        mongo.db.users.update({"_id": ObjectId(user_id)}, submit)
        flash("Password Successfully Updated")
        return redirect(url_for("profile", username=session["user"]))

    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("change_password.html", user=user, form=form)


@app.route("/delete_manager/<manager_id>")
def delete_manager(manager_id):
    mongo.db.managers.remove({"_id": ObjectId(manager_id)})
    flash("Manager Successfully Deleted")
    return redirect(url_for("get_managers"))

@app.route("/delete_department/<department_id>")
def delete_department(department_id):
    mongo.db.departments.remove({"_id": ObjectId(department_id)})
    flash("Department Successfully Deleted")
    return redirect(url_for("get_departments"))


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("User Successfully Deleted")
    return redirect(url_for("get_users"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)