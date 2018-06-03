while True:
    enter = input("\nTo quit enter -1, to continue press any key\n")
    if enter != "-1":
        text = list(input("Enter text: "))
        for i in range(0, len(text)-1):
            if text[i] == ' ':
                text[i] = '_'
            elif text[i] == '_':
                text[i] = ' '
        print("\nResult:")
        print("".join(text))
    else:
        break
