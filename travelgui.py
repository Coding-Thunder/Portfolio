from tkinter import *

def gymdata():
    # fnamevalue, lnamevalue, timevalue, agevalue, contactvalue, gendervalue
    print(f"First-Name is {fnamevalue.get()}")
    print(f"Last-Name is {lnamevalue.get()}")
    print(f"Batch-Time They Expect To Be Given{timevalue.get()}")
    print(f"Applicant's Age is {agevalue.get()}")
    print(f"Applicant's Contact is {fnamevalue.get()}")
    print(f"Applicant's Gender is {gendervalue.get()}")

with open("gym.txt","w") as f:
    pass

root = Tk()
root.geometry("455x355")

l1 = Label(root, text = "First-Name")
l1.grid()

l2 = Label(root, text = "Last-Name")
l2.grid(row = 1, column = 0 )

l3 = Label(root, text = "Expected-Time")
l3.grid(row = 2, column = 0)

l4 = Label(root, text = "Age")
l4.grid(row = 3, column = 0)

l5 = Label(root, text = "Contact")
l5.grid(row = 4, column = 0)

l6 = Label(root, text = "Gender")
l6.grid(row = 5, column = 0)

# fnamevalue, lnamevalue, timevalue, agevalue, contactvalue, gendervalue
# Text area created Using Stringvar() Class
fnamevalue = StringVar()
lnamevalue = StringVar()
timevalue = StringVar()
agevalue = StringVar()
contactvalue =  StringVar()
gendervalue = StringVar()

# Entry Class
fnameentry = Entry(root, textvariable = fnamevalue)
lnameentry = Entry(root, textvariable = lnamevalue)
timeentry = Entry(root, textvariable = timevalue)
ageentry = Entry(root, textvariable = agevalue)
contactentry = Entry(root, textvariable = contactvalue)
genderentry = Entry(root, textvariable = gendervalue)

fnameentry.grid(row = 0, column = 1)
lnameentry.grid(row = 1, column = 1)
timeentry.grid(row = 2, column = 1)
ageentry.grid(row = 3, column = 1)
contactentry.grid(row = 4, column = 1)
genderentry.grid(row = 5, column = 1)

# Button Created Using Button() Class
Button(root, text = "Submit-Info.", command = gymdata).grid() 

root.mainloop()

