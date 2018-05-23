# https://py.checkio.org/en/mission/secret-message/


def find_message(text: str)-> str:
    secret = ""
    for character in text:
        if character.isupper():
            secret += character
    return secret


while True:
    enter = input("\nTo quit enter -1, to continue press any key\n")
    if enter != "-1":
        text = input("Enter message")
        print(find_message(text))
    else:
        break
