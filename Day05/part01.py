import re
id = 'FBFBBFFRLR'

row_range = [0,127]
FB = (row_range[1]-row_range[0])//2 + row_range[0]
if id[0] == 'F':
    row_range0 = [row_range[0], FB]
else:
    row_range0 = [FB+1, row_range[1]]

FB1 = (row_range0[1]-row_range0[0])//2 + row_range0[0]
if id[1] == 'F':
    row_range1 = [row_range0[0], FB1]
else:
    row_range1 = [FB1+1, row_range0[1]]

FB2 = (row_range1[1]-row_range1[0])//2 + row_range1[0]
if id[2] == 'F':
    row_range2 = [row_range1[0], FB2]
else:
    row_range2 = [FB2+1, row_range1[1]]

FB3 = (row_range2[1]-row_range2[0])//2 + row_range2[0]
if id[3] == 'F':
    row_range3 = [row_range2[0], FB3]
else:
    row_range3 = [FB3+1, row_range2[1]]


print(row_range, row_range0, row_range1, row_range2)