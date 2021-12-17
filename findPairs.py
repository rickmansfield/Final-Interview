def findPairs(array, v):
    results = []
    
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == v:
                results.append([array[i], array[j]])
            else:
                continue
                
    return results

a = [3, 5, 2, -4, 8, 11]

print(findPairs(a, 7))