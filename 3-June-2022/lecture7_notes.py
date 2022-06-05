"""
All course notes are at:

http://www.cs.rpi.edu/~sibel/csci1100/fall2017

Learn how to use Piazza for questions

Exam #1 coming, next monday
6-7:30PM
(accommodation: 4:30, location to be sent)

Exam practice questions will be posted on Piazza

Data types:

int
   values: 1,2,3,-4,...
   
   functions: float(), round(), abs(), 
   str(), min(), max().
   +.-.*,/,//, %, etc.

float
   values: 1.2, 2.3, -1.3, 2.0
   
   functions: same as int, int(), str()

string
   values: 'a', 'bcd', ...
   
   functions: len(), .upper(), .lower(),
   .find(), .count(), .title(), .capitalize(),
   .format(), .strip(), .replace(), int(), float()

Boolean
   values: True, False

   functions(kind of): and, or, not
   
All functions so far, return a value!

New data type: list, contains multiple values
of any type

Define a list by square brackets

x = [1,4,5]

Find a single item by indexing square
brackets

x[1]

Valid indices:  0 -> len(list)-1
                -len(list) <- -1
                
0 is the first item
len(list)-1 is the last item

in reverse

-1 is the last item
-len(list) is the first item

Functions that return a single value:

    len(), 
    min(), max(), sum()  ##these require the same value that can be compared
    
New type of function that changes a list
but does not return a value

    .sort(), .append(), .remove(), .insert()
    
***Functions that return a value and change
the list

    .pop()
    
Call these but do not assign them to a variable

x.sort() -- correct

a = x.sort() -- incorrect


"""


temp = [89, 87, 87, 81, 68]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

print ("There are", len(temp), "items in the list")

avg_temp = sum(temp)/len(temp)

print ("Average temperature this week is", avg_temp)
print ("Temperature on {0}: {1}".format( days[0], temp[0] ))
print ("Temperature on {0}: {1}".format( days[1], temp[1] ))

degree_difference = temp[0]-temp[1]

if temp[1] > temp[0]:
    print ("Tomorrow is going to be hotter than today")
elif temp[0] > temp[1]:
    print ("Tomorrow is going to be {} degrees cooler than today".format( degree_difference))
else:
    print ("Tomorrow will be the same temperature as today")
