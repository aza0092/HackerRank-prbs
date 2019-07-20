if __name__ == '__main__':
  N = int(input())
  output_list = []
  for i in range(N):
    read_inp = input().split()
    command = read_inp[0]
    if command == 'insert':
      output_list.insert(int(read_inp[1]), int(read_inp[2]))
    if command == 'print':
      print(output_list)
    if command == 'remove':
      output_list.remove(int(read_inp[1]))
    if command == 'append':
      output_list.append(int(read_inp[1]))
    if command == 'sort':
      output_list.sort()
    if command == 'pop':
      output_list.pop()
    if command == 'reverse':
      output_list.reverse()