import knapsack, time

# totalWeight = 6404180
# weights = [382745,799601,909247,729069,467902,44328,34610,698150,823460,903959,853665,551830,610856,670702,488960,951111,323046,446298,931161,31385,496951,264724,224916,169684]
# values = [ 825594,1677009,1676628,1523970,943972,97426,69666,1296457,1679693,1902996,1844992,1049289,1252836,1319836,953277,2067538,675367,853655,1826027,65731,901489,577243,466257,369261]

# totalWeight = 7
# weights = [1,3,4,5]
# values = [1,4,5,7]
# itemIndexes = [0,1,2,3]


totalWeight = 5
weights = [4,6,8]
values = [5,4,4]
itemIndexes = [0,1,2]

sol = knapsack.Knapsack(totalWeight, weights, values, itemIndexes)
time1 = time.time()
res = sol.run()
print(str(time.time() - time1) + " seconds")
print(res)
items = sol.showItems()
print(items)
print(" ".join("#"+str(i)+"," for i in items))

