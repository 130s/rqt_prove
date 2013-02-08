#!/usr/bin/env python
import os
        
def pv_list_comprehension():
    names = ['a', 'b', 'c', 'c']
    names_chosen = [n for n in names if n =='c']    
    print 'len={}'.format(len(names_chosen))

def prv_find_last_occurrence():
    s = 'lol, aha'
    print s[s.rfind('l') + 1:]

def prv_isspace():
    str = ' '    
    if (not str) or (str.isspace()):
        print 'recognized as empty'
    else:
        print 'Not recognized as empty                                             '      
        
if __name__ == '__main__':
    prv_isspace()
    #prv_find_last_occurrence()
    #pv_list_comprehension()
            