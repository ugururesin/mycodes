#######################
## WRITING ROS NODES ##
#######################

## ROS PUBLISHERS
############################################################
'''
Publishers allow a node to send messages to a topic,
so that data from the node can be used in other parts of the ROS system.
In Python, ROS publishers typically have the following definition format,
although other parameters and arguments are possible:
'''
pub1 = rospy.Publisher("/topic_name", message_type, queue_size=size)

'''
ROS publishing can be either synchronous or asynchronous:

## Synchronous publishing
Means that a publisher will attempt to publish to a topic but may be blocked
if that topic is being published to by a different publisher.
In this situation, the second publisher is blocked until the first publisher has serialized
all messages to a buffer and the buffer has written the messages to each of the topic's subscribers. 
This is the default behavior of a "rospy.Publisher" if the "queue_size" parameter is not used or set to "None".

## Asynchronous publishing 
Mans that a publisher can store messages in a queue until the messages can be sent.
If the number of messages published exceeds the size of the queue, the oldest messages are dropped.
The queue size can be set using the "queue_size" parameter.

Once the publisher has been created as above, a message with the specified data type can be published as follows:
'''
pub1.publish(message)


## IMPLEMENTING ROS NODE
############################################################
'''
The node is called simple_mover. 
This node only has one responsibility, and that is to command joint movements for simple_arm.

To do so, it must publish joint angle command messages to the following topics:
Topic Name 		/simple_arm/joint_1_position_controller/command
Message Type 	std_msgs/Float64
Description 	Commands joint 1 to move counter-clockwise, units in radians
Topic Name 		/simple_arm/joint_2_position_controller/command
Message Type 	std_msgs/Float64
Description 	Commands joint 2 to move counter-clockwise, units in radians

Note: You must have the catkin workspace!

## Adding the scripts directory
In order to create a new node in python,
you must first create the "scripts directory" within the simple_arm package

$ cd ~/catkin_ws/src/simple_arm/
$ mkdir scripts

## Creating a new script
Once the scripts directory has been created, executable scripts can be added to the package.
However, in order for rosrun to find them, their permissions must be changed to allow execution.
Let’s add a simple bash script that prints “Hello World” to the console.

$ cd scripts
$ echo '#!/bin/bash' >> hello
$ echo 'echo Hello World' >> hello

After setting the appropriate execution permissions on the file, rebuilding the workspace,
and sourcing the newly created environment, you will be able to run the script.

$ chmod u+x hello
$ cd ~/catkin_ws
$ catkin_make
$ source devel/setup.bash
$ rosrun simple_arm hello

And there you have it! You have now added a script

Creating the empty simple_mover node script
To create the simple_mover node script,
you will must simply follow the same basic routine introduced a moment ago.

$ cd ~/catkin_ws/src/simple_arm
$ cd scripts
$ touch simple_mover
$ chmod u+x simple_mover
'''

## CREATING A ROS NODE with PYTHON
############################################################
#!/usr/bin/env python

import math
import rospy
#The official Python client library for ROS

from std_msgs.msg import Float64
#From the std_msgs package, we import Float64, which is one of the primitive message types in ROS.

def mover():
	'''
	Below, 2 publishers are declared, one for joint 1 commands, and one for joint 2 commands.
	Here, the queue_size parameter is used to determine the maximum number messages
	that may be stored in the publisher queue before messages are dropped.
	More information about this parameter can be found here.
	'''
    pub_j1 = rospy.Publisher('/simple_arm/joint_1_position_controller/command',
                             Float64, queue_size=10)
    pub_j2 = rospy.Publisher('/simple_arm/joint_2_position_controller/command',
                             Float64, queue_size=10)
    
    '''
    Initializes a client node and registers it with the master.
    Here “arm_mover” is the name of the node. init_node() must be called
    before any other rospy package functions are called.
    The argument anonymous=True makes sure that you always have a unique name for your node
    '''
    rospy.init_node('arm_mover')

    '''
    The rate object is created here with a value of 10 Hertz.
    Rates are used to limit the frequency at which certain loops spin in ROS.
    Choosing a rate which is too high may result in unnecessarily high CPU usage,
    while choosing a value too low could result in high overall system latency.
    Choosing sensible values for all of the nodes in a ROS system is a bit of a fine-art.
    '''
    rate = rospy.Rate(10)	#10Hz

    '''
    start_time is used to determine how much time has elapsed.
    When using ROS with simulated time (as we are doing here), rospy.Time.now() will initially return 0,
    until the first message has been received on the /clock topic.
    This is why start_time is set and polled continuously until a nonzero value is returned
    '''
    start_time = 0
    while not start_time:
        start_time = rospy.Time.now().to_sec()

    '''
    This the main loop.
    Due to the call to rate.sleep(), the loop is traversed at approximately 10 Hertz.
    Each trip through the body of the loop will result in two joint command messages being published.
    The joint angles are sampled from a sine wave with a period of 10 seconds,
    and in magnitude from [-pi/2, +pi/2].
    When the node receives the signal to shut down (either from the master,
    or via SIGINT signal in a console window), the loop will be exited.
    '''
    while not rospy.is_shutdown():
        elapsed = rospy.Time.now().to_sec() - start_time
        pub_j1.publish(math.sin(2*math.pi*0.1*elapsed)*(math.pi/2)) #0.1 for 10Hz
        pub_j2.publish(math.sin(2*math.pi*0.1*elapsed)*(math.pi/2))
        rate.sleep()

'''
If the name variable is set to “main”, indicating that this script is being executed directly,
the mover() function will be called.
The try/except blocks here are significant as rospy uses exceptions extensively.
The particular exception being caught here is the ROSInterruptException.
This exception is raised when the node has been signaled for shutdown.
If there was perhaps some sort of cleanup needing to be done before the node shuts down, it would be done here.
'''
if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException:
        pass


## RUNNING A ROS NODE with PYTHON
############################################################
'''
Assuming that your workspace has recently been built & setup.bash has been sourced

The "simple_arm" node can be launched as follows:

$ cd ~/catkin_ws
$ roslaunch simple_arm robot_spawn.launch

Once ROS Master, Gazebo, and all of our relevant nodes are up and running,
we can finally launch simple_mover. 
To do so, open a new terminal and type the following commands:

$ cd ~/catkin_ws
$ source devel/setup.bash
$ rosrun simple_arm simple_mover
'''


## ROS-SERVICES
############################################################

## Defining Services
service = rospy.Service('service_name', serviceClassName, handler)

## Using Services
service_proxy = rospy.ServiceProxy('service_name', serviceClassName)

msg = serviceClassNameRequest()
#update msg attributes here to have correct data
response = service_proxy(msg)

'''
In the code above, a new service message is created by calling the serviceClassNameRequest() method.
This method is provided by rospy, and its name is given by appending Request()
to the name used for serviceClassName. Since the message is new,
the message attributes should be updated to have the appropriate data.
Next, the service_proxy can be called with the message, and the response stored.
'''


## THE Arm-Mover
############################################################
''' 
Custom message generation
Services
Parameters
Launch Files
Subscribers
Logging
'''

## Description of Arm Mover
'''
It is responsible for commanding the arm to move.

The arm_mover node provides the service move_arm,
which allows other nodes in the system to send movement_commands.
'''

## Creating a new service definition
'''
The definitions of the request and response message type are contained within .srv files
living in the srv directory under the package’s root.

Let’s define a new service for simple_arm. We shall call it GoToPosition.
$ cd ~/catkin_ws/src/simple_arm/
$ mkdir srv
$ cd srv
$ touch GoToPosition.srv

You should now edit GoToPosition.srv, so it contains the following:

float64 joint_1
float64 joint_2
---
duration time_elapsed


Service definitions always contain two sections, separated by a ‘---’ line.
The first section is the definition of the request message. 
Here, a request consists of two float64 fields, one for each of simple_arm’s joints. 
The second section contains is the service response.
The response contains only a single field, time_elapsed.
The time_elapsed field is of type duration, and is responsible for
indicating how long it took the arm to perform the movement.
'''

#!/usr/bin/env python

import math
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from simple_arm.srv import *

'''
The imported modules for arm_mover are the same as simple_arm, with the exception of two new imports.
Namely, the JointState message, and the simple_arm.srv module.

JointState messages are published to the /simple_arm/joint_states topic,
and are used for monitoring the position of the arm.

The simple_arm package, and the srv module are automatically generated by catkin as part of the build process.
'''

def at_goal(pos_j1, goal_j1, pos_j2, goal_j2):
	'''
	This function returns True if the joint positions are close to the goals.
	When taking measurements from sensors in the real world, there will always be some amount of noise.
	The same is true of the joint positions reported by the gazebo simulator.
	If both joint positions are within .05 radians of the goal, True is returned.
	'''
    tolerance = .05
    result = abs(pos_j1 - goal_j1) <= abs(tolerance)
    result = result and abs(pos_j2 - goal_j2) <= abs(tolerance)
    return result

def clamp_at_boundaries(requested_j1, requested_j2):
	'''
	This function is responsible for enforcing the minimum and maximum joint angles for each joint.
	If the joint angles passed in are outside of the operable range,
	they will be “clamped” to the nearest allowable value.
	'''
    clamped_j1 = requested_j1
    clamped_j2 = requested_j2

    min_j1 = rospy.get_param('~min_joint_1_angle', 0)
    max_j1 = rospy.get_param('~max_joint_1_angle', 2*math.pi)
    min_j2 = rospy.get_param('~min_joint_2_angle', 0)
    max_j2 = rospy.get_param('~max_joint_2_angle', 2*math.pi)
    '''
    The minimum and maximum joint angles are retrieved from the parameter server
    each time clamp_at_boundaries() is called.
    The “~” is the private namespace qualifier,
    and indicates that the parameter we wish to get is within this node’s private namespace /arm_mover/
    (e.g. ~min_joint_1_angle resolves to /arm_mover/min_joint_1_angle).
    The second parameter is the default value to be returned,
    in the case that rospy.get_param() was unable to get the parameter from the param server.
    '''

    '''
    The rest of this function simply clamps the joint angle if necessary.
    Warning messages are logged if the requested joint angles are out of bounds.
    '''
    if not min_j1 <= requested_j1 <= max_j1:
        clamped_j1 = min(max(requested_j1, min_j1), max_j1)
        rospy.logwarn('j1 is out of bounds, valid range (%s,%s), clamping to: %s',
                      min_j1, max_j1, clamped_j1)

    if not min_j2 <= requested_j2 <= max_j2:
        clamped_j2 = min(max(requested_j2, min_j2), max_j2)
        rospy.logwarn('j2 is out of bounds, valid range (%s,%s), clamping to: %s',
                      min_j2, max_j2, clamped_j2)

    return clamped_j1, clamped_j2

def move_arm(pos_j1, pos_j2):
	'''
	Commands the arm to move, returning the amount of time that elapsed while the arm was moving.
	Note: Within the function we are using the rospy.wait_for_message() call to receive
	JointState messages from the /simple_arm/joint_states topic.
	This is blocking function call, meaning that it will not return until
	a message has been received on the /simple_arm/joint_states topic.

	In general, you should not use wait_for_message().
	We simply use it here for the sake of clarity, and because move_arm is being called
	from the handle_safe_move_request() function, 
	which demands that the response message is passed back as a return parameter.
    '''
    time_elapsed = rospy.Time.now()
    j1_publisher.publish(pos_j1)
    j2_publisher.publish(pos_j2)

    while True:
        joint_state = rospy.wait_for_message('/simple_arm/joint_states', JointState)
        if at_goal(joint_state.position[0], pos_j1, joint_state.position[1], pos_j2):
            time_elapsed = joint_state.header.stamp - time_elapsed
            break

    return time_elapsed

def handle_safe_move_request(req):
	'''
	This is the service handler function.
	When a service client sends a GoToPosition request message to the safe_move service,
	this function is called.
	The function parameter req is of type GoToPositionRequest.
	The service response is of type GoToPositionResponse.

	This is the service handler function, it is called whenever a new service request is received.
	The response to the service request is returned from the function.

	Note: move_arm() is blocking, and will not return until the arm has finished its movement.
	Incoming messages cannot be processed, and no other useful work can be done in the python script
	while the arm is performing it’s movement command.
	While this poses no real problem for this example, it is a practice that should generally be avoided.
	One great way to avoid blocking the thread of execution would be to use Action.
    '''
    rospy.loginfo('GoToPositionRequest Received - j1:%s, j2:%s',
                   req.joint_1, req.joint_2)
    clamp_j1, clamp_j2 = clamp_at_boundaries(req.joint_1, req.joint_2)
    time_elapsed = move_arm(clamp_j1, clamp_j2)

    return GoToPositionResponse(time_elapsed)

def mover_service():
	'''
	Here the node is initialized with the name “arm_mover”,
	and the GoToPosition service is created with the name “safe_move”.

	As mentioned previously, the “~” qualifier identifies that safe_move is meant
	to belong to this node’s private namespace.

	The resulting service name will be /arm_mover/safe_move .
	The third parameter to the rospy.Service() call is the function that
	should be called when a service request is received.

	Lastly, rospy.spin() simply blocks until a shutdown request is received by the node.
	Failure to include this line would result in mover_service() returning, and the script completing execution.
    '''
    rospy.init_node('arm_mover')
    service = rospy.Service('~safe_move', GoToPosition, handle_safe_move_request)
    rospy.spin()

if __name__ == '__main__':
    j1_publisher = rospy.Publisher('/simple_arm/joint_1_position_controller/command',
                                   Float64, queue_size=10)
    j2_publisher = rospy.Publisher('/simple_arm/joint_2_position_controller/command',
                                   Float64, queue_size=10)

    try:
        mover_service()
    except rospy.ROSInterruptException:
        pass


## LAUNCH & INTERACT
############################################################
'''
Launching the project with the new service
To get the arm_mover node, and accompanying safe_move service to launch along with all of the other nodes,
you will modify robot_spawn.launch.

Launch files, when they exist, are located within the launch directory in the root of a catkin package.
simple_arm’s launch file is located in ~/catkin_ws/src/simple_arm/launch

To get the arm_mover node to launch, simply add the following:

<!-- The arm mover node -->
<node name="arm_mover" type="arm_mover" pkg="simple_arm">
<rosparam>
  min_joint_1_angle: 0
  max_joint_1_angle: 1.57
  min_joint_2_angle: 0
  max_joint_2_angle: 1.0
</rosparam>
</node>























