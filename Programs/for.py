d={1:{2:3,3:4},
   2:{1:2,2:3},
   3:{1:4,2:5}}
for i in d.keys():
    for j in d[i].keys():
        print(d[i][j])
