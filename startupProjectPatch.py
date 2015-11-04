import sys
import linecache


if len(sys.argv) < 2:
    print '\n-->ERROR PARSING COMMAND ARGUMENTS\n'
    exit(str('-->Solution file name missing after parameter : '+sys.argv[0]+'\n\n-->Please enter complete name of solution file alongwith address in format <file location>/<file name>'))

a = str(sys.argv[1]).split('\\')
name = a.pop(a.__len__()-1)
name = name.split('.')
name = name.pop(name.__len__()-2)

f = open(str(sys.argv[1]))
start = -1
end = -1
# Locate the sim project
for num , line in enumerate(f,1):
    if line.__contains__(str('"'+name+'"')):
        start = num
    if line.__eq__('EndProject\n') and start != -1:
        end = num
        break
# write the project lines in seperate file
fout = open('./simLines.txt', 'w')
for i in range(start, end+1, 1):
    templine = linecache.getline(str(sys.argv[1]), i)
    fout.write(templine)
fout.close()

# save project lines
foutslim = open('./simLines.txt', 'r')
lineslim = foutslim.readlines()

# load existing sim.sln file contents
foutsim = open(str(sys.argv[1]), 'r')
linesim = foutsim.readlines()
foutsim.close()

# rearrange the project lines
linesim.insert(2, lineslim)
linesim.__delslice__(start,end+1)

# save rearranged lines to the solution file
fsave = open(str(sys.argv[1]), 'w')
for line in linesim:
    fsave.writelines(line)
print '\n-->Success'