#PM2.5空气质量提醒
PM = eval(input("请输入PM2.5数值"))
if 0 <= PM < 35:
    print("空气优质")
if 35 <= PM <75:
    print("空气良好")
if 75 <= PM:
    print("空气污染")