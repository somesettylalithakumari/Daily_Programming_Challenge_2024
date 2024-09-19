from itertools import permutations
def permu(s):
    u = set(permutations(s))
    res = [''.join(p) for p in u]
    return res

print(permu("abc"))  
print(permu("aab"))  
print(permu("aaa"))  
print(permu("a"))    
print(permu("abcd")) 
