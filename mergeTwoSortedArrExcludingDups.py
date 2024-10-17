a = [1,2,3,4,4,5,6,8,9]
b = [4,4,5,5,6,10,12,13,13,14]

#Assume the arrays are sorted first
def merge(array1: list[int], array2: list[int]) -> list[int]:
    it1 = 0
    it2 = 0
    merged = []
    last = max(array1[0], array2[0])
    while it1 < len(array1) and it2 < len(array2):
        if a[it1] < b[it2]:
            if a[it1] != last:
                merged.append(a[it1])
                last = a[it1]
            it1 += 1
        elif a[it1] > b[it2]:
            if b[it2] != last:
                merged.append(b[it2])
                last = b[it2]
            it2 += 1
        elif a[it1] == b[it2]:
            if a[it1] != last:
                merged.append(a[it1])
                last = a[it1]
            it1 += 1
            it2 += 1
    
    while it2 < len(array2):
        if (b[it2] != merged[len(merged) - 1]):
            merged.append(b[it2])
        it2 += 1
        
    while it1 < len(array1):
        if (a[it1] != merged[len(merged) - 1]):
            merged.append(a[it1])
        it1 += 1
    return merged

print(merge(a,b))