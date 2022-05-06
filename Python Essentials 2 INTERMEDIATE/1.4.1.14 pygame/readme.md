# How to use pip: a simple test program
Now that pygame is finally accessible, we can try to use it in a very simple test program. Let’s comment on it briefly.
- line 1: import pygame and let it serve us;
- line 3: the program will run as long as the run variable is True;
- lines 4 and 5: determine the window's size;
- line 6: initialize the pygame environment;
- line 7: prepare the application window and set its size;
- line 8: make an object representing the default font of size 48 points;
- line 9: make an object representing a given text – the text will be anti-aliased (True) and white (255,255,255)
- line 10: insert the text into the (currently invisible) screen buffer;
- line 11: flip the screen buffers to make the text visible;
- line 12: the pygame main loop starts here;
- line 13: get a list of all pending pygame events;
- lines 14 through 16: check whether the user has closed the window or clicked somewhere inside it or pressed any key;
- line 15: if yes, stop executing the code.
