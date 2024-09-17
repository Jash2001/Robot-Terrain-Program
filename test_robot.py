import pytest 
from robot import Terrain

@pytest.fixture
def setup_terrain():
    terrain = Terrain()
    terrain.add_robot(1)
    terrain.add_robot(2)
    return terrain

def test_robot_1_move_N4(setup_terrain):
    terrain = setup_terrain
    terrain.move_robot(1, "N4")
    assert terrain.get_robot_position(1) == (-4, 0)

def test_robot_2_move_E3(setup_terrain):
    terrain = setup_terrain
    terrain.move_robot(2, "E3")
    assert terrain.get_robot_position(2) == (0, 3)

def test_robot_1_move_S1(setup_terrain):
    terrain = setup_terrain
    terrain.move_robot(1, "N4")
    terrain.move_robot(1, "S1")
    assert terrain.get_robot_position(1) == (-3, 0)

def test_robot_2_move_W2(setup_terrain):
    terrain = setup_terrain
    terrain.move_robot(2, "E3")
    terrain.move_robot(2, "W2")
    assert terrain.get_robot_position(2) == (0, 1)

def test_collision_robot_1_E3(setup_terrain):
    terrain = setup_terrain
    terrain.move_robot(1, "N4")
    terrain.move_robot(1, "S1")
    terrain.move_robot(2, "E3")  
    terrain.move_robot(2, "W2") 
    terrain.move_robot(1, "E3")  
    assert terrain.get_robot_position(1) == (-3, 3)  
