


def includes_todo(string):

    if not isinstance(string, str):
        print("This is not a string")
        return False
    elif string.find("#TODO") == -1:
        return False
    else:
        print(string)
        return True

