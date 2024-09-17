class Robot:
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.position = [0, 0]  # Starts at (0, 0)

    def move(self, direction, steps, occupied_positions):
        directions = {
            'N': (-1, 0),  # Move up (negative row)
            'S': (1, 0),   # Move down (positive row)
            'E': (0, 1),   # Move right (positive column)
            'W': (0, -1)   # Move left (negative column)
        }
        
        if direction not in directions:
            raise ValueError("Invalid direction. Must be one of 'N', 'S', 'E', 'W'")
        
        for _ in range(steps):
            new_position = [
                self.position[0] + directions[direction][0],
                self.position[1] + directions[direction][1]
            ]
            
            if tuple(new_position) in occupied_positions:
                print(f"Robot {self.robot_id} stopped before reaching occupied cell {new_position}.")
                break
            
            self.position = new_position

    def get_position(self):
        return tuple(self.position)

class Terrain:
    def __init__(self):
        self.robots = {}
    
    def add_robot(self, robot_id):
        if robot_id in self.robots:
            raise ValueError(f"Robot with ID {robot_id} already exists.")
        self.robots[robot_id] = Robot(robot_id)
    
    def move_robot(self, robot_id, command):
        if robot_id not in self.robots:
            raise ValueError(f"No robot with ID {robot_id} exists.")
        
        direction = command[0]
        steps = int(command[1])
        
        occupied_positions = {robot.get_position() for rid, robot in self.robots.items() if rid != robot_id}
        
        self.robots[robot_id].move(direction, steps, occupied_positions)

    def get_robot_position(self, robot_id):
        if robot_id not in self.robots:
            raise ValueError(f"No robot with ID {robot_id} exists.")
        return self.robots[robot_id].get_position()

