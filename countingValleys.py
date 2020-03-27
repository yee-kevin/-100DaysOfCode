# Complete the countingValleys function below.
def countingValleys(n, s):
    seq = []
    alti = 0
    # Create list of altitudes
    for char in s:
        if char == 'D':
            alti -= 1
            seq.append(alti)
        if char == 'U':
            alti += 1
            seq.append(alti)
    
    # Find the index of 0's to find when he returns to sea level
    zero_idx = []
    for idx, num in enumerate(seq):
        if num == 0:
            zero_idx.append(idx)
    
    # For each index of 0's, check if he just exited a valley to reach sea level 
    valley_cnt = 0
    for idx in zero_idx:
        if seq[idx-1] < 0:
            valley_cnt +=1
                
    return valley_cnt
    
print(countingValleys(8, 'DDUUUUDD'))
print(countingValleys(8, 'DUDUDDUU'))
print(countingValleys(8, 'UDDDUDUU'))