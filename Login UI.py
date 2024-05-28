from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("APPLIED SUCCESSFULLY")

Label(root, text="REGISTRATION FORM", font="arial 15 bold").grid(row=0, column=5)

name=Label(root,text="NAME").grid(row=1,column=2)
age=Label(root,text="AGE").grid(row=2,column=2)
gender=Label(root,text="GENDER").grid(row=3,column=2)
number=Label(root,text="NUMBER").grid(row=4,column=2)

name_value=StringVar
age_value=StringVar
gender_value=StringVar
number_value=StringVar
check_value=IntVar

name_entry=Entry(root, textvariable=name_value).grid(row=1,column=3)
age_entry=Entry(root, textvariable=age_value).grid(row=2,column=3)
gender_entry=Entry(root, textvariable=gender_value).grid(row=3,column=3)
number_entry=Entry(root, textvariable=number_value).grid(row=4,column=3)

check_btn=Checkbutton(text="remember me?", variable=check_value).grid(row=6,column=3)

Button(text="SUBMIT", command=getvals).grid(row=7, column=3)

root.mainloop()