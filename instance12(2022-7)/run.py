def readfile(filename):
    f = open(filename,encoding = "utf-8")
    text = []
    line = f.readline()
    while line:
        text.append(line)
        line = f.readline()
    f.close()
    return text

def writefile(filename,text):
    f = open(filename,'w')
    for i in text:
        f.write(i)
    f.close()

def findstr(key,line,begin):
    for i in range(begin,len(line)-len(key)+1):
        if line[i:i+len(key)]==key:
            return i
    return -1

def replace(key,new,line):
    begin = 0
    while begin < len(line)-len(key):
        pos = findstr(key,line,begin)
        if pos == -1:
            break
        else:
            line = line[0:pos] + new + line[pos + len(key):len(line)]
            begin = pos + len(key)
    return line

text = readfile("in.txt")
key = input("查找：")
new = input("替换：")
result = []
for line in text:
    newline = replace(key,new,line)
    result.append(newline)
writefile("out.txt",result)