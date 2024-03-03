#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [even for even in num_list if even % 2 == 0]
    return even_numbers


def make_exclamation(sentence_list):
    exclaimed_list = [f"{list_item}!" for list_item in sentence_list]
    return exclaimed_list


print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))

