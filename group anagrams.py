from collections import defaultdict
def groupAnagrams(strs):
    anagrams = defaultdict(list) 
    for s in strs:
        s1 = ''.join(sorted(s)) 
        anagrams[s1].append(s)  
    return list(anagrams.values()) 
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  
print(groupAnagrams([""]))  
print(groupAnagrams(["a"])) 
print(groupAnagrams(["abc", "bca", "cab", "xyz", "zyx", "yxz"])) 
print(groupAnagrams(["abc", "def", "ghi"]))  
