import mysql.connector

# الاتصال بقاعدة البيانات
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # أدخل كلمة مرور الجذر إذا كانت موجودة
    database="mydatabase",
    charset='utf8mb4'  # تعيين charset إلى utf8mb4
)

cursor = conn.cursor()

# إدخال البيانات
name = input("أدخل الاسم: ")
email = input("أدخل البريد الإلكتروني: ")

# إضافة البيانات إلى الجدول
sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
val = (name, email)

cursor.execute(sql, val)

# حفظ التغييرات
conn.commit()

print(cursor.rowcount, "سجل(سجلات) مضاف(ة)")

# إغلاق الاتصال
cursor.close()
conn.close()