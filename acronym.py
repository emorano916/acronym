

def abbreviate(full_name: str):
    full_name_cap = full_name.title()
    full_name_cap2 = full_name_cap.strip(-)
    full_name_list = full_name_cap2.split()  # create a list
    init_list = []  # initialize a new list

    for full_name in full_name_list:  # for loop in the list
        init_list.append(full_name[0])  # add of the first letter of each word in the list
    return "".join(init_list)  # create an acronym

full_name1 = "Oh My God"
abbreviate(full_name1)
