# count how many deletes to make two strings anagrams
# the method works by removing all similar chars and only including the non-similar chars
def makeAnagram(a, b):
    for i in a:
        if i in b:
            b=b.replace(i,'',1)
            a=a.replace(i,'',1)
    return len(a)+len(b)
	
# Alternative solution using sets
def number_needed(a, b):
	"""
	create set with a single occurance of the common characters between the two strings. 
	Then iterate over each character of ab_intersection to determine the least number in either string. 
	Summing the minimum occurance of common characters allows you to calculate how many characters to remove.
	"""
    ab_intersection = set(a).intersection(b)
    anagram = sum(min(a.count(char),b.count(char)) for char in ab_intersection)
    return(len(a)+len(b)-2*anagram)

a = input().strip()
b = input().strip()

print(number_needed(a, b))
