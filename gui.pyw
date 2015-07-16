try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import os
import json

class UserForms(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.createUserButton()
        self.deleteUserButton()
        self.addUserNameForm()
        self.addUserGroupForm()
        self.addUserEmailForm()
        self.addUserKeyForm()

    def createUserButton(self):
        self.username_button = Button(self)
        self.username_button["text"] = "Create User",
        self.username_button["command"] = self.generate_user

        self.username_button.pack({"side": "bottom"})

    def deleteUserButton(self):
        self.username_del_button = Button(self)
        self.username_del_button["text"] = "Delete User",
        self.username_del_button["command"] = self.remove_user

        self.username_del_button.pack({"side": "bottom"})

    def addUserNameForm(self):

        self.username_label = Label(self)
        self.username_label['text'] = "User Name"

        self.username_entry = Entry(self)
        self.username_entry_contents = StringVar()
        self.username_entry_contents.set("Andrew Conan")
        self.username_entry['textvariable'] = self.username_entry_contents

        self.username_label.pack()
        self.username_entry.pack()

    def addUserGroupForm(self):
        self.username_group_entry = Entry(self)
        self.username_group_entry_contents = StringVar()
        self.username_group_entry_contents.set("Superadmin")
        self.username_group_entry['textvariable'] = self.username_group_entry_contents

        self.username_group_label = Label(self)
        self.username_group_label['text'] = "User Group"
        self.username_group_label2 = Label(self)
        self.username_group_label2['text'] = "(superadmin, admin, editor)"

        self.username_group_label.pack()
        self.username_group_label2.pack()
        self.username_group_entry.pack()

    def addUserEmailForm(self):
        self.username_email_entry = Entry(self)
        self.username_email_entry_contents = StringVar()
        self.username_email_entry_contents.set("example@example.com")
        self.username_email_entry['textvariable'] = self.username_email_entry_contents

        self.username_email_label = Label(self)
        self.username_email_label['text'] = "Email Address"

        self.username_email_label.pack()
        self.username_email_entry.pack()

    def addUserKeyForm(self):
        self.username_key_entry = Entry(self)
        self.username_key_entry_contents = StringVar()
        self.username_key_entry_contents.set("0000")
        self.username_key_entry['textvariable'] = self.username_key_entry_contents

        self.username_key_label = Label(self)
        self.username_key_label['text'] = "Authorisation Key"

        self.username_key_label.pack()
        self.username_key_entry.pack()

    def generate_user(self):
        username = self.username_entry_contents.get().lower()
        usergroup = self.username_group_entry_contents.get().lower()
        useremail = self.username_email_entry_contents.get().lower()
        userkey = self.username_key_entry_contents.get().lower()
        check_keys = json.load(open(os.path.expanduser('~/.doccu/ids.dbs'),'r'))
        for user in check_keys.values():
            if userkey == user['key']:
                toplevel = Toplevel()
                label1 = Label(toplevel, text="Please enter a different authorisation key.", height=0, width=50)
                label1.pack()
                closewindow = Button(toplevel)
                closewindow["text"] = "Ok",
                closewindow["command"] = toplevel.destroy 
                closewindow.pack()
        for user in check_keys:
            if username == user:
                toplevel = Toplevel()
                label1 = Label(toplevel, text="Please enter a different user name.", height=0, width=50)
                label1.pack()
                closewindow = Button(toplevel)
                closewindow["text"] = "Ok",
                closewindow["command"] = toplevel.destroy 
                closewindow.pack()
        if username == 'andrew conan':
            toplevel = Toplevel()
            label1 = Label(toplevel, text="Please enter a real user name.", height=0, width=50)
            label1.pack()
            closewindow = Button(toplevel)
            closewindow["text"] = "Ok",
            closewindow["command"] = toplevel.destroy 
            closewindow.pack()
        if useremail == 'example@example.com':
            toplevel = Toplevel()
            label1 = Label(toplevel, text="Please enter a real email address.", height=0, width=50)
            label1.pack()
            closewindow = Button(toplevel)
            closewindow["text"] = "Ok",
            closewindow["command"] = toplevel.destroy 
            closewindow.pack()
        if '@' not in useremail:
            toplevel = Toplevel()
            label1 = Label(toplevel, text="Please enter a valid email address.", height=0, width=50)
            label1.pack()
            closewindow = Button(toplevel)
            closewindow["text"] = "Ok",
            closewindow["command"] = toplevel.destroy 
            closewindow.pack()
        if '.' not in useremail:
            toplevel = Toplevel()
            label1 = Label(toplevel, text="Please enter a valid email address.", height=0, width=50)
            label1.pack()
            closewindow = Button(toplevel)
            closewindow["text"] = "Ok",
            closewindow["command"] = toplevel.destroy 
            closewindow.pack()
        if userkey == '0000':
            toplevel = Toplevel()
            label1 = Label(toplevel, text="Please enter a valid authorisation key.", height=0, width=50)
            label1.pack()
            closewindow = Button(toplevel)
            closewindow["text"] = "Ok",
            closewindow["command"] = toplevel.destroy 
            closewindow.pack()
        if username != 'andrew conan':
            if useremail != 'example@example.com':
                if '@' in useremail:
                    if '.' in useremail:
                        if username not in check_keys:
                            for user in check_keys.values():
                                if userkey != user['key']:
                                    if create_user(username, useremail, usergroup, userkey) == 'True':
                                        toplevel = Toplevel()
                                        label1 = Label(toplevel, text="User Added Succesfully.", height=0, width=50)
                                        label1.pack()
                                        closewindow = Button(toplevel)
                                        closewindow["text"] = "Ok",
                                        closewindow["command"] = toplevel.destroy 
                                        closewindow.pack()

    def remove_user(self):
        toplevel = Toplevel()
        label1 = Label(toplevel, text="Not Yet Implemented.", height=0, width=50)
        label1.pack()
        closewindow = Button(toplevel)
        closewindow["text"] = "Ok",
        closewindow["command"] = toplevel.destroy 
        closewindow.pack()

class UpdateResources(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        print("Not Yet Implemented")

def create_user(username, useremail, usergroup, userkey):
    userdict = {}
    userdict[username] = {}
    userdict[username]['group'] = usergroup
    userdict[username]['key'] = userkey
    userdict[username]['email'] = useremail
    currentFile = json.load(open(os.path.expanduser('~/.doccu/ids.dbs'),'r'))
    outDict = userdict.copy()
    outDict.update(currentFile)
    json.dump(outDict,open(os.path.expanduser('~/.doccu/ids.dbs'),"w+"), sort_keys=True, indent=4, separators=(',', ': '))
    return True


def main():
    root = Tk()
    root.wm_title("Doccu Management Console")
    app = UserForms(master=root)
    app.mainloop()
    root.destroy()

if __name__ == '__main__':
    main()