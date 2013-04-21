# Software License Agreement (BSD License)
#
# Copyright (c) 2012, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: Isaac Saito

import sys
import threading
from time import sleep, time

from PyQt4.QtGui import QApplication, QWidget


class ThreadArg(object):
    def __init__(self):
        self._val = None

    def set_val(self, val):
        self._val = val

    def get_val(self):
        return self._val


class PrvThreadGen(threading.Thread):

    def __init__(self, thread_obj):
        super(PrvThreadGen, self).__init__()

        self._condition_variable = threading.Condition()
        self._configs_pending = {}
        self._timestamp_last_pending = None
        self._stop_flag = False
        print ' Thread initted'
        self._thread_obj = thread_obj

    def run(self):
        _timestamp_last_commit = None
        print ' Thread started'
        val = QWidget()
        self._thread_obj.set_val(val)


def simple_thread_run():
    obj = ThreadArg()
    main = PrvThreadGen(obj)
    main.start()
    sleep(10)
    print ' val={}'.format(obj.get_val())


def many_thread_run():
    time_begin = time() * 1000
    for i in range(900):
        obj = ThreadArg()
        main = PrvThreadGen(obj)
        main.start()
        print ' #{}'.format(i)
    print ' time took={}'.format(time() - time_begin)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    many_thread_run()
