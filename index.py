from flask import Flask
from flask_mysqldb import MySQL

# import main

# from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'shhp'
mysql = MySQL(app)


@app.route('/')
def index():
    decision=True
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM `complaints` WHERE status='Applied' ''')
    result = cur.fetchall()
    result=result[0]
    data={}
    data["id"]=result[0]
    data["statement"]=result[9]
    data["video"]=result[10]
    data["status"]=result[11]
    # decision = main.startProject(data)
    # if decision :
    #     cur.execute(''' ''')
    # else:
    #     cur.execute(''' ''')

    return str(data)


if __name__ == '__main__':
    app.run(debug=True)
