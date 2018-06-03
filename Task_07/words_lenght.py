import re

reg = '[a-zA-Z]{3,5}'

while True:
    enter = input("\nTo quit enter -1, to continue press any key\n")
    if enter != "-1":
        text = input("Enter text: ")
        print("Three - five long words:")
        for em in re.findall(reg, text):
            print(em)
    else:
        break
