the_mask = 8 # my bit - nr 3
flag_register = 0b0000_0000_0000_0000

# Set bit:
# flag_register = flag_register | the_mask
flag_register |= the_mask

# Reset bit:
# flag_register = flag_register & ~the_mask
flag_register &= ~the_mask

# Negate your bit:
# flag_register = flag_register ^ the_mask
flag_register ^= the_mask

# print state o the bit
if flag_register & the_mask:
    print("My bit is set.")
else:
    print("My bit is reset.")