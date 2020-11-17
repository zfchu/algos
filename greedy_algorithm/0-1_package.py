class goods:
    def __init__(self, name, weight=0, value=0):
        self.name = name
        self.weight = weight
        self.value = value
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return "('%s',%d,%.2f)" % (self.name, self.weight, self.value)
 
def knapsack(bag_volume=0, goods_set=[]):
    #利用lambda函数对goods_set以单位价值作为规则进行排序，由大到小排列
    goods_set.sort(key=lambda x: x.value / x.weight, reverse=True)
    result = []
    the_cost = 0
    for good in goods_set:
        if bag_volume < good.weight:
            break
        #如果存在空间，则将此商品装入背包即放进result中，同时修改背包容量
        else:
            result.append(good)
            bag_volume = bag_volume - good.weight
 
    if len(result) < len(goods_set) and bag_volume != 0:
        result.append(goods(good.name, bag_volume, good.value *(bag_volume /                         
 good.weight)))
    #计算背包的最终价值the_cost并输出(保留两位小数)
    for x in result:
        the_cost += x.value
    print('%.2f' % the_cost)
    return result
 
if __name__ == '__main__':
    some_goods = [goods(0, 3, 5), goods(1, 5, 7), goods(2, 6, 2), goods(3, 4, 7), goods(4, 1, 3)]
    #调用knapsack函数，输出背包容量为6公斤时候背包的最大价值与商品选择
    print(knapsack(6, some_goods))
