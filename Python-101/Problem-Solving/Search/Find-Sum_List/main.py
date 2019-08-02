def find_pair_sum_in_list(list1, target_sum):
    set1 = set()
    for num in list1:
        if target_sum - num in set1:
            print(num, target_sum - num)
        else:
            set1.add(num)  # All target sum will be stored in set, if (n,k) pair make a sum in set, then we have a pair
