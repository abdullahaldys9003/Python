import tkinter as tk

# إنشاء نافذة جديدة
window = tk.Tk()
window.title("نافذة بسيطة")

# تعيين حجم النافذة
window.geometry("300x200")

# إنشاء دالة بسيطة يتم استدعاؤها عند الضغط على الزر
def on_button_click():
    label.config(text="تم الضغط على الزر!")

# إنشاء زر
button = tk.Button(window, text="اضغط هنا", command=on_button_click)
button.pack(pady=20)  # وضع الزر في النافذة مع بعض المسافة العمودية

# إنشاء تسمية لعرض النص
label = tk.Label(window, text="")
label.pack()

# بدء تشغيل الحلقة الرئيسية
window.mainloop()