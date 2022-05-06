3.4.1.14 Points on a plane

LAB

Estimated time

30-60 minutes
Level of difficulty

Easy/Medium
Objectives

    improving the student's skills in defining classes from scratch;
    defining and using instance variables;
    defining and using methods.

Scenario

Let's visit a very special place - a plane with the Cartesian coordinate system (you can learn more about this concept here: https://en.wikipedia.org/wiki/Cartesian_coordinate_system).

Each point located on the plane can be described as a pair of coordinates customarily called x and y. We expect that you are able to write a Python class which stores both coordinates as float numbers. Moreover, we want the objects of this class to evaluate the distances between any of the two points situated on the plane.

The task is rather easy if you employ the function named hypot() (available through the math module) which evaluates the length of the hypotenuse of a right triangle (more details here: https://en.wikipedia.org/wiki/Hypotenuse) and here: https://docs.python.org/3.7/library/math.html#trigonometric-functions.

This is how we imagine the class:

    it's called Point;
    its constructor accepts two arguments (x and y respectively), both default to zero;
    all the properties should be private;
    the class contains two parameterless methods called getx() and gety(), which return each of the two coordinates (the coordinates are stored privately, so they cannot be accessed directly from within the object);
    the class provides a method called distance_from_xy(x,y), which calculates and returns the distance between the point stored inside the object and the other point given as a pair of floats;
    the class provides a method called distance_from_point(point), which calculates the distance (like the previous method), but the other point's location is given as another Point class object;

Complete the template we've provided in the editor and run your code and check whether your output looks the same as ours.
Expected output

1.4142135623730951
1.4142135623730951