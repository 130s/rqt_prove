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
