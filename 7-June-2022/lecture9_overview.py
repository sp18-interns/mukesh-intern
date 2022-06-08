"""
How to construct loops

<make sure the stopping condition is not true
at first>
while <stopping condition is not true>:
    repeat some stuff
    <make sure the stopping condition eventually
    becomes true>

Accumulation of values from a list

initial value for accumulation of values (often zero)
while loop:
   <>
   accumulate values to this variable
   
<compute what you need with the accumulation variable>

Ending on a different condition

not_finished = True
while not_finished:
    ##do something
    
    if <something happens>:
        not_finished = False

"""


i = 1
while (i < 10):
    print (i)
    i += 1

print()   
    
i=0
while (i<10):
    i += 1
    print (i)

print()   
    
i = 1
while (i < 10):
    print (i)
    i += 2



citadel = ['CowboyRick', 'EvilMorty', 'Rick176B', 'SimpleRick', 'AlienMorty', 'RickMorty']


## count 0 up to but not including len(list)
## to index the list properly

i = 0
while i < len(citadel):
    item = citadel[i]
    if item.find("Rick") != -1:
        print ( item )
    i += 1
    
    
co2_levels = [ (2001, 320.03), (2003, 322.16), (2004, 328.07),\
               (2006, 323.91), (2008, 341.47), (2009, 348.92),\
               (2010, 357.29), (2011, 363.77), (2012, 361.51),\
               (2013, 382.47) ]
    
i = 0
while i < len(co2_levels):
    item = co2_levels[i]
    print ( item[0], item[1] )
    i += 1
    

i=10
while i > 0:
    print (i)
    i -= 1
    
i = -1
while i >= -len(co2_levels):
    item = co2_levels[i]
    print ( item[0], item[1] )    
    i -= 1
    
i = len(co2_levels)-1
while i >= 0:
    item = co2_levels[i]
    print ( item[0], item[1] )    
    i -= 1    