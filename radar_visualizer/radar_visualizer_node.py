#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import Header, ColorRGBA
from geometry_msgs.msg import Point
from delphi_esr_msgs.msg import EsrTrack # 메시지 타입에 따라 수정 필요

import math

class RadarVisualizer(Node):
    def __init__(self):
        super().__init__('radar_visualizer')

        self.declare_parameter('marker_duration', 0.16)
        self.declare_parameter('marker_duration_velocity', 5.0)

        self.marker_duration = self.get_parameter('marker_duration').get_parameter_value().double_value
        self.marker_duration_velocity = self.get_parameter('marker_duration_velocity').get_parameter_value().double_value

        self.get_logger().info(f"Marker Duration: {self.marker_duration} sec (Normal), {self.marker_duration_velocity} sec (with Velocity)")
        self.subscription = self.create_subscription(MarkerArray, '/radar_1/can_vis_markers', self.listener_callback, 10)
        self.marker_pub = self.create_publisher(MarkerArray, '/radar_1/can_vis_markers_long', 10)

    def listener_callback(self, msg):
        extended_markers = MarkerArray()

        for marker in msg.markers:
            if marker.lifetime.sec == 0 and marker.lifetime.nanosec == 0:
                continue

            new_marker = Marker()
            new_marker = marker  # shallow copy

            # Marker with speed infomation
            if "m/s" in marker.text or marker.color.r == 0.0:
                new_marker.lifetime.sec = (self.marker_duration_velocity // 1)
                new_marker.lifetime.nanosec = (self.marker_duration_velocity % 1) * int(1e9)
                
                self.get_logger().info(f"ID: {marker.id}, Speed: {marker.text}")
            else:
                new_marker.lifetime.sec = (self.marker_duration // 1)
                new_marker.lifetime.nanosec = (self.marker_duration % 1) * int(1e9)
#         
            extended_markers.markers.append(new_marker)

        self.marker_pub.publish(extended_markers)


def main(args=None):
    rclpy.init(args=args)
    radar_visualizer = RadarVisualizer()
    rclpy.spin(radar_visualizer)
    radar_visualizer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
