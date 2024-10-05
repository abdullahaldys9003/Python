import sqlite3

# إنشاء اتصال بقاعدة البيانات
conn = sqlite3.connect('mydatabase.db')

# إنشاء كائن المؤشر
cursor = conn.cursor()

# استعلام لعرض البيانات
cursor.execute('SELECT * FROM users')

# الحصول على جميع الصفوف
rows = cursor.fetchall()

# طباعة البيانات
for row in rows:
    print(row)

# إغلاق الاتصال
cursor.close()
conn.close()