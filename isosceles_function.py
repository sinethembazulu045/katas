# iscosceles
def isoscelesTri(raw_num):
    isosceles_raw = ''
    raw_num = 2*raw_num -2

    for raw_count in range(0,raw_num):
        for column in range(0,raw_num):
            print(end=" ")
        raw_num = raw_num-1
        for column in range(0,raw_count+1):
            print("#", end=" ")
        print("\r")
    return isosceles_raw
check= isoscelesTri(3)
print(check)  
