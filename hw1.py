"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    #This function computes the amount of vowels in a string
    #The text parameter takes in a string
    #The function returns an integer that represents the count of vowels
    # TODO: Replace this exception with your implementation.
    lower_text = text.lower()
    count = 0
    for char in lower_text:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1
    return count


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # This function computes a new list of lists of the passed in list of lists that only contain two integers
    # The items parameter takes in a list of list of its specifically
    # The function returns a list of lists of the passed in list of lists that only contain two integers
    # TODO: Replace this exception with your implementation.
    new_list = []
    for list in items:
        if len(list) == 2:
            new_list.append(list)
    return new_list


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    #This function will return a new list of lists of ints, keeping the same order but have lists of length two have a list of ints in descending order
    #Items is the list of lists of ints
    #The function returns a list of lists of ints based off the computation
    new_list = []
    for item in items:
        if len(item) != 2:
            new_list.append(item)
        elif len(item) == 2 and item[1] > item[0]:
            new_list.append([item[0], item[1]])
        else:
            new_list.append(item)
    return new_list
                    

# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    #The function computes two prices and returns a new price if there are excess cents
    #The first and second parameters are two different values of dollars and cents
    #The output is a new Price object that adds together the two values and makes sure there are no excess cents > 100
    if (first.cents + second.cents) >= 100:
        return data.Price((first.dollars+second.dollars+1), ((first.cents + second.cents) - 100))
    return data.Price((first.dollars+second.dollars), (first.cents + second.cents))



# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 5: implement rectangle_area")


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 6: implement books_by_author")


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 7: implement circle_bound")


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 8: implement below_pay_average")
