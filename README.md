โปรแกรมคำนวนค่าใช้จ่ายโดยใช้ภาษา Python 
Expense_Recorder/
│── main.py               # ไฟล์หลัก แสดงผล GUI และจัดการ event
│── database.py           # จัดการ SQLite (เชื่อมต่อ ดึง เพิ่ม ลบ แก้ไขข้อมูล)
│── ui_components.py      # สร้างและจัดการ widgets ใน หน้าต่าง Main GUI ด้วย tkinter
│── controller.py         # จัดการการเชื่อมโยงระหว่าง GUI และ database
│── add_expense.py        # สร้างและจัดการ widgets และ command ต่างๆในหน้าต่าง add
└── update_exense.py      # สร้างและจัดการ widgets และ command ต่างๆในหน้าต่าง edit
