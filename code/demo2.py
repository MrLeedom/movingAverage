'''
加权移动平均给固定跨越期限内的每个变量值以不同的权重．其原理是；历史各期产品需求的数据信息对预测未来期内的需求量的
作用是不一样的．除了以n为周期的周期性变化外，远离目标期的变量值的影响力相对较低，故给予较低的权重．

重点是：权重的分配问题
公式：
Ｆ = w1*A1 + w2*A2 + ... + wn*An
'''
import matplotlib.pyplot as plt

#加权移动平均法
def Wmovingaverage(list2,w):
    n = len(list2)
    sum = 0
    for i in range(n):
        sum += list2[i] * w[i]
    return sum

def answer(list1, n):
    #加权移动平均法
    w = [0.2,0.3,0.5] #各期的权重
    listWMA = []
    for i in range(n-1,len(list1)):
        list2 = (list1[i-(n-1):i+1])
        listWMA.append(Wmovingaverage(list2,w))
    print('加权移动平均值的列表：{}'.format(listWMA))
    #最后的移动平均值可作为下一个数的预测
    x = listWMA[-1]
    print('下一个数的预测：{}'.format(x))
    #画图
    plt.scatter(list(range(len(listWMA))),listWMA)
    plt.show()

if __name__ == '__main__':
    list1 = [1,2,4,5,6,8,10,12,14,16,19,24,29]
    n = 3
    #加权移动平均法
    answer(list1,n)