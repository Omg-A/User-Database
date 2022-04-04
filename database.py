from tkinter import *

root = Tk()
root.title("User Database")
root.geometry("500x500")
root.configure(background="SteelBlue1")

label_username = Label(root, text="Username:", bg="SteelBlue1")
label_username.place(relx=0.3, rely=0.2, anchor=CENTER)

input_username = Entry(root)
input_username.place(relx=0.5, rely=0.2, anchor=CENTER)

label_email = Label(root, text="Email:", bg="SteelBlue1")
label_email.place(relx=0.3, rely=0.3, anchor=CENTER)

input_email = Entry(root)
input_email.place(relx=0.5, rely=0.3, anchor=CENTER)

label = Label(root, bg="SteelBlue1")

dictionary = {}
class Users:
    def addUser(key, value): 
         global dictionary
         dictionary[key]=value
         label["text"] = str(dictionary)

class GetUsers(Users):    
    def getUser(self):
        username = input_username.get()
        email = input_email.get()
        Users.addUser(username, email)

user = GetUsers()
btn = Button(root, text="Add user details", command=user.getUser, bg="gold")
btn.place(relx=0.5,rely=0.4, anchor=CENTER)
label.place(relx=0.5,rely=0.5, anchor=CENTER)
root.mainloop()