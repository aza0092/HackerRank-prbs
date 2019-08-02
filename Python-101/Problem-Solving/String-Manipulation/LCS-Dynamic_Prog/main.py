def LCS(s1, s2):
    s1_length, s2_length = len(s1), len(s2)
    lcs = [[0] * (s2_length + 1) for _ in range(s1_length + 1)]  # Create 2D list that has size+1 of both strs storing 0's 

    for i, current_char_s1 in enumerate(s1):  # Current index, and the value at that index
        for j, current_char_s2 in enumerate(s2):
            if current_char_s1 == current_char_s2:
                lcs[i][j] = lcs[i - 1][j - 1] + 1  # add 1 to the current value from the previous char in s2 \
            else:
                lcs[i][j] = max(lcs[i][j - 1],
                                lcs[i - 1][j])  # get the max value from prev char in s1 and next char in s2 /

    return lcs[s1_length - 1][s2_length - 1]  # Trace back and get the LCS
