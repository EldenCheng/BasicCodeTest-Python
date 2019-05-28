import random

#如果直接使用random方法，会随机得到一个0 - 1之间的浮点数
print("random方法会得到一个0 - 1 的浮点数: ", random.random())

#需要指定一个范围内随机获得一个整数，可以使用randint方法
print("randint方法会在指定一个范围内随机获得一个整数: ", random.randint(1, 10))

#需要指定一个列表内随机获得一个元素，可以使用choice方法
l =["A","B","C","D"]
print("choice方法会在一个列表内随机获得一个元素: ", random.choice(l))

#普通随机方法的返回值是随机的，如果需要带权重的随机值，可以使用choices方法
#注意权重的数量必须要与被挑选的元素个数一致，比如下面l有四个元素，权重就必须要四个，但权重的和不必一定是100
#参数分别是 1.population: 准备被挑选的元素列表
#           2. weights: 相对权重列表，就是各元素被挑选的比例，比如(10,5,30,5)
#           3. cumulative weights: 累计权重列表，实际上是相对权重累加起来的列表，比如上面的相对权重转化为
#                                  累计权重就是(10,15,45,50),实际就是(10,(10+5),(10+5+30),(10+5+30+5))
#           4. k: 返回元素的个数，注意k的数量等于重复挑选的次数，比如k=10就会从l中挑选10然后组成一个新的列表
print("choices方法会在一个列表内带权重地重复指定次数地随机获得元素:",random.choices(l,cum_weights=(10,15,45,50),k=10))