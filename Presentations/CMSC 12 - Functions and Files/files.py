file = open("info.txt", "r")

# info = file.read()
lines = []
for line in file.readlines():
    lines.append(line.replace("\n","")) # without slicing, this would get the new line at the end of the line

for line in lines:
    print(line)

# print(info)
file.close()