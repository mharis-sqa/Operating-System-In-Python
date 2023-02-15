import os
import time

with open('info.data', 'w') as f:
	f.writelines("1")

print("""

░██████╗███████╗████████╗██╗░░░██╗██████╗░
██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗
╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝
░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░
██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░
╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░

""")

name = input("Please Enter Your Username To Be Displayed: ")
pas = input("Please Enter Your Password To Login: ")

with open('dataname.pass', 'w') as f:
	f.writelines(name)

with open('password.pass', 'w') as f:
	f.writelines(pas)

print("Setup Complete!!!")
print("Opening Login Page...")
time.sleep(0.5)
os.startfile('login.py')