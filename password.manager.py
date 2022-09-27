from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
  with open('passwords.txt', 'r') as f:
    for line in f.readlines():
        data = line.rstrip()
        user, passw = data.split("|")
        print("User:", user, "| Password:",
        fer.decrypt(passw.encode()).decode())

        # rstrip will take away the carriage return
        # the .split is splitting the data that is seperated by a pipe(|) 

def add():
  name = input("Account Name: ")
  pwd = input("Password: ")

  with open('passwords.txt', 'a') as f:
   f.write(name + "|" + (fer.encrypt(pwd.encode()).decode()) + "\n")

    # the 'with' element will automatically close the file once the open() is completed. without the with, you would have to create another line of code
    # 'open' literally opens a file
    # the 'a' is a mode that the file is being opened in. there are a few different modes with different meanings, however there are 3 primary ones. the 3 primary meanings are down below
    # w mode will write a new file, even to the point of overwriting it
    # r mode will simply read the file and do nothing else with it
    # a mode will add something to the exisitng file and create a new file if it does not exist
    # 'f' is the type of thing we are creating/opening. f stands for file.
    #\n simply creates a new line within the file that we have created

while True:
  mode = input('Would you like to add a new password or add an exisiting one(view, add)? ')
  if mode == "q":
      break

  if mode == "view":
      view()
  elif mode == "add":
      add()
  else:
   print("Invalid Mode.")
   continue