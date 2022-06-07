def merge(lArr, rArr):
    rightFirst = rArr[0]
    leftLast = lArr[len(lArr) - 1]
    change = rightFirst - leftLast
    # print(lArr)
    # print(rArr)
    if change > 0 :
        # print("Increasing")
        return 'I', False, lArr[0]
    else :
        # print("Decreasing")
        return 'D', False, rArr[-1]
 

def Divide(data_set, status, break_chain, val):

    length = len(data_set) 
    if length <= 1:
        return status, break_chain, val
    
    if break_chain:
         return status, break_chain, val
    
    lArr = data_set[:length//2]
    rArr = data_set[length//2:]
    
    lstatus, break_chain, val = Divide(lArr, status, break_chain, val)
    rstatus, break_chain, val = Divide(rArr, status, break_chain, val)
    
    if lstatus != None and rstatus != None:
        if lstatus != rstatus:
            if lstatus == 'I':
                return lstatus, True, max(lArr[-1],rArr[0])
            else:
                return lstatus, True, min(lArr[-1],rArr[0])
    
    cur_status, break_chain, val = merge(lArr, rArr)
    return  cur_status, break_chain, val
    
# strict cases
# data_set = [3, 5, 7, 9, 11, 13, 15, 17]
# data_set = [17, 15, 13, 11, 9, 7, 5, 3]

# max - min cases
# data_set = [13, 15, 17, 19, 17, 15, 13, 11]
# data_set = [23, 21, 19, 17, 19, 21, 23, 25, 27]
data_set = [1, 2, 3, 1]

# assuming minimum val is to be printed 
# if breakchain is true, minima or maxima is present else it's either strictly Inc/Dec
status, breakChain, val = Divide(data_set, None, False, None)
# print(status, breakChain, min_flag, val)

if breakChain:
    if status == 'I':
        print('Maxima:', val)
    else:
        print('Minima:', val)
else:
    if status == 'I':
        print('Strictly Increasing:', val)
    else:
        print('Strictly Decreasing:', val)
