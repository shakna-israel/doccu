try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import os
import json
import requests

class DoccuTitle(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack({"side":"top"})
        self.createWidgets()

    def createWidgets(self):
        self.doccu_label = Label(self)
        self.doccu_label['text'] = "Doccu"
        self.doccu_label2 = Label(self)
        self.doccu_label2['text'] = "Your Friendly Documentation Engine"
        self.doccu_label.pack()
        self.doccu_label2.pack()

class UserForms(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack({"side":"left"})
        self.home_label = Label(self)
        self.home_label['text'] = "Users"
        self.home_label.pack({"side":"top"})
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
                        if not check_keys.values():
                            create_user(username, useremail, usergroup, userkey)
                            popup("User Succesfully Added")
                        else:
                            for user in check_keys.values():
                                if userkey != user['key']:
                                    create_user(username, useremail, usergroup, userkey)
                                    popup("User Succesfully Added")

    def remove_user(self):
        username = self.username_entry_contents.get().lower()
        check_keys = json.load(open(os.path.expanduser('~/.doccu/ids.dbs'),'r'))
        try:
            del check_keys[username]
            json.dump(check_keys,open(os.path.expanduser('~/.doccu/ids.dbs'),"w+"), sort_keys=True, indent=4, separators=(',', ': '))
            popup("User Succesfully Deleted")
        except KeyError:
            popup("Sorry, that user does not exist!")
        

class ListUsers(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.title_label = Label(self)
        self.title_label['text'] = "Current Users"
        self.title_label.pack({"side":"top"})
        self.pack({"side":"left"})
        self.createWidgets()

    def createWidgets(self):
        self.username_refresh_button = Button(self)
        self.username_refresh_button["text"] = "Refresh Users",
        self.username_refresh_button["command"] = self.refresh_user_list
        self.username_refresh_button.pack({"side":"bottom"})

    def refresh_user_list(self):
        try:
            self.label.destroy()
        except AttributeError:
            pass
        users = json.load(open(os.path.expanduser('~/.doccu/ids.dbs'),'r'))
        self.label = Label(self)
        label_text = ""
        for user in users:
            label_text = label_text + "\n" + str(user)
        self.label["text"] = label_text
        self.label.pack()

class UpdateResources(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.title_label = Label(self)
        self.title_label['text'] = "Update Resources"
        self.title_label.pack({"side":"top"})
        self.pack({"side":"left"},fill='x', expand=1)
        self.createWidgets()

    def createWidgets(self):
        self.button = Button(self)
        self.button["text"] = "Update Resources",
        self.button["command"] = self.update_resources
        self.button.pack({"side":"bottom"})

    def update_resources(self):
        # Download the server
        download_file("https://raw.githubusercontent.com/shakna-israel/doccu-server/master/doccu_server.py",os.path.expanduser("~/.doccu/doccu_server.py"))
        # Download the js stuff
        download_file('https://raw.githubusercontent.com/bpampuch/pdfmake/master/build/pdfmake.min.js', os.path.expanduser('~/.doccu/static/js/pdfmake.min.js'))
        download_file('https://raw.githubusercontent.com/bpampuch/pdfmake/master/build/vfs_fonts.js', os.path.expanduser('~/.doccu/static/js/vfs_fonts.js'))
        popup("Files downloaded!")

class RunServer(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.title_label = Label(self)
        self.title_label['text'] = "Launch Server"
        self.title_label.pack({"side":"top"})
        self.pack({"side":"left"},fill='x', expand=1)
        self.createWidgets()

    def createWidgets(self):
        self.button = Button(self)
        self.button["text"] = "Launch Server",
        self.button["command"] = self.launch_server
        self.button.pack({"side":"bottom"})

    def launch_server(self):
        popup()

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

def popup(stringText="Not Yet Implemented"):
    toplevel = Toplevel()
    label1 = Label(toplevel, text=str(stringText), height=0, width=50)
    label1.pack()
    closewindow = Button(toplevel)
    closewindow["text"] = "Ok",
    closewindow["command"] = toplevel.destroy 
    closewindow.pack()

def download_file(url, fileName):
    """A procedural download, to allow for interruptions and large file sizes."""
    url_request = requests.get(url, stream=True)
    with open(fileName,'wb') as fileOpen:
        for chunk in url_request.iter_content(chunk_size=1024):
            if chunk:
                fileOpen.write(chunk)
                fileOpen.flush()

def main():
    root = Tk()
    root.wm_title("Doccu Management Console")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    doccuPretty = DoccuTitle(master=root)
    userForms = UserForms(master=root)
    userList = ListUsers(master=root)
    updateResources = UpdateResources(master=root)
    runServer = RunServer(master=root)
    doccuPretty.mainloop()
    UserForms.mainloop()
    userList.mainloop()
    updateResources.mainloop()
    runServer.mainloop()
    root.destroy()

if __name__ == '__main__':
    main()