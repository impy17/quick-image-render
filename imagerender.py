# !/usr/bin/python

# python imagerender.py CAMERA.CSV

# ------------------------------------------
# CSV file formatted with two columns, the
# first one is a timestamp which will need
# to be stripped and the second is the hex-
# codes, which will be stored in a list that
# can then be read to render the jpeg image
# ------------------------------------------

# ------------------------------------------
# for focusing the UCAM-II camera, make sure
# to measure from edge of the lense to the 
# baseplate of the enclosure: the measurement
# is 11.69mm for focus on midsection of boom
# ------------------------------------------

import sys

# creating lists to hold csv information
content = []
outputContent = []

# opening up csv file passed to program
# and reading in the values to the list
output = open(sys.argv[1], 'r')
for line in output.readlines():
    content.append(line)

# stripping the new lines and returns
# and then filtering out empty elements
content = [x.strip('\n') for x in content]
content = [x.strip('\r') for x in content]

content = list(filter(None, content))

# splitting the timestamp off of the hex-codes
i = 0
while i != len(content):
    outputContent.append(content[i].split(", "))
    i = i + 1

# determining size of new list
size = len(outputContent)
i = 0

# looping through and converting hexcodes to
# jpeg images arbitrarily named
while i != size:
    output = open("camera_" + str(i + 1) + ".jpeg", 'wb')
    d = bytearray(int(i, 16) for i in outputContent[i][1].strip().split(' '))
    output.write(d)
    output.close()
    i = i + 1
