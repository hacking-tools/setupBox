# setupBox
This allows you to add the current HTB Box IP and name to the `/etc/hosts` file.

# How To Setup

Then install the requirement by typing `pip install hostsman`

Then when you run the program you will br prompted for the box Name and IP. It will then add that information to the `/etc/hosts` file so that instead of typing in the IP every time you can just right `boxname.htb`.

# Installation:
1. Download the newest release from the releases tab.
2. Unzip the file.
3. In terminal, navigate to the directory that the file `setupBox` is in.
4. Then type the command: `sudo mv ./setupBox /usr/local/bin/setupBox; chmod +x /usr/local/bin/setupBox`
5. Test the program out by typing `setupBox` and follow the steps to setup the IP.
