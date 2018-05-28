def generate_numbers():
    while True:
        enter = input("\nTo quit enter -1, to continue press any key\n")
        if enter != "-1":
            number = int(input("Enter number: "))
            print({x: x*x for x in range(1, number+1)})
        else:
            break


def count_characters():
    while True:
        enter = input("\nTo quit enter -1, to continue press any key\n")
        if enter != "-1":
            string = input("Enter string: ")
            print({x: string.count(x) for x in list(string)})
        else:
            break


def fizz_buzz():
    result = []
    for i in range(1, 101):
        result.append("")
        if i % 3 == 0:
            result[i-1] += "Fizz"
        if i % 5 == 0:
            result[i-1] += "Buzz"
        if result[i-1] == "":
            result[i-1] += str(i)
    print(result)


def is_palindrome():
    while True:
        enter = input("\nTo quit enter -1, to continue press any key\n")
        if enter != "-1":
            word = input("Enter word: ")
            rev_word = word[::-1]
            if word == rev_word:
                result = True
            else:
                result = False
            print(result)
        else:
            break
