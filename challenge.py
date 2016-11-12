#!/usr/bin/env python

class MultipleNumber():
    def __init__(self, number):
        self.number = number

    def listMulti(self, first_number, last_number):
        result_list = [i * self.number for i in range(first_number/self.number, last_number/self.number + 1)]
        if result_list[0] == 0 or result_list[0] < first_number:
            result_list.pop(0)
        return result_list

def replace(a, b, c):
    stand = 0
    for i in b:
        index = a[stand:].index(i)
        a[stand + index] = c
        stand += index
    return a

if __name__ == "__main__":
    #Set params
    start = 30
    end = 300
    numb1 = 7
    numb2 = 13

    #create list from number start and end
    o_list = range(start, end+1)

    #get list number change to alphabet
    multi1 = MultipleNumber(numb1)
    list1 = multi1.listMulti(start, end)
    multi2 = MultipleNumber(numb2)
    list2 = multi2.listMulti(start, end)
    multi3 = MultipleNumber(numb1*numb2)
    list3 = multi3.listMulti(start, end)
    list1 = sorted(list(set(list1) - set(list3)))
    list2 = sorted(list(set(list2) - set(list3)))

    #replace original list
    o_list = replace(o_list, list1, 'abc')
    o_list = replace(o_list, list2, 'yxz')
    o_list = replace(o_list, list3, 'a-z')

    #print list after replace
    print o_list
