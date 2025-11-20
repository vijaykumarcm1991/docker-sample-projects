import time
import mysql.connector
from mysql.connector import Error
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    while True:
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="demo"
            )
            print("MySQL Connected!")
            return conn
        except Error as e:
            print("MySQL not ready. Retrying in 3 seconds...")
            time.sleep(3)

@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test(id INT PRIMARY KEY AUTO_INCREMENT, msg VARCHAR(255))")
    cursor.execute("INSERT INTO test(msg) VALUES('Hello from MySQL')")
    conn.commit()
    cursor.execute("SELECT * FROM test")
    data = cursor.fetchall()
    return {"data": data}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)