#!/usr/bin/env python
import xml.etree.ElementTree as ET
import os
from pydoc import doc
import subprocess


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


def prv_dict_loop():
    """
    http://stackoverflow.com/questions/3294889/iterating-over-dictionaries-for-loops-in-python
    """
    d = {'x': 1, 'y': 2, 'z': 3}
    #for key in d:
    for poo in d:
        key = poo
        print key, 'corresponds to', d[key]


def prv_elemtree():
    tree = ET.parse("test.xml")
    print tree

    doc = tree.getroot()
    print doc.attrib
    thingies = tree.findall('arg')
    #print thingy.attrib
    for thingy in thingies:
        print thingy.attrib


def prv_os_usage():
    """Return int containing memory used by user's processes."""
    username = 'isaito'
    process = subprocess.Popen("ps -u %s -o rss | awk '{sum+=$1} END {print sum}'" % username,
                               shell=True, stdout=subprocess.PIPE)
    stdout_list = process.communicate()[0].split('\n')
    print stdout_list
    print int(stdout_list[0])


if __name__ == '__main__':
    prv_os_usage()
    #prv_elemtree()
    #prv_dict_loop()
    #prv_isspace()
    #prv_find_last_occurrence()
    #pv_list_comprehension()
