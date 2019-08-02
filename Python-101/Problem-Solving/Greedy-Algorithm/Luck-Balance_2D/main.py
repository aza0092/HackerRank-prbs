def luckBalance(k, contests):
    # sort from greatest luck to least luck
    contests.sort(reverse=True)  # Sort from big to small
    luck = 0
    not_important = 0

    for contest in contests:
        if contest[1] == not_important:
            luck += contest[0]
        elif k > 0:  # Didn't run out of most k'th competitions she can lose
            luck += contest[0]
            k -= 1
        else:
            luck -= contest[0]  # Won a competition, thus luck dec

    return luck