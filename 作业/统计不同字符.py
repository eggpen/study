input_str = input('请输入一行字符')
eng_num = 0
dig_num = 0
spa_num = 0
other_num = 0
chi_num = 0
for i in input_str: #查看全部字符串，去除每个字符
    ord_i = ord(i)      #取出每个字符的Unicode编码值
    if ord('a') <= ord_i <= ord('z') or ord('A') <= ord_i <= ord('Z'):
        #英文字符
        eng_num += 1
    elif ord('0') <= ord_i <= ord('9'):
        #数字字符
        dig_num += 1
    elif ord(' ') == ord(i):
        #空格字符
        spa_num += 1
    elif 0x4E00 <= ord_i <= 0x9FFF:
        chi_num += 1
    else:
        #其他字符
        other_num += 1
print('{}中，英文字符{}个，数字字符{}个，空格字符{}个，中文字符为{}，其他字符{}个，'.format(input_str, eng_num, dig_num, spa_num, chi_num, other_num))

