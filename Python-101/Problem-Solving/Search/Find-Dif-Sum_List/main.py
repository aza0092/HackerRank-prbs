def find_pair_dif_sum_in_list(list1, target_dif_sum):
    set1 = set()
    count = 0
    for num in list1:
        if num + target_dif_sum in set1:
            #count += 1
            print(num, target_dif_sum + num)
        if num - target_dif_sum in set1:
            #count += 1
            print(num, num - target_dif_sum)
        set1.add(num)  # All target dif sum will be stored in set, if (num, target_dif_sum) pair make a sum dif in set, then we have a successful pair/count
    #print(count)
