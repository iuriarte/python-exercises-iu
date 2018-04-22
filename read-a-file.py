# file_handle = open('hello.txt', 'r')
# contents = file_handle.read()
# file_handle.close()
# print(contents)

# file_handle = open('hello.txt', 'r')
# line1 = file_handle.readline()
# file_handle.close()
# print(line1)

file_handle = open('hello.txt', 'r')
while True:
  c = file_handle.read(1)
  if c is None:
    break
  else:
    print(c)
file_handle.close()