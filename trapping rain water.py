def ctrapped_water(bars):
    if not bars:
        return 0
    
    start, end = 0, len(bars) - 1
    max_left, max_right = bars[start], bars[end]
    total_water = 0
    
    while start < end:
        if bars[start] < bars[end]:
            start += 1
            max_left = max(max_left, bars[start])
            total_water += max_left - bars[start]
        else:
            end -= 1
            max_right = max(max_right, bars[end])
            total_water += max_right - bars[end]
    
    return total_water

print(ctrapped_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  
print(ctrapped_water([4, 2, 0, 3, 2, 5])) 
print(ctrapped_water([1, 1, 1]))  
print(ctrapped_water([5]))  
print(ctrapped_water([2, 0, 2]))  
print(ctrapped_water([0, 0, 0]))  
print(ctrapped_water([5, 4, 3, 2, 1])) 
print(ctrapped_water([1, 2, 3, 4, 5]))  
