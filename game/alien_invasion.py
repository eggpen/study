import sys
#内置标准模块
import pygame           #调用pygame库
import settings         #调用自己做的模块bg_color
pygame.init()
#初始pygame所有化模块，虽然大多数模块没有这行也能运行，但没有这行代码字体模块可能会出错。

'''主窗口'''
screen_image = pygame.display.set_mode((800, 600))
#创建一个窗口，宽800像素高600像素，有两个括号，说明里面的参数是一个元组
screen_rect = screen_image.get_rect()
                    #获取图像信息

'''标题栏'''
pygame.display.set_caption('myDemo')          #修改标题栏里的文字

'''飞船'''
ship_image = pygame.image.load('img/bmp.bmp') #用image模块加载图像，赋值给ship_image

ship_rect = ship_image.get_rect()
                #获取图像信息
ship_rect.center = screen_rect.center         #center居中,让飞船居中与屏幕

'''子弹'''
bullet_rect = pygame.Rect(0, 0, 3, 15)
                #        (x  y  宽  高)
bullet_rect.midbottom = ship_rect.midtop      #让子弹的底部中心与飞船的顶部中心相等

'''文字'''
txt_font = pygame.font.SysFont(None, 48)
#字体模块，None表示系统默认字体，48为字号
txt_image = txt_font.render('50', True, settings.bg_color2, settings.bg_color3)
                        #显示的文字，        前景色， 背景色
#生成文本的图像，在pygame里没有文字只有图像，所以想要文字就要先转换为图像
txt_rect = txt_image.get_rect()
                #获取图像信息
txt_rect.x = 740
txt_rect.y = 20


'''死循环'''
while True:
#建立一个循环（死循环）
#建立在死循环里既可以让程序一直运行，又可以持续捕获运行时的所有操作
#任何时候，只要我们按了退出，程序就会马上结束
    for event in pygame.event.get():         #for循环捕获鼠标操作，将捕获结果给到event
        if event.type == pygame.QUIT:
        #用条件语句判断是否点击退出按钮，pygame.QUIT: 代表退出按钮
           #如果点击了退出按钮，系统就退出 
            sys.exit()                       #退出
        elif event.type == pygame.KEYDOWN:   #如果不是系统退出而是键盘操作的情况
            #筛选按的是哪个按键
            if event.key == pygame.K_LEFT:   #如果按的是左键
                ship_rect.x -= 10            #就让ship_rect的x轴减十个像素
            if event.key == pygame.K_RIGHT:  #如果右箭头
                ship_rect.x += 10            #加十个像素
            if event.key == pygame.K_UP:     #按上箭头
                ship_rect.y -= 10            #减十个像素
            if event.key ==pygame.K_DOWN:    #按下箭头
                ship_rect.y += 10            #加十个像素
    bullet_rect.y -= 1

    '''图像绘制'''
    screen_image.fill(settings.bg_color1)                 #设置屏幕颜色为#颜色值变量
    screen_image.blit(ship_image, ship_rect)
    screen_image.blit(txt_image, txt_rect)       #设置图像位置,默认出现在左上角
    pygame.draw.rect(screen_image, settings.bg_color2, bullet_rect)#该模块有三个参数，第一个是在哪画，第二个是用什么颜色，第三个是画谁
    pygame.display.flip()                        #刷新屏幕，如果不进行刷新将无法显示新设置的东西
