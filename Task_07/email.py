import re

reg = '[a-zA-Z0-9_%+-]{1,}\@[a-z0-9-]{1,}\.[a-z]{1,}'

while True:
    enter = input("\nTo quit enter -1, to continue press any key\n")
    if enter != "-1":
        text = input("Enter text with email: ")
        print("Emails: ")
        for em in re.findall(reg, text):
            print(em)
    else:
        break
