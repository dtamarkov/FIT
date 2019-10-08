#!/usr/bin/python

import sys, getopt
from typing import List

class Item:
    def __init__(self, weight: int, price: int):
        self.__weight = weight
        self.__price = price

    @property
    def price(self):
        return self.__price

    @property
    def weight(self):
        return self.__weight


class Problem:
    def __init__(self, id: int, n: int, m: int, c:int, items: List[Item]):
        self.__id = id
        self.__number_of_items = n
        self.__bag_capacity = m
        self.__min_price = c
        self.__items = items

    @property
    def id(self):
        return self.__id

    @property
    def number_of_items(self):
        return self.__number_of_items

    @property
    def bag_capacity(self):
        return self.__bag_capacity

    @property
    def min_price(self):
        return self.__min_price

    @property
    def items(self):
        return self.__items


class Solver:
    def __init__(self, problems: List[Problem]):
        self.__best_value = 0
        self.__problems = problems
    
    def solve_problems(self, problem):
        pass
    

def pairwise(list):
    a = iter(list)
    return zip(a, a)


def main(argv):
    inputfile = None
    outputfile = None
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    problems = []

    if inputfile:
        with open(inputfile) as f:
            for line in f:
                problem = line.split()
                info = problem[:4]
                items = problem[4:]
                items_list = []
                print(info)
                for w, p in pairwise(items):
                    items_list.append(Item(w, p))
                    print("weight:" + str(w) + " -> " + "price:" + str(p))
                print('----------------------------------------------------')
                problems.append(Problem(*info, items_list))
        

if __name__ == '__main__':
    main(main(sys.argv[1:]))