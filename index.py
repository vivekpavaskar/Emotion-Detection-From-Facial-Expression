from flask import Flask
import main

# from flask_mysqldb import MySQL
app = Flask(__name__)
'''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Shop'
mysql = MySQL(app)
'''


@app.route('/')
def index():
    # cur = mysql.connection.cursor()
    # cur.execute('''SELECT * FROM `login` WHERE 1''')
    # rv = cur.fetchall()
    # return str(rv)
    status = main.startProject()
    return status


if __name__ == '__main__':
    app.run(debug=True)
