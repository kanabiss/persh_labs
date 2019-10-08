ifname = "input.txt"
ofname = "output.txt"

with open(ifname, "r") as ifile:
	content = ifile.read()

print(content)

ofile = open(ofname, "w")

for i in range(0, len(content)):
	ofile.write(str(ord(content[i]))+' ')

ofile.close()