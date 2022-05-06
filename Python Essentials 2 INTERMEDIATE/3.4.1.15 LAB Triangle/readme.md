# 3.4.1.15 Triangle

LAB

Estimated time
30-60 minutes

Level of difficulty
Medium

Objectives

- improving the student's skills in defining classes from scratch;
- using composition.

## Scenario

Now we're going to embed the Point class (see Lab 3.4.1.14) inside another class. Also, we're going to put three points into one class, which will let us define a triangle. How can we do it?

The new class will be called Triangle and this is the list of our expectations:

- the constructor accepts three arguments - all of them are objects of the Point class;
- the points are stored inside the object as a private list;
- the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points; the perimeter is a sum of all legs' lengths (we mention it for the record, although we are sure that you know it perfectly yourself.)

Complete the template we've provided in the editor. Run your code and check whether the evaluated perimeter is the same as ours.

Below you can copy the Point class code we used in the previous lab:
```
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
```
## Expected output
```
3.414213562373095
```
