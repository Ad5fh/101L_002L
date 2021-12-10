import math

def Total(list):
    try:
        if len(list) ==0:
            raise ValueError
        else:
            return sum(list)
    except ValueError:
        return 0
        
def Average(list):
    if len(list)==0:
        return math.nan
    else:
        return float(sum(list)/len(list))

def Median (list):
    if len(list)==0:
            raise ValueError
    else:
        list.sort()
        median=int(len(list)/2)
        if len(list)%2 ==0:
            return (list[median] + list[median-1])/2
        else:
            return (list[median])
