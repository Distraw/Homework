def max_in_sublist(user_list: list[list[int]]) -> int:
    max_element = user_list[0][0]

    for sublist in user_list:
        for element in sublist:
            if element > max_element:
                max_element = element

    return max_element

def pythonic_max_in_sublist(user_list: list[list[int]]) -> int:
    return max(max(sublist) for sublist in user_list)

global_list1 = [ [2, -5], [-2, 3], [-4, 7] ]
global_list2 = [ [-2, 3], [-4, 9], [-1, 7] ]
def global_arg_max_in_sublist() -> [int]:
    return max(max(sublist) for sublist in global_list1), max(max(sublist) for sublist in global_list2)


if __name__ == "__main__":
    list1 = [ [2, -5], [-2, 3], [-4, 7] ]
    list2 = [ [-2, 3], [-4, 9], [-1, 7] ]

    max_from_list1 = max_in_sublist(list1)
    max_from_list2 = max_in_sublist(list2)


    pythonic_max_from_list1 = max_in_sublist(list1)
    pythonic_max_from_list2 = max_in_sublist(list2)

    global_max_from_list1, global_max_from_list2 = global_arg_max_in_sublist()

    print("List1: " + str(max_from_list1))
    print("List2: " + str(max_from_list2))

    print("Pythonic list1: " + str(pythonic_max_from_list1))
    print("Pythonic list2: " + str(pythonic_max_from_list2))

    print("Global list1: " + str(global_max_from_list1))
    print("Global list2: " + str(global_max_from_list2))