if __name__ == '__main__':
  N = int(input())
  output_list = []
  for i in range(N):
    command = input().split()
    if command[0] == 'insert':
      output_list.insert(int(command[1]), int(command[2]))
    if command[0] == 'print':
      print(output_list)
    if command[0] == 'remove':
      output_list.remove(int(command[1]))
    if command[0] == 'append':
      output_list.append(int(command[1]))
    if command[0] == 'sort':
      output_list.sort()
    if command[0] == 'pop':
      output_list.pop()
    if command[0] == 'reverse':
      output_list.reverse()