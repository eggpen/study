a = int(input('底数:'))  #test表示变量名称，input("")获取用户输入的字符串
b = int(input('幂数:'))
def power(a,b):
    s = a**b
    return s
print(a,'的',b,'次方=',power(a,b))

 
# {}.format()截取变量获取的字符串,并填充到前面“{花括号}”内。