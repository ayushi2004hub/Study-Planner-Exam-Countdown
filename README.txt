=====================================================
Study Planner with Exam Countdown - Python Project
=====================================================

📌 Author: Ayushi Anil Wankhade  
📚 Course: B.Tech (Artificial Intelligence & Data Science)  
🗓️ Academic Year: 2024–2025  
👨‍🏫 Guide: [Your Faculty Name]  

-----------------------------------------------------
1. 🔍 Project Description
-----------------------------------------------------
This is a Python-based command-line application that allows students to:

- Add subjects and their exam dates
- Add study topics under each subject
- Mark topics as completed
- Track exam countdown (days left)
- View overall progress in percentage
- Visualize progress using a pie chart

It helps students stay organized and plan their studies more effectively.

-----------------------------------------------------
2. 🛠️ Technologies and Tools Used
-----------------------------------------------------
- Python 3.x
- JSON (for data storage)
- datetime (for countdown logic)
- matplotlib (for visualizing progress)
- File handling (read/write planner data)
- Functions, loops, conditions, and error handling

-----------------------------------------------------
3. 📂 Project Structure
-----------------------------------------------------
study_planner_project/
│
├── main.py                # Main program and menu
├── tracker.py             # Functions to add/edit study data
├── countdown.py           # Countdown logic
├── planner_data.json      # File to store study plans
└── README.txt             # Project summary and usage guide

-----------------------------------------------------
4. 🚀 How to Run the Project
-----------------------------------------------------
1. Open terminal or VS Code
2. Navigate to project folder
3. Run the command:

   python main.py

4. Follow the on-screen menu to:
   - Add exams
   - Add topics
   - Mark topics complete
   - View exam countdown
   - View progress report

-----------------------------------------------------
5. 📈 Example Menu (on running main.py)
-----------------------------------------------------
------ Study Planner ------
1. Add new exam
2. Add study topic
3. Mark topic as complete
4. View exam countdown
5. View progress report
6. Exit

-----------------------------------------------------
6. 📝 Sample JSON Data Format
-----------------------------------------------------
{
  "Math": {
    "exam_date": "2025-07-20",
    "topics": {
      "Algebra": "completed",
      "Geometry": "pending"
    }
  }
}

-----------------------------------------------------
7. 📌 Project Status
-----------------------------------------------------
✅ All core features implemented  
✅ Tested with multiple subjects and topics  
✅ File-based data persistence  
✅ Pie chart visual added using matplotlib

-----------------------------------------------------
8. 🚀 Future Scope
-----------------------------------------------------
- GUI using tkinter
- Email and reminder alerts
- Daily study timers
- PDF report generation

-----------------------------------------------------
9. 📧 Contact
-----------------------------------------------------
Ayushi Anil Wankhade  
[Your Email]  
[Your College Name]
