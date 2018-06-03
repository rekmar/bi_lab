def division():
    try:
        print(5/0)
    except ZeroDivisionError:
        print("You cannot divide to zero\n")


def print_list_element(the_list, index):
    try:
        print(the_list[index])
    except IndexError:
        print("Index is out of bounds\n")


def add_to_list_in_dict(the_dict, list_name, element):
    try:
        length = the_dict[list_name]
        print("%s already has %d elements." % (list_name, len(length)))
    except KeyError:
        the_dict[list_name] = []
        print("Created %s." % list_name)
    finally:
        the_dict[list_name].append(element)
        print("Added %s to %s.\n" % (element, list_name))


division()

my_list = [1, 2, 3]
# valid index
print_list_element(my_list, 1)
# invalid index
print_list_element(my_list, 6)

my_dict = {1: [1, 3, 5], 2: [2, 4, 6]}
add_to_list_in_dict(my_dict, 2, 4)
add_to_list_in_dict(my_dict, 1, 7)
