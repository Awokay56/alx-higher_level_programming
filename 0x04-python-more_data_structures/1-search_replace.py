#!/usr/bin/python3
#1-search_replace.py

def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list=my_list[:]
    for idx, d in enumerate(new_list):
        if d == search:
            new_list[idx] = replace
            return new_list
