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

import time

import dynamic_reconfigure as dyn_reconf
import dynamic_reconfigure.client
import rosservice
import rospy

from rqt_reconfigure.treenode_qstditem import TreenodeQstdItem

if __name__ == '__main__':
    try:
        nodes = dyn_reconf.find_reconfigure_services()
    except rosservice.ROSServiceIOException as e:
        rospy.logerr("Reconfigure GUI cannot connect to master.")
        raise e  # TODO Make sure 'raise' here returns or finalizes func.

    i_node_curr = 1
    num_nodes = len(nodes)
    elapsedtime_overall = 0.00
    for node_name_grn in nodes:
        time_siglenode_loop = time.time()

        try:
            _dynreconf_client = dynamic_reconfigure.client.Client(
                                               str(node_name_grn), timeout=5.0)
        except rospy.exceptions.ROSException:
            rospy.logerr("TreenodeQstdItem. Couldn't connect to {}".format(
                                                               node_name_grn))
        time_siglenode_loop = time.time() - time_siglenode_loop
        elapsedtime_overall += time_siglenode_loop
        print '{}th node. elapsed {} / {} sec'.format(i_node_curr,
                                                 round(time_siglenode_loop, 2),
                                                 round(elapsedtime_overall, 2))
        i_node_curr += 1
