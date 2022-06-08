"""
Print an ever green tree like the one below of a given
size

    *
   ***
  *****
 *******
*********
   ***
   ***
   
"""

height = int(input("Enter height => "))

i = 1
line = "*"
num_spaces = height - 1

while i <= height:
    print (" "*num_spaces+line)
    num_spaces -= 1
    i += 1
    line += "**"
    
## Print tree trunk, subtracting 5 because we add stars
## one extra time, plus the three stars we print
## Modify this to print height/2 times the trunk
    
num_spaces = (len(line)-5)//2
print (" "*num_spaces + "***")
print (" "*num_spaces + "***")
