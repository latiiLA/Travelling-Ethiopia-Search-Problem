#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path

class PathfindingNode:
    def init(self):
        rospy.init_node('pathfinding_node', anonymous=True)
        self.path_pub = rospy.Publisher('/path', Path, queue_size=10)
        self.start_state = (0, 0)
        self.goal_state = (2, 2)
        self.states = {
            (0, 0): [(1, 1)],
            (1, 1): [(2, 2)],
            (2, 2): []
        }
        self.path = Path()
        self.path.header.frame_id = "map"
        self.search()

    def search(self):
        from collections import deque

        queue = deque([self.start_state])
        visited = set()
        parent = {self.start_state: None}

        while queue:
            current = queue.popleft()
            if current == self.goal_state:
                self.construct_path(current, parent)
                return

            for neighbor in self.states.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

    def construct_path(self, state, parent):
        path = []
        while state is not None:
            path.append(state)
            state = parent[state]

        path.reverse()

        for x, y in path:
            pose = PoseStamped()
            pose.pose.position.x = x
            pose.pose.position.y = y
            self.path.poses.append(pose)

        self.path_pub.publish(self.path)


if __name__ == '__main__':
    try:
        PathfindingNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
