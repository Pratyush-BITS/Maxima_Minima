def merge(lArr, rArr, status):
    rightFirst = rArr[0]
    leftLast = lArr[len(lArr) - 1]
    change = rightFirst - leftLast
    print(lArr)
    print(rArr)
    if change > 0 :
        print("Increasing")
        return 'I'
    else :
        print("Decreasing")
        return 'D'
 

def Divide(data_set, status):

    length = len(data_set) 
    if length <= 1:
        return 0
    
    lArr = data_set[:length//2]
    rArr = data_set[length//2:]
    
    lstatus = Divide(lArr, status)
    rstatus = Divide(rArr, status)
    
    if lstatus != rstatus:
        if status == lstatus:
            min = 0
        

    #merging function, will returns the minima, maxima, times the array switched 
    #it's direcion and type in future
    curStatus = merge(lArr, rArr, status)
    return curStatus
    # return minIndex, maxIndex, switchCount, arrType
    
        
# data_set = [3, 5, 7, 9, 11, 13, 15, 17]
# data_set = [17, 15, 13, 11, 9, 7, 5, 3]
data_set = [13, 15, 17, 19, 17, 15, 13, 11]
# data_set = [3, 5, 7, 9, 11, 13, 15, 17]
Divide(data_set, None)