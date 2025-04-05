import math
import pytest
from cricketpositionguesser.polar_coordinate import PolarCoordinate
from cricketpositionguesser.cartesian_coordinate import CartesianCoordinate

def test_polar_to_cartesian():
    polar = PolarCoordinate(10, 45)
    cartesian = polar.to_cartesian()
    assert math.isclose(cartesian.x, 7.071, rel_tol=1e-3)
    assert math.isclose(cartesian.y, 7.071, rel_tol=1e-3)

def test_distance_to_same_point():
    polar1 = PolarCoordinate(10, 45)
    polar2 = PolarCoordinate(10, 45)
    assert math.isclose(polar1.distance_to(polar2), 0.0, rel_tol=1e-3)

def test_distance_to_different_points():
    polar1 = PolarCoordinate(10, 0)
    polar2 = PolarCoordinate(10, 90)
    assert math.isclose(polar1.distance_to(polar2), 14.142, rel_tol=1e-3)

def test_polar_to_cartesian_zero_distance():
    polar = PolarCoordinate(0, 45)
    cartesian = polar.to_cartesian()
    assert cartesian.x == 0
    assert cartesian.y == 0

def test_distance_to_zero_distance_point():
    polar1 = PolarCoordinate(10, 45)
    polar2 = PolarCoordinate(0, 0)
    assert math.isclose(polar1.distance_to(polar2), 10.0, rel_tol=1e-3)