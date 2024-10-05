import phonenumbers
from phonenumbers import geocoder

def get_phone_info(phone_number):
    try:
        # تحليل الرقم
        number = phonenumbers.parse(phone_number)

        # الحصول على موقع الرقم
        location = geocoder.description_for_number(number, "en")

        return location if location else "موقع غير معروف"
    except phonenumbers.NumberParseException:
        return "رقم هاتف غير صالح"

# اختبار الدالة
print(get_phone_info("+967777123456"))  # قد يظهر "Yemen"
print(get_phone_info("+966551234567"))   # قد يظهر "Saudi Arabia"