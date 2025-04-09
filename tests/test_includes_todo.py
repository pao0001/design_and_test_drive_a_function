from lib.includes_todo import *

# check if text is a string
    # find() makes sure is string
# search a string, 
    # done, using find
# check if todo is present
    # done, using find
# Task has to have #TODO

# Return all strings with #TODO""

# def test_check_if_string():
#     # check if text is a string, force string input.
#     result = includes_todo(text)
#     return str

def test_search_string_true():
    assert includes_todo('#TODO drinking coffee') == True
def test_search_string_false():
    assert includes_todo('coffeetime!') == False
def test_search_string_string():
    assert includes_todo(35) == False