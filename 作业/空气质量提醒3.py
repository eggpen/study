PM = eval(input("请输入PM2.5数值"))
if 0 <= PM < 35:
    print("空气优质")
elif 35 <= PM <75:
    print("空气良好")
else:
    print("空气污染")
    