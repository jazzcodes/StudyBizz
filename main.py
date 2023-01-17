from flask import *
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html");


@app.route("/add_student")
def add_student():
    return render_template("add_student.html")


@app.route("/saverecord", methods=["POST", "GET"])
def saveRecord():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            father_name = request.form["father_name"]
            mother_name = request.form["mother_name"]
            age = request.form["age"]
            address = request.form["address"]
            reg_date = request.form["reg_date"]

            with sqlite3.connect("student_details.db") as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT into Student_Info (name, father_name, mother_name, age, address, reg_date) values (?,?,?,?,?,?)",
                    (name, father_name, mother_name, age, address, reg_date))
                connection.commit()
                msg = "Student details successfully Added"
        except:
            connection.rollback()
            msg = "We can not add Student details to the database"
        finally:
            return render_template("success_record.html", msg=msg)
            connection.close()


@app.route("/delete_student")
def delete_student():
    return render_template("delete_student.html")


@app.route("/student_info")
def student_info():
    connection = sqlite3.connect("student_details.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("select * from Student_Info")
    rows = cursor.fetchall()
    return render_template("student_info.html", rows=rows)

@app.route("/student_filter")
def student_filter():

    return render_template("filter.html")

@app.route("/filter_reg_date")
def filter_by_reg_date():

    return render_template("filter_reg_date.html")

@app.route("/filter_name")
def filter_by_name():

    return render_template("filter_name.html")

@app.route("/filter_city")
def filter_by_city():

    return render_template("filter_city.html")

@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("student_details.db") as connection:

        cursor = connection.cursor()
        cursor.execute("select * from Student_Info where id=?", (id))
        rows = cursor.fetchall()
        if not rows == []:

            cursor.execute("delete from Student_Info where id = ?", (id,))
            msg = "Student detail successfully deleted"
            return render_template("delete_record.html", msg=msg)

        else:
            msg = "can't be deleted"
            return render_template("delete_record.html", msg=msg)

@app.route("/filter-student-reg-date", methods=["POST"])
def filterRegDate():
    reg_date = request.form["reg_date"]

    with sqlite3.connect("student_details.db") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("select * from Student_Info where reg_date=?", (reg_date,))
        rows = cursor.fetchall()
        if not rows == []:

            return render_template("filter@regdate.html", rows=rows)

        else:
            msg = "No data found"
            return render_template("filter@regdate.html", msg=msg)

@app.route("/filter-student-name", methods=["POST"])
def filterName():
    name = request.form["name"]
    with sqlite3.connect("student_details.db") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("select * from Student_Info where name=?", [name])
        rows = cursor.fetchall()
        if not rows == []:

            return render_template("filter@name.html", rows=rows)

        else:
            msg = "No data found"
            return render_template("filter@name.html", msg=msg)

@app.route("/filter-student-city", methods=["POST"])
def filterCity():
    address = request.form["address"]
    with sqlite3.connect("student_details.db") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("select * from Student_Info where address=?", [address])
        rows = cursor.fetchall()
        if not rows == []:

            return render_template("filter@city.html", rows=rows)

        else:
            msg = "No data found"
            return render_template("filter@city.html", msg=msg)


if __name__ == "__main__":
    app.run(debug=True)
