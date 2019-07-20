def count_substring(string, sub_string):
  if (len(string) >= 1 and len(string) <= 200):
    counter =0
    sub_len = len(sub_string)
    for i in range(len(string)):
      if (string.find(sub_string)!=-1): #if sub is found
        index = string.find(sub_string) #get the index at which the sub is found
        counter +=1 
        string = string[((index+sub_len)-1):] #trim string at sub index
  return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)