# countdown.py
from datetime import datetime

def countdown_days(data, subject):
    if subject in data:
        try:
            exam_date_str = data[subject]["exam_date"]
            exam_date = datetime.strptime(exam_date_str, "%Y-%m-%d").date()
            today = datetime.today().date()
            remaining_days = (exam_date - today).days

            if remaining_days >= 0:
                print(f"📆 {remaining_days} day(s) left until the {subject} exam.")
            else:
                print(f"📅 The exam date for {subject} has already passed.")
        except Exception as e:
            print("⚠️ Error in date format or countdown calculation:", e)
    else:
        print("❌ Subject not found.")