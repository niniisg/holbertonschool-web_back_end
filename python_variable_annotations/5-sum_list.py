#!/usr/bin/env python3

""" 
this is a function that takes a list of floats as input
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum list of floating point numbers


    :arg input_list: the list of float numbers
    :return: returns the sum of float numbers in a list
    """
    return sum(input_list)
