'''
移动平均法：Moving average,又称为滑动平均法，滑动平均模型法
移动平均法是用一组最近的实际数据值来预测未来一期或几期内公司产品的需求量＼公司产能等的一种常用方法．
移动平均法适用于近期预测．当产品需求既不快速增长也不快速下降，且不存在季节性因素时，移动平均法能有效地消除预测中的随机波动，
是非常有用的．移动平均法根据预测时使用的各因素的权重不同，可以分为：简单移动平均和加权移动平均．

移动平均法是一种简单平滑预测技术，它的基本思想是：根据时间序列资料，逐项推移，以此计算包含一定项数的序时平均值，以反映
长期趋势的方式．因此，当时间序列的数值由于受周期变动和随机波动的影响，起伏较大，不易显示出事件的发展趋势时，使用移动
平均法可以消除这些因素的影响，显示出事件的发展方向与趋势（即趋势线），然后依趋势线分析预测序列的长期趋势．
公式：
F = (A1 + A2 + ... + An) / n
'''

import matplotlib.pyplot as plt

#简单移动平均法
def moving_average(list):
    n = len(list)
    sum = 0
    for i in list:
        sum += i
    result = sum / n
    return result

def answer(list1,n):
    #简单移动平均法
    listMA = []
    for i in range(n-1,len(list1)):
        list2 = (list1[i-(n-1):i+1])
        listMA.append(moving_average(list2))
    print('简单移动平均值的列表：{}'.format(listMA))
    #最后的移动平均值可作为下一个数的预测
    x = listMA[-1]
    print('下一个数的预测：{}'.format(x))
    #画图
    d = [i for i in range(len(listMA))]
    # print(list(d))
    plt.scatter(d,listMA) 
    plt.show()

if __name__ == '__main__':
    list1 = [1,2,4,5,6,8,10,12,14,16,19,24,29]
    n = 3  #移动平均期数
    answer(list1,n) 