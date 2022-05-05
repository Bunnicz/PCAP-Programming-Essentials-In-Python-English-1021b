How do we deal with single bits?

We'll now show you what you can use bitwise operators for. Imagine that you're a developer obliged to write an important piece of an operating system. You've been told that you're allowed to use a variable assigned in the following way:
flag_register = 0x1234


The variable stores the information about various aspects of system operation. Each bit of the variable stores one yes/no value. You've also been told that only one of these bits is yours - the third (remember that bits are numbered from zero, and bit number zero is the lowest one, while the highest is number 31). The remaining bits are not allowed to change, because they're intended to store other data. Here's your bit marked with the letter x:
flag_register = 0000000000000000000000000000x000


You may be faced with the following tasks:

1. Check the state of your bit - you want to find out the value of your bit; comparing the whole variable to zero will not do anything, because the remaining bits can have completely unpredictable values, but you can use the following conjunction property:
x & 1 = x
x & 0 = 0


If you apply the & operation to the flag_register variable along with the following bit image:
00000000000000000000000000001000

(note the 1 at your bit's position) as the result, you obtain one of the following bit strings:

    00000000000000000000000000001000 if your bit was set to 1
    0000000000000000000000000000000 if your bit was reset to 0

Such a sequence of zeros and ones, whose task is to grab the value or to change the selected bits, is called a bit mask.

Let's build a bit mask to detect the state of your bit. It should point to the third bit. That bit has the weight of 23 = 8. A suitable mask could be created by the following declaration:
the_mask = 8



You can also make a sequence of instructions depending on the state of your bit i here it is:
if flag_register & the_mask:
    # My bit is set.
else:
    # My bit is reset.


2. Reset your bit - you assign a zero to the bit while all the other bits must remain unchanged; let's use the same property of the conjunction as before, but let's use a slightly different mask - exactly as below:
11111111111111111111111111110111


Note that the mask was created as a result of the negation of all the bits of the_mask variable. Resetting the bit is simple, and looks like this (choose the one you like more):
flag_register = flag_register & ~the_mask
flag_register &= ~the_mask



3. Set your bit - you assign a 1 to your bit, while all the remaining bits must remain unchanged; use the following disjunction property:
x | 1 = 1
x | 0 = x


You're now ready to set your bit with one of the following instructions:
flag_register = flag_register | the_mask
flag_register |= the_mask


4. Negate your bit - you replace a 1 with a 0 and a 0 with a 1. You can use an interesting property of the xor operator:
x ^ 1 = ~x
x ^ 0 = x


and negate your bit with the following instructions:
flag_register = flag_register ^ the_mask
flag_register ^= the_mask
