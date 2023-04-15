m = [[2,1,3] ,[3,1,5]]
trans_m =[[m[j][i] for  j in range(len(m))] for i in range(len(m[0]))]
print(m)
[[2,1,3],[3,1,5]]
print(trans_m)
[[2,3],[1,1] ,[3,5]]