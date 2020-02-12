# concanetion of lists

def concanetion(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    combo = []
    
    
    if len1 > len2:
        for i in range(len2):
            combo.append(list1[i])
            combo.append(list2[i])
        # Now add remaining elements from list1
        for remaining_index in range(i,len1):
            combo.append(list1[remaining_index])
    elif len1 < len2:
        i = 0
        for i in range(len1):
            combo.append(list1[i])
            combo.append(list2[i])
        for remaining_index in range(i,len2):
            combo.append(list2[remaining_index])
    else:
        if len1 == len2:
            for i in range(len1):
                combo.append(list1[i])
                combo.append(list2[i])
    return combo

check = concanetion([2,4,6], [5,4,3])
print(check)
