## ROS PUBLISHERS
'''
Publishers allow a node to send messages to a topic,
so that data from the node can be used in other parts of the ROS system.
In Python, ROS publishers typically have the following definition format,
although other parameters and arguments are possible:
'''
pub1 = rospy.Publisher("/topic_name", message_type, queue_size=size)

