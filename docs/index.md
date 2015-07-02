# Doccu

## Documentation Engine

---

## Quickstart

First, ensure you have [Python 2.7+](https://www.python.org/downloads/) or [Python 3.1+](https://www.python.org/downloads/) installed.

Then, in the Terminal or Command Prompt, run:

```
pip install doccu
```

If you have an issue with ```command pip not found```, refer to [this documentation](http://docs.python-guide.org/en/latest/starting/install/win/#setuptools-pip).

If you have other Python applications on the same serer, you should probably use [Virtualenv](https://virtualenv.pypa.io/en/latest/).

You now have a new command you can run in any, (if you used Virtualenv, you'll still need to activate it first), Terminal or Command Prompt:

```
doccu-manage
```

After running it, you should be greeted with a screen like:

```
Enter 1 to ADD a user
2 to REMOVE a User
3 to START the server
4 to updated browser-based dependencies
5 to updateserver-based dependencies:
```

You'll need to add at least one user before you can generate documentation, so enter *1* and press enter, you should get a screen like:

```
Enter 1 to ADD a user
2 to REMOVE a User
3 to START the server
4 to updated browser-based dependencies
5 to updateserver-based dependencies:1
Enter a users UNIQUE name, e.g. Andrew Conan:
```

Enter their name, and hit enter. 

(It is *strongly* advised to **not** simply create an *Administrator* user... Who would know who they are? You don't want that ambiguous name tied into your documentation.)

Next, you'll get a screen like:

```
Enter 1 to ADD a user
2 to REMOVE a User
3 to START the server
4 to updated browser-based dependencies
5 to updateserver-based dependencies:1
Enter a users UNIQUE name, e.g. Andrew Conan: Andrew Conan
Enter a users UNIQUE code, e.g. 00226677
```

Here is the unique code you give to a user.

They use this code to authenticate documents.

This is the code you will need to give to said user, as they can't edit this themselves.

The reccomended code is an integer, about six digits long. e.g. 002255

However, Doccu should treat this as a string, so it could potentially be any password.

*Note:* No two users can have the same password. The Management Console will complain if you try to give it a non-unique code.

You'll then get a screen like:

```
Enter 1 to ADD a user
2 to REMOVE a User
3 to START the server
4 to updated browser-based dependencies
5 to updateserver-based dependencies:1
Enter a users UNIQUE name, e.g. Andrew Conan: Andrew Conan
Enter a users UNIQUE code, e.g. 00226677 002255
User written to database!
Done!
Press enter to try exit.
```

Success! You've added a user to Doccu.

Next, we need to make sure all the dependencies are up to date.

Launch the Management Console again:

```
doccu-manage
```

And enter *4*, to update the libraries that allow PDFs to work.

You should get a screen like:

```
Enter 1 to ADD a user
2 to REMOVE a User
3 to START the server
4 to updated browser-based dependencies
5 to updateserver-based dependencies:4
Updating javascript dependencies...
Updated!
```

If you get an *InsecurePlatformWarning*, you can resolve it by running:

```
pip install pyopenssl
```

Next, re-launch the Management Console:

```
doccu-manage
```

And then enter *5* so we can make sure Doccu's non-core files are up to date. (This is required the first time you launch Doccu).

You should get a screen like:

```
Enter 1 to ADD a user
2 to REMOVE a User
3 to START the server
4 to updated browser-based dependencies
5 to update server-based dependencies:5
Updating templates...
Updated!
```

Next, re-launch the Management Console:

```
doccu-manage
```

Then we just need to update Doccu's server, enter *6* and press enter. (This is required the first time you launch Doccu).

You should get a screen like:

```
Enter 1 to ADD a user
2 to REMOVE a User
3 to START the server
4 to updated browser-based dependencies
5 to updateserver-based dependencies:6
Updating server...
Updated!
```

Now we're ready to run Doccu!

Next, re-launch the Management Console:

```
doccu-manage
```

And enter *3*, and press enter.

You should get a screen like:

```
Enter 1 to ADD a user
2 to REMOVE a User
3 to START the server
4 to updated browser-based dependencies
5 to update server-based dependencies:3
Running on port 5000, logging to error.log
Running on port 5000, logging to error.log
```

So long as this Terminal or Command Prompt is open, Doccu should continue to run.

You can access Doccu at [http://localhost:5000](http://localhost:5000)

---

## Next Steps

* [Logging](Logging.md)
* [User Management](UserManagement.md)
* [Content Management](ContentManagement.md)
