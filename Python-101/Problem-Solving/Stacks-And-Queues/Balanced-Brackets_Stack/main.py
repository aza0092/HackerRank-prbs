def check_str(string):
    stack = []
    table = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    for char in string:
        if not stack:  # If empty
            stack.append(char)
        elif char not in table:  # Add all openings
            stack.append(char)
        elif table[char] == stack[-1]:  # Check opening match
            stack.pop()  # Clear a match
        else:
            stack.append(char)
    if stack:
        print("NO")
    else:
        print("YES")  # If stack is empty at the end