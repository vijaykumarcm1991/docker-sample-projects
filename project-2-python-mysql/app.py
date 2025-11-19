import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="demo"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test(id INT PRIMARY KEY AUTO_INCREMENT, msg VARCHAR(255))")
    cursor.execute("INSERT INTO test(msg) VALUES('Hello from MySQL')")
    conn.commit()
    cursor.execute("SELECT * FROM test")
    data = cursor.fetchall()
    return {"data": data}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)