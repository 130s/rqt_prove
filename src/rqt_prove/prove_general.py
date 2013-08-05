#!/usr/bin/env python
import xml.etree.ElementTree as ET
import os
from pydoc import doc
import subprocess
import time

import rospy
from std_msgs.msg import String


def pv_list_comprehension():
    names = ['a', 'b', 'c', 'c']
    names_chosen = [n for n in names if n == 'c']
    print 'len={}'.format(len(names_chosen))


def prv_find_last_occurrence():
    s = 'lol, aha'
    print s[s.rfind('l') + 1:]


def prv_isspace():
    str = ' '
    if (not str) or (str.isspace()):
        print 'recognized as empty'
    else:
        print 'Not recognized as empty'


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
    tree = ET.parse("pr2_bringup.launch")
    print tree

    doc = tree.getroot()
    print doc.attrib
    #thingies = tree.findall('arg')
    thingies = tree.findall('include')
    #print thingy.attrib
    for thingy in thingies:
        print thingy.attrib

    node = 'node'
    print 'from here: {}'.format(node)
    thingies = tree.findall(node)
    for thingy in thingies:
        print thingy.attrib


def prv_os_usage():
    """Return int containing memory used by user's processes."""
    username = 'n130s'
    process = subprocess.Popen(\
         "ps -u {} -o rss | awk '{sum+=$1} END {print sum}'".format(username),
         shell=True, stdout=subprocess.PIPE)
    stdout_list = process.communicate()[0].split('\n')
    print stdout_list
    print int(stdout_list[0])


def prv_str_dict_conversion():
    val_a = object
    str = 'sample str'
    dict = {'key_a': val_a}
    print 'before: {}'.format(str)
    str = dict
    print 'after: {}'.format(str)


def prv_if_obj():
    list_obj = [None, 'a', 'b']
    for i in list_obj:
        if not i:
            print 'none?'
        else:
            print i


class PrvPydevAutocompletion(object):
    def __init__(self):
        pass

    def method1(self):
        pass

    def method2(self):
        pass


def prv_pydev_autocompletion_return():
    """
    @rtype: prove_general.PrvPydevAutocompletion
    """
    p = PrvPydevAutocompletion()
    return p


def prv_pydev_autocompletion():
    s = prv_pydev_autocompletion_return()


def prv_rm_list_elem():
    list = ['a', 'b', 'c', 'd', 'b', 'e']
    list = [x for x in list if x != 'f']
    print list


_list_prv_global_var = []
def prv_global_var1():
    _list_prv_global_var.append('elem1')


def prv_global_var1_1():
    print 'dummy'


def prv_global_var2():
    prv_global_var1()
    print 'list={}'.format(_list_prv_global_var)


def prv_dyn_import():
    rn = __import__('rosnode')
    print 'before={}'.format(rn)
    print rn.rosnode_ping('/turtlesim', 1)
    del rn
    #print 'before={}'.format(rn)


def prv_sum():
    a = range(11)
    print sum(a)


def prv_slicing():
    a = range(11)
    print a[:5]
    print a[5+1:]


def prv_sleep():
    '''To see if cpu process is made while running python'''
    print 'before sleep'
    time.sleep(15)
    rospy.init_node('node_name')
    rospy.Subscriber("chatter", String, prv_sleep_callback)

    print 'after sleep'
    time.sleep(15)


def prv_sleep_callback(data):
    rospy.loginfo("I heard %s", data.data)


if __name__ == '__main__':
    prv_sleep()

    #prv_if_obj()
    #prv_str_dict_conversion()
    #prv_os_usage()
    #prv_elemtree()
    #prv_dict_loop()
    #prv_isspace()
    #prv_find_last_occurrence()
    #pv_list_comprehension()
