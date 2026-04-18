from flask import Flask, request
from psycopg2 import connect, OperationalError

app=Flask(__name__)
def save_reader(cur, name,email):
    sql="INSERT INTO Readers(name,email) VALUES(%s,%s)"
    values=(name,email)
    cur.execute(sql,values)


FORM="""<form action="" method="POST">
            <label for="name">First Name of readers</label></br>
            <input type="text" name="name" id="name"></br>
            <label for="email">Email of readers</label></br>
            <input type="text" name="email" id="email"></br>
            <button type="submit value="Submit">Submit</button>
         </form>
"""
@app.route("/add_readers", methods=("GET","POST"))
def add_reader_view():
    if request.method=="GET":
        return FORM
    else:
        name=request.form.get("name")
        email=request.form.get("email")
        try:
            if name and email:
                if "@" in email:
                    connection=connect(dbname="exam2_db", user="postgres", password="coderslab", host="localhost", port="5432")
                    connection.autocommit=True
                    cursor=connection.cursor()
                    save_reader(cursor, name, email)
                    connection.close()
                    return "Dodat citalac"
        except OperationalError as e:
            print("Error",e)

if __name__=='__main__':
    app.run()


