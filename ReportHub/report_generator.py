import json

# قائمة لتخزين الكائنات
reports = []

# إنشاء 50 كائن ببيانات باللغة العربية
for i in range(1, 51):
    report = {
        "id": i,
        "department_name": "سرقة",
        "reporter_name": f"مراسل {i}",
        "reported_person_name": f"الشخص المبلغ عنه {i}",
        "report_number": f"{2800 + i}-2132",
        "report_type": "سرقة",
        "report_status": "مغلق" if i % 2 == 0 else "مفتوح",
        "report_description": f"هذا هو وصف البلاغ رقم {i}، يشمل جميع التفاصيل المطلوبة.",
        "report_date": "2024-11-24",
        "report_time": "12:34:56",
        "location": f"مدينة {i}، اليمن",
        "reported_person_number": f"+967-7606404{i:02}",
        "report_category": "عادي" if i % 2 == 0 else "طارئ",
        "reporter_address": f"العنوان {i}، المدينة {i}",
        "reporter_phone_number": f"+967 7890741{i:02}",
        "reporter_date": "1988-03-04"
    }
    reports.append(report)

# كتابة الكائنات في ملف JSON
with open("reports.json", "w", encoding="utf-8") as file:
    json.dump(reports, file, ensure_ascii=False, indent=4)
    
print("تم إنشاء الملف reports.json بنجاح!")