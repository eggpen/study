import random
random.seed()#初始化随机数种子
random_num = random.randint(0,9)#表示这次预设的随机数

N = 0 #猜的次数
while True:
    input_num = int(input("请猜一个0-9的整数"))
    #每次循环，猜的次数加一，将猜的数字与预设的数字进行比较，并根据相应的提示
    N += 1
    if random_num > input_num:#如果预设的比输入的要大，则提示‘太小了’
        print("太小了")
    elif random_num == input_num:
        print("预测{}次，猜中了".format(N))
        break #强制结束循环
    else:#如果预设的比输入的要小，则提示‘太大了’
        print('太大了')
        