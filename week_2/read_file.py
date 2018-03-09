file_handle = open ('hello.tx', 'r')

while True:
    char = file_handle.read(1)
    if not char:
        break
        
    else:
        print(char)
        