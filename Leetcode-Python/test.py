#### FIND DUPLICATES
def find_duplicates(nums:list):
    seen = {}
    arr = []
    for num in nums:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    for key, val in seen.items():
        if val > 1: # duplicates
            arr.append(key)
    return arr if arr else []
            

print(find_duplicates([1, 1, 2, 2, 3]))

#### GROUP ANAGRAMS
from collections import defaultdict
def group_anagrams(arr:list):
    anagram_list = defaultdict(list)
    
    for word in arr:
        sorted_word = ''.join(sorted(word))
        anagram_list[sorted_word].append(word)
    for key, value in anagram_list.items():
        print(f'{key} :- {value}')
        
    return list(anagram_list.items())

print("1st set:")
output = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print("\nGrouped Anagrams:", output)



####  DIVIDED STRING
def divideString(s,k,fill):
    main_list:list = []
    i = 0
    while i < len(s):
        chunk = s[i:i+k]
        print(chunk)
        if len(chunk) < k:
            chunk += fill * (k - len(chunk)) 
        main_list.append(chunk)
        i += k
        
    return main_list
    
s ="abcdefghi"
k = 3
fill = 'x'
divideString(s=s, k=k, fill=fill)
# Output: ["abc","def","ghi"]
