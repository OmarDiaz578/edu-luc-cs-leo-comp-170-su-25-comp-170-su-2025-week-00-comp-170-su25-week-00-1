#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
1. first_name, is a valid name in python, because it is snake case, which is when we use '_' instead of spaces between words.
2. 2nd_name, is not a valid name in python as it starts with a number. 
3. age, is a valid name in python as it is alphaneumerical.
4. total_amount, is a valid name in python as it is snake case.
5. while, is not a valid name in python as it is a reserved word.
6. Student, is a valid name as it's alphaneumerical.
7. my-variable, is not a valid name in python as it cotains a special chracter.
8. for, is not a valid name in python as it is a reserved word.
9. _temp, is a valid name in python but leading with an underscore should be avoided unless necessary.
10. value#, is not a valid name in python as it contains a special character.


"""
# Problem 2
"""
1. calculate_total, is a valid name in python, because it is snake case.
2. 3rd_function, is not a valid name in python as it starts with a number.
3. print_values, is a valid name in python, because it is snake case.
4. find-item, is not a valid name in python as it cotains a special chracter.
5. def, is not a valid name in python as it is a reserved word.
6. updateProfile, is a valid name in python as it is alphaneumerical.
7. my_function, is a valid name in python, because it is snake case.
8. try, is a valid name in python as it is alphaneumerical.
9. init_data, is a valid name in python, because it is snake case.
10. value@function, is not a valid name in python as it contains a special character.



"""
# Problem 3
"""
1.True and False, valid, evaluates to False because of the truth table.
2. 5 > 3 or "apple" < "banana", valid, evaluates to True because of the truth table.
3. not 10 <= 20, valid, is False since 10 <= 20 is True, and not True is False.
4. True or 5 = 4, not valid, 5 = 4 should use "==" instead.
5. "apple" != "orange" and 5, not valid, doesn't evaluate.
6. 3 < 5 not True, not valid, missing logical opperator.
7. False == (3 > 4), valid, evaluates to true.
8. 10 <= "10", not valid, can't compare each other.
9. True or not False, valid, not False is True and True or True evaluates to True
10. 5 and or 4, not valid, can't have multiple logical opperators next to each other.

.
.

"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
