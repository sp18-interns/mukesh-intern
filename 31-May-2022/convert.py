

def convert(miles_per_hour):
    km_per_day = miles_per_hour * 24 * 1.60934
    return km_per_day

val = 10
val2 = convert(val)
print ("{0:.1f} miles/hour is {1:.1f} km/day".format(val,val2))
       