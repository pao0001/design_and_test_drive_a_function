"""check if text is a string

search a string, 

check if todo is present

Task has to have #TODO

Return all strings with #TODO"""

# def test_check_if_string():
#     # check if text is a string, force string input.
#     result = includes_todo(text)
#     return str

def test_search_string():
    # search a string, if #TODO present, return True
    result = includes_todo('#TODO drinking coffee')
    assert '#TODO drinking coffee' == True