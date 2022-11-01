test1 = input("")  #test表示变量名称，input("")获取用户输入的字符串
test2 = input("")
print("世界那么大{}想去{}看看".format(test1,test2))  
# {}.format()截取变量获取的字符串,并填充到“{花括号}”内。

#当然format函数的值也可以直接是变量，但必须在花括号内输入输入变量名称，操作如下
print("世界那么大{test3}想去{test4}看看".format(test3 = "张三" ,test4 = "李四"))