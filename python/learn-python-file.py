#coding=utf-8
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

fo = open('nginx.log', 'rb')
line = fo.readline()
print line
fo.seek(2, 0) #offset -- 开始的偏移量，也就是代表需要移动偏移的字节数 第二个参数意义: 0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起
line = fo.readline()
print line

count = linecache.getline('nginx.log',3)
print count
print count.find("dfa")
print count.find("fgdc")

counts = linecache.getlines('nginx.log',3)
print counts
