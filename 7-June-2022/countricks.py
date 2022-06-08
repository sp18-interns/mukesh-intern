citadel = ['CowboyRick', 'EvilMorty', 'Rick176B', 'SimpleRick', 'AlienMorty', 'RickMorty']

#count Rick's and Morty's

i = 0
cntr = 0
cntm = 0


## Still does not handle "RickMorty", which should be 
## a Morty. You can use .endswith() string function to
## to check for this. How?

while i < len(citadel):
    item = citadel[i]
    if item.find('Rick') != -1:
        cntr += 1
    if item.find('Morty') != -1:
        cntm += 1
    i+= 1
    
print ("{} Ricks and {} Mortys".format(cntr, cntm))