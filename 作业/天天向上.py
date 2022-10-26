
import math
A君 = math.pow((1.0 + 0.01),365)
print("A君365天不停歇:{:.2f}.".format(A君));

def dayUP(df):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1+ df)
    return dayup
B君 = 0.01
while (dayUP(B君)<37.78):
    B君 += 0.001
print("B君工作日的努力参数是:{:.3f}.".format(B君));