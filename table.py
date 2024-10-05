import sqlite3

# إنشاء اتصال بقاعدة البيانات (إذا لم يكن الملف موجودًا، سيتم إنشاؤه)
conn = sqlite3.connect('mydatabase.db')  # اسم الملف هو mydatabase.db

# إنشاء كائن المؤشر
cursor = conn.cursor()

# إنشاء جدول جديد
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# إدخال البيانات
name = input("أدخل الاسم: ")
email = input("أدخل البريد الإلكتروني: ")

# إضافة البيانات إلى الجدول
cursor.execute('''
INSERT INTO users (name, email)
VALUES (?, ?)
''', (name, email))

# حفظ التغييرات
conn.commit()

print("تم إضافة البيانات بنجاح!")

# إغلاق الاتصال
cursor.close()
conn.close()