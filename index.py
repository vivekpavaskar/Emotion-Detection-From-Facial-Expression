from flask import Flask
from flask_mysqldb import MySQL
from main import startProject

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'shhp'
mysql = MySQL(app)


@app.route('/')
def index():
    conn = mysql.connection
    cur = conn.cursor()
    sql = "SELECT * FROM `complaints` WHERE status='Applied' limit 1"
    cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        return "ALL COMPLAINTS PROCESSED"
    result = result[0]
    data = {}
    data["id"] = str(result[0])
    data["statement"] = result[9]
    data["video"] = result[10]
    data["status"] = result[11]
    decision = startProject(data)

    # cur = mysql.connection.cursor()
    # sql = '''UPDATE `complaints` SET `status` = %s WHERE `complaints`.`id` = %s'''
    # sqlv = (decision, data["id"])
    # cur.execute(sql, sqlv)
    # conn.commit()
    return str(data)


if __name__ == '__main__':
    app.run(debug=True)
