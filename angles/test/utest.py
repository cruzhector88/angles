#!/usr/bin/env python
from angles import *
import sys
import unittest
from math import pi, fabs

## A sample python unit test
class TestAngles(unittest.TestCase):
    def test_shortestDistanceWithLimits(self):
        result, shortest_angle = shortest_angular_distance_with_limits(-0.5, 0.5,-0.25,0.25)
        self.assertFalse(result)

        result, shortest_angle = shortest_angular_distance_with_limits(-0.5, 0.5,0.25,0.25)
        self.assertFalse(result)

        result, shortest_angle = shortest_angular_distance_with_limits(-0.5, 0.5,0.25,-0.25)
        self.assertTrue(result)
        self.assertAlmostEqual(shortest_angle, -2*pi+1.0)

        result, shortest_angle = shortest_angular_distance_with_limits(0.5, 0.5,0.25,-0.25)
        self.assertTrue(result)
        self.assertAlmostEqual(shortest_angle, 0)

        result, shortest_angle = shortest_angular_distance_with_limits(0.5, 0,0.25,-0.25)
        self.assertFalse(result)
        self.assertAlmostEqual(shortest_angle, -0.5)

        result, shortest_angle = shortest_angular_distance_with_limits(-0.5, 0,0.25,-0.25)
        self.assertFalse(result)
        self.assertAlmostEqual(shortest_angle, 0.5)

        result, shortest_angle = shortest_angular_distance_with_limits(-0.2,0.2,0.25,-0.25)
        self.assertFalse(result)
        self.assertAlmostEqual(shortest_angle, -2*pi+0.4)

        result, shortest_angle = shortest_angular_distance_with_limits(0.2,-0.2,0.25,-0.25)
        self.assertFalse(result)
        self.assertAlmostEqual(shortest_angle,2*pi-0.4)

        result, shortest_angle = shortest_angular_distance_with_limits(0.2,0,0.25,-0.25)
        self.assertFalse(result)
        self.assertAlmostEqual(shortest_angle,2*pi-0.2)

        result, shortest_angle = shortest_angular_distance_with_limits(-0.2,0,0.25,-0.25)
        self.assertFalse(result)
        self.assertAlmostEqual(shortest_angle,-2*pi+0.2)

        result, shortest_angle = shortest_angular_distance_with_limits(-0.25,-0.5,0.25,-0.25)
        self.assertTrue(result)
        self.assertAlmostEqual(shortest_angle,-0.25)

        result, shortest_angle = shortest_angular_distance_with_limits(-0.25,0.5,0.25,-0.25)
        self.assertTrue(result)
        self.assertAlmostEqual(shortest_angle,-2*pi+0.75)

        result, shortest_angle = shortest_angular_distance_with_limits(-0.2500001,0.5,0.25,-0.25)
        self.assertTrue(result)
        self.assertAlmostEqual(shortest_angle,-2*pi+0.5+0.2500001)

        result, shortest_angle = shortest_angular_distance_with_limits(-0.6, 0.5,-0.25,0.25)
        self.assertFalse(result)

        result, shortest_angle = shortest_angular_distance_with_limits(-0.5, 0.6,-0.25,0.25)
        self.assertFalse(result)

        result, shortest_angle = shortest_angular_distance_with_limits(-0.6, 0.75,-0.25,0.3)
        self.assertFalse(result)

        result, shortest_angle = shortest_angular_distance_with_limits(-0.6, pi*3.0/4.0,-0.25,0.3)
        self.assertFalse(result)

        result, shortest_angle = shortest_angular_distance_with_limits(-pi, pi,-pi,pi)
        self.assertTrue(result)
        self.assertAlmostEqual(shortest_angle,0.0)

    def test_normalize_angle_positive(self):
        self.assertAlmostEqual(0, normalize_angle_positive(0))
        self.assertAlmostEqual(pi, normalize_angle_positive(pi))
        self.assertAlmostEqual(0, normalize_angle_positive(2*pi))
        self.assertAlmostEqual(pi, normalize_angle_positive(3*pi))
        self.assertAlmostEqual(0, normalize_angle_positive(4*pi))

        self.assertAlmostEqual(0, normalize_angle_positive(-0))
        self.assertAlmostEqual(pi, normalize_angle_positive(-pi))
        self.assertAlmostEqual(0, normalize_angle_positive(-2*pi))
        self.assertAlmostEqual(pi, normalize_angle_positive(-3*pi))
        self.assertAlmostEqual(0, normalize_angle_positive(-4*pi))

        self.assertAlmostEqual(0, normalize_angle_positive(-0))
        self.assertAlmostEqual(3*pi/2, normalize_angle_positive(-pi/2))
        self.assertAlmostEqual(pi, normalize_angle_positive(-pi))
        self.assertAlmostEqual(pi/2, normalize_angle_positive(-3*pi/2))
        self.assertAlmostEqual(0, normalize_angle_positive(-4*pi/2))

        self.assertAlmostEqual(0, normalize_angle_positive(0))
        self.assertAlmostEqual(pi/2, normalize_angle_positive(pi/2))
        self.assertAlmostEqual(pi/2, normalize_angle_positive(5*pi/2))
        self.assertAlmostEqual(pi/2, normalize_angle_positive(9*pi/2))
        self.assertAlmostEqual(pi/2, normalize_angle_positive(-3*pi/2))

    def test_normalize_angle(self):
        self.assertAlmostEqual(0, normalize_angle(0))
        self.assertAlmostEqual(pi, normalize_angle(pi))
        self.assertAlmostEqual(0, normalize_angle(2*pi))
        self.assertAlmostEqual(pi, normalize_angle(3*pi))
        self.assertAlmostEqual(0, normalize_angle(4*pi))

        self.assertAlmostEqual(0, normalize_angle(-0))
        self.assertAlmostEqual(pi, normalize_angle(-pi))
        self.assertAlmostEqual(0, normalize_angle(-2*pi))
        self.assertAlmostEqual(pi, normalize_angle(-3*pi))
        self.assertAlmostEqual(0, normalize_angle(-4*pi))

        self.assertAlmostEqual(0, normalize_angle(-0))
        self.assertAlmostEqual(-pi/2, normalize_angle(-pi/2))
        self.assertAlmostEqual(pi, normalize_angle(-pi))
        self.assertAlmostEqual(pi/2, normalize_angle(-3*pi/2))
        self.assertAlmostEqual(0, normalize_angle(-4*pi/2))

        self.assertAlmostEqual(0, normalize_angle(0))
        self.assertAlmostEqual(pi/2, normalize_angle(pi/2))
        self.assertAlmostEqual(pi/2, normalize_angle(5*pi/2))
        self.assertAlmostEqual(pi/2, normalize_angle(9*pi/2))
        self.assertAlmostEqual(pi/2, normalize_angle(-3*pi/2))
 
    def test_shortest_angular_distance(self):
         self.assertAlmostEqual(pi/2, shortest_angular_distance(0, pi/2))
         self.assertAlmostEqual(-pi/2, shortest_angular_distance(0, -pi/2))
         self.assertAlmostEqual(-pi/2, shortest_angular_distance(pi/2, 0))
         self.assertAlmostEqual(pi/2, shortest_angular_distance(-pi/2, 0))

         self.assertAlmostEqual(-pi/2, shortest_angular_distance(pi, pi/2))
         self.assertAlmostEqual(pi/2, shortest_angular_distance(pi, -pi/2))
         self.assertAlmostEqual(pi/2, shortest_angular_distance(pi/2, pi))
         self.assertAlmostEqual(-pi/2, shortest_angular_distance(-pi/2, pi))

         self.assertAlmostEqual(-pi/2, shortest_angular_distance(5*pi, pi/2))
         self.assertAlmostEqual(pi/2, shortest_angular_distance(7*pi, -pi/2))
         self.assertAlmostEqual(pi/2, shortest_angular_distance(9*pi/2, pi))
         self.assertAlmostEqual(pi/2, shortest_angular_distance(-3*pi/2, pi))

         # Backside wrapping
         self.assertAlmostEqual(-pi/2, shortest_angular_distance(-3*pi/4, 3*pi/4))
         self.assertAlmostEqual(pi/2, shortest_angular_distance(3*pi/4, -3*pi/4))

    def test_two_pi_complement(self):
         epsilon = 1e-9
         self.assertAlmostEqual(two_pi_complement(0), 2*pi)
         self.assertAlmostEqual(two_pi_complement(2*pi), 0)
         self.assertAlmostEqual(two_pi_complement(-2*pi), 0)
         self.assertAlmostEqual(two_pi_complement(2*pi-epsilon), -epsilon)
         self.assertAlmostEqual(two_pi_complement(-2*pi+epsilon), epsilon)
         self.assertAlmostEqual(two_pi_complement(pi/2), -3*pi/2)
         self.assertAlmostEqual(two_pi_complement(pi), -pi)
         self.assertAlmostEqual(two_pi_complement(-pi), pi)
         self.assertAlmostEqual(two_pi_complement(-pi/2), 3*pi/2)

         self.assertAlmostEqual(two_pi_complement(3*pi), -pi)
         self.assertAlmostEqual(two_pi_complement(-3.0*pi), pi)
         self.assertAlmostEqual(two_pi_complement(-5.0*pi/2.0), 3*pi/2)

    def test_find_min_max_delta(self):
         epsilon = 1e-9
         # Straight forward full range
         flag, min_delta, max_delta = find_min_max_delta( 0, -pi, pi)
         self.assertTrue(flag)
         self.assertAlmostEqual(min_delta, -pi)
         self.assertAlmostEqual(max_delta, pi)

         # pi/2 Full Range
         flag, min_delta, max_delta = find_min_max_delta( pi/2, -pi, pi)
         self.assertTrue(flag)
         self.assertAlmostEqual(min_delta, -3*pi/2)
         self.assertAlmostEqual(max_delta, pi/2)

         # -pi/2 Full range
         flag, min_delta, max_delta = find_min_max_delta( -pi/2, -pi, pi)
         self.assertTrue(flag)
         self.assertAlmostEqual(min_delta, -pi/2)
         self.assertAlmostEqual(max_delta, 3*pi/2)

         # Straight forward partial range
         flag, min_delta, max_delta = find_min_max_delta( 0, -pi/2, pi/2)
         self.assertTrue(flag)
         self.assertAlmostEqual(min_delta, -pi/2)
         self.assertAlmostEqual(max_delta, pi/2)

         # pi/4 Partial Range
         flag, min_delta, max_delta = find_min_max_delta( pi/4, -pi/2, pi/2)
         self.assertTrue(flag)
         self.assertAlmostEqual(min_delta, -3*pi/4)
         self.assertAlmostEqual(max_delta, pi/4)

         # -pi/4 Partial Range
         flag, min_delta, max_delta = find_min_max_delta( -pi/4, -pi/2, pi/2)
         self.assertTrue(flag)
         self.assertAlmostEqual(min_delta, -pi/4)
         self.assertAlmostEqual(max_delta, 3*pi/4)

         # bump stop negative full range
         flag, min_delta, max_delta = find_min_max_delta( -pi, -pi, pi)
         self.assertTrue(flag)
         self.assertTrue((fabs(min_delta) <= epsilon and fabs(max_delta - 2*pi) <= epsilon) or (fabs(min_delta+2*pi) <= epsilon and fabs(max_delta) <= epsilon))
         self.assertAlmostEqual(min_delta, 0.0)
         self.assertAlmostEqual(max_delta, 2*pi)

         flag, min_delta, max_delta = find_min_max_delta(-0.25,0.25,-0.25)
         self.assertTrue(flag)
         self.assertAlmostEqual(min_delta, -2*pi+0.5)
         self.assertAlmostEqual(max_delta, 0.0)

         # bump stop positive full range
         flag, min_delta, max_delta = find_min_max_delta( pi-epsilon, -pi, pi)
         self.assertTrue(flag)
         #self.assertTrue((fabs(min_delta) <= epsilon and fabs(max_delta - 2*pi) <= epsilon) or (fabs(min_delta+2*pi) <= epsilon and fabs(max_delta) <= epsilon))
         self.assertAlmostEqual(min_delta, -2*pi+epsilon)
         self.assertAlmostEqual(max_delta, epsilon)

         # bump stop negative partial range
         flag, min_delta, max_delta = find_min_max_delta( -pi, -pi, pi)
         self.assertTrue(flag)
         self.assertAlmostEqual(min_delta, 0)
         self.assertAlmostEqual(max_delta, 2*pi)

         # bump stop positive partial range
         flag, min_delta, max_delta = find_min_max_delta( -pi/2, -pi/2, pi/2)
         self.assertTrue(flag)
         self.assertAlmostEqual(min_delta, 0.0)
         self.assertAlmostEqual(max_delta, pi)

         #Test out of range negative
         flag, min_delta, max_delta = find_min_max_delta( -pi, -pi/2, pi/2)
         self.assertFalse(flag)
         #Test out of range postive
         flag, min_delta, max_delta = find_min_max_delta( pi, -pi/2, pi/2)
         self.assertFalse(flag)

         # pi/4 Partial Range
         flag, min_delta, max_delta = find_min_max_delta( 3*pi/4, pi/2, -pi/2)
         self.assertTrue(flag)
         self.assertAlmostEqual(min_delta, -pi/4)
         self.assertAlmostEqual(max_delta, 3*pi/4)

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun('angles', 'test_python_angles', TestAngles)
