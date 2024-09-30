from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass
from android.permissions import request_permissions, Permission

# استخدام Pyjnius للوصول إلى Android API
Environment = autoclass('android.os.Environment')
File = autoclass('java.io.File')

# طلب الأذونات للوصول إلى الملفات
def request_android_permissions():
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

# دالة لعرض محتويات مجلد الصور
def show_user_images():
    # الحصول على مسار مجلد DCIM (الذي يحتوي على الصور في الغالب)
    pictures_directory = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM).getAbsolutePath()
    
    # قراءة الملفات الموجودة في المجلد
    file = File(pictures_directory)
    files_list = file.listFiles()

    if files_list:
        for f in files_list:
            print(f.getName())  # طباعة أسماء الملفات

# تطبيق Kivy الأساسي
class FileBrowserApp(App):
    def build(self):
        # زر يطلب الأذونات ويعرض الملفات عند الضغط
        btn = Button(text="عرض ملفات الصور")
        btn.bind(on_press=lambda x: (request_android_permissions(), show_user_images()))
        return btn

# تشغيل التطبيق
if __name__ == "__main__":
    FileBrowserApp().run()
