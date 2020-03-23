# setupBox
This allows you to add the current HTB Box IP and name to the `/etc/hosts` file, and also create a folder for the box in your htb folder.

# How To Setup

There should be a folder like `/root/hackthebox/` or `/root/htb/`

Inside that folder there should be at least 2 folders with the names of `boxes` and `boxGen` you will put the python file in `boxGen`

Then install the requirement by typing `pip install hostsman`

Then when you run the program you will br prompted for the box Name and IP. It will then add that information to the `/etc/hosts` file so that instead of typing in the IP every time you can just right `boxname.htb`.

When you are in the directory that the python folder is in you can run `python3 setupBox.py` 

Working on making the program run from anywhere.
