import linecache

count = 0

thefile = open('nginx.log', 'rb')

while True:
    buffer = thefile.read(8192*1024)
    if not buffer:
        break
    count += buffer.count('\n')

thefile.close( )

print count

count = linecache.getline('nginx.log',linenum)