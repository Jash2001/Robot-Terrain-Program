from robot import Terrain

terrain = Terrain()

terrain.add_robot(1)
terrain.add_robot(2)

terrain.move_robot(1, "N4")
print(f"Robot 1 position: {terrain.get_robot_position(1)}")  

terrain.move_robot(2, "E3")
print(f"Robot 2 position: {terrain.get_robot_position(2)}")  

terrain.move_robot(1, "S1")
print(f"Robot 1 position: {terrain.get_robot_position(1)}")  

terrain.move_robot(2, "W2")
print(f"Robot 2 position: {terrain.get_robot_position(2)}")  

terrain.move_robot(1, "E3")
print(f"Robot 1 position after potential collision: {terrain.get_robot_position(1)}") 