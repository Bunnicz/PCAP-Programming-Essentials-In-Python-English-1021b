blocks = int(input("Enter the number of blocks: "))
height = 0
#
# Write your code here.
#	
while height+1 <= blocks:
    blocks -= height+1
    height+=1

print("The height of the pyramid:", height, "\nRemaining blocks:", blocks, "\nBlocks needed for next layer:", height+1-blocks)
