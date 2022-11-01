'''
#死循环，无限循环
while True:
    a = 1
    print(a)
'''



#for循环
#for 变量名称 in 集合 
for a in range(0, 10): #当循环输出完集合中的取值之后才会停止运行，#比如range(0, 10)就会运行十次,range(0, 100)就会运行一百次
    print(a)
#兔子每年以基础数乘以2，如：第一年6只，第二年12只，N年后多少只
兔子 = 3            #初始值，兔子三只
print("想知道n年后兔子多少只,请输入年数")       #打印提示信息  input 函数的返回值为字符串
N = int(input())    #int(input())是将input函数的返回值转换为int数据类型
#input()可以接收任何字符, 存储成字符串str  #int(input())只能接受数字并且转换为int数据类型

#for 变量名称 in 集合
for a in range(0, N):           #0-n年， 
    兔子 = 兔子 * 2             #兔子在设置好的基础上乘以二
    print("%d年%d只"%(N, 兔子)) #输出print(%d.%(N, 兔子))


