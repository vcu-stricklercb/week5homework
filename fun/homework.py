"""Homework file for my students to have fun with some algorithms! """
def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
incoming_list = [1,2,3,4,5]
incoming_list.sort()
greatest_number = incoming_list[-1]
print(greatest_number)
pass
def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
incoming_list = [1,2,3,4,5]
incoming_list.sort()
smallest_number = incoming_list[:1]
print(smallest_number)
pass
def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
incoming_list = [1,2,3,4,5]
Addlist = sum(incoming_list)
print(Addlist)
pass
def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
incoming_dict = ['blue', 'green', 'black', 'orange', 'yellow', 'burgundy']
largest_word = max(incoming_dict, key = len)
print(largest_word)
pass
