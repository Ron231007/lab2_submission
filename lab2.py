import statistics

def DisplayMenu():
    print("Enter some numbers separated by commas (e.g. 5, 67,37)")

def get_user_input():
    nums= input("Numbers:")
    str_nums= nums.split(",")

    for i in range(len(str_nums)):
        str_nums[i] = float(str_nums[i])
    
    return str_nums

def min_max_temperature(temp):
    return [int(min(temp)), int(max(temp))]

def average_temperature(temp):
    sum =0
    for x in (temp):
        sum += x
    
    return (sum/len(temp))

def calc_median_temperature(temp):
   return statistics.median(temp)
   
   
    # temp.sort()
    # iseven = len(temp)%2 ==0
    # middle = len(temp) //2
    
    # if(iseven):
    #    return round((temp[middle] + temp[middle +1])/2,2)
    
    # else:
    #     return temp[middle]


