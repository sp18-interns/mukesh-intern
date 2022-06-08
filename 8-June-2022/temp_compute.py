"""
Want to find out average temperature for each decade
and store in a list


total = 0
decades = []
count_years = 0
in a loop:
    if a new decade has started:
        put the old total in the list decades
        total = 0
        ###What to do here????
    add 1 to count_years
    add temperature values

add the last total to the decades list

"""



tempdata = [(1956,50.9), (1957,50.8), (1958,49.2), (1959,52.9), (1960,50.3), (1961,53.8), (1962,50.9), (1963,56.0), (1964,49.9), (1965,50.0), (1966,49.5), (1967,52.2), (1968,54.1), (1969,51.6), (1970,54.3), (1971,57.0), (1972,47.4), (1973,53.3), (1974,46.2), (1975,54.0), (1976,47.2), (1977,48.9), (1978,48.9), (1979,51.3), (1980,49.9), (1981,47.9), (1982,51.3), (1983,52.5), (1985,51.9), (1986,50.6), (1987,48.2), (1988,48.5), (1989,52.4), (1990,54.4), (1991,53.3), (1992,47.3), (1993,49.5), (1994,51.3), (1995,55.7), (1996,51.1), (1997,50.0), (1998,52.7), (1999,50.3), (2000,51.9), (2001,54.1), (2002,49.9), (2003,49.6), (2004,51.2), (2005,52.4), (2006,49.8), (2007,57.7), (2008,49.8), (2010,51.9), (2011,53.4), (2012,54.9), (2013,53.9), (2014,55.4)]


### This program is not complete, we need to add more to it
i = 0
totaltemp = 0
decades = []
while i < len(tempdata):
    temp = tempdata[i][1]
    year = tempdata[i][0]
    ##check if a new decade has started
    if year%10 == 0:
        decades.append(totaltemp)
        totaltemp = 0
    totaltemp  += temp
    i += 1
    
decades.append(totaltemp)    
print ("Temperates in Troy", decades)
