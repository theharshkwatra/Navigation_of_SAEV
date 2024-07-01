#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge


class camera_sensor_check : 
    def __init__(self):
        sub_topic_name = "robot/camera_top/rgb/image_raw"
        self.camera_subscriber = rospy.Subscriber(sub_topic_name,Image,self.camera_callback)
        self.out = cv2.VideoWriter('~/home/Desktop/test.avi',cv2.VideoWriter_fourcc('M','J','P','G'),10,(640,480))
        self.bridge = CvBridge()

    def camera_callback(self, data):
        frame = self.bridge.imgmsg_to_cv2(data)
        edge_frame = cv2.Canny(frame,100,200)
        self.out.write(edge_frame)
        print(edge_frame.shape)
        cv2.imshow("output",edge_frame)
        cv2.waitKey(1)

if __name__ == '__main__':
    node_name = "camera_sensor_check"
    rospy.init_node(node_name)
    camera_sensor_check()
    rospy.spin()