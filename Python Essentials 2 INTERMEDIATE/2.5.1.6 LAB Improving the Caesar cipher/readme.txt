2.5.1.6 LAB: Improving the Caesar cipher

LAB

Estimated time

30-90 minutes
Level of difficulty

Hard
Pre-requisites

Module 1.11.1.1, Module 1.11.1.2
Objectives

    improving the student's skills in operating with strings;
    converting characters into ASCII code, and vice versa.

Scenario

You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.

The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

    asks the user for one line of text to encrypt;
    asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
    prints out the encoded text. 

Test your code using the data we've provided.
Test data

Sample input:
abcxyzABCxyz 123
2

Sample output:
cdezabCDEzab 123

Sample input:
The die is cast
25

Sample output:
Sgd chd hr bzrs