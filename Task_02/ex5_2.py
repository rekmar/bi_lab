#https://py.checkio.org/en/mission/the-most-frequent/


def most_frequent(data: list) -> str:
    return max(data, key=data.count)


while True:
    enter = input("\nTo quit enter -1, to continue press any key\n")
    if enter != "-1":
        text = input("Enter words with a space: ").split(' ')
        print(most_frequent(text))
    else:
        break
