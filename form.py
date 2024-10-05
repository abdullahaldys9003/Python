from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# إنشاء اتصال بقاعدة البيانات
def init_db():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/add-user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']

    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (name, email)
    VALUES (?, ?)
    ''', (name, email))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('index'))

@app.route('/view-users')
def view_users():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()  # جلب جميع البيانات من جدول المستخدمين
    cursor.close()
    conn.close()
    return render_template('view_users.html', users=users)

if __name__ == '__main__':
    init_db()  # تأكد من إنشاء قاعدة البيانات
    app.run(debug=True)