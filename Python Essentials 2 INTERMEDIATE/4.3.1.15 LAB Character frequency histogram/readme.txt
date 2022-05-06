4.3.1.15 LAB: Character frequency histogram

LAB

Estimated time

30-60 minutes
Level of difficulty

Medium
Objectives

    improving the student's skills in operating with files (reading)
    using data collections for counting numerous data.

Scenario

A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

    asks the user for the input file's name;
    reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
    prints a simple histogram in alphabetical order (only non-zero counts should be presented)

Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:
aBc

samplefile.txt

the expected output should look as follows:
a -> 1
b -> 1
c -> 1

output

Tip: We think that a dictionary is a perfect data collection medium for storing the counts. The letters may be keys while the counters can be values.