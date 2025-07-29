# tracker.py
from datetime import datetime
import matplotlib.pyplot as plt

def add_exam(data):
    subject = input("Enter subject name: ").strip()
    if not subject:
        print("❌ Subject name cannot be empty.")
        return
    date = input("Enter exam date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format! Use YYYY-MM-DD.")
        return

    if subject not in data:
        data[subject] = {
            "exam_date": date,
            "topics": {}
        }
        print(f"✅ Exam for {subject} added.")
    else:
        print("⚠️ Subject already exists.")

def add_study_topic(data):
    subject = input("Enter subject name: ").strip()
    if subject in data:
        topic = input("Enter topic name: ").strip()
        if not topic:
            print("❌ Topic name cannot be empty.")
            return
        data[subject]["topics"][topic] = "pending"
        print(f"✅ Topic '{topic}' added to {subject}.")
    else:
        print("❌ Subject not found.")

def mark_topic_complete(data):
    subject = input("Enter subject name: ").strip()
    if subject in data:
        topic = input("Enter topic name to mark complete: ").strip()
        if topic in data[subject]["topics"]:
            data[subject]["topics"][topic] = "completed"
            print(f"✅ Marked '{topic}' as completed in {subject}.")
        else:
            print("❌ Topic not found.")
    else:
        print("❌ Subject not found.")

def view_progress(data):
    for subject, details in data.items():
        topics = details["topics"]
        total = len(topics)
        completed = sum(1 for status in topics.values() if status == "completed")
        pending = total - completed

        print(f"\n📚 Subject: {subject}")
        print(f"📄 Total Topics: {total}")
        print(f"✅ Completed: {completed}")
        print(f"⏳ Pending: {pending}")

        if total > 0:
            percent = (completed / total) * 100
            print(f"📊 Progress: {percent:.2f}%")
            plot_progress(completed, pending, subject)

def plot_progress(completed, pending, subject):
    labels = ['Completed', 'Pending']
    sizes = [completed, pending]
    colors = ['green', 'red']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title(f"Progress for {subject}")
    plt.axis('equal')
    plt.show()