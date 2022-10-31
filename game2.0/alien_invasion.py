from hashlib import new
from operator import truediv
from random import gammavariate
import sys
#内置标准模块
import pygame           #调用pygame库
import settings         #调用自己做的模块bg_color
pygame.init()
#初始pygame所有化模块，虽然大多数模块没有这行也能运行，但没有这行代码字体模块可能会出错。

        #主窗口
screen_image = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#创建一个窗口，宽800像素高600像素，有两个括号，说明里面的参数是一个元组
screen_rect = screen_image.get_rect()
                    #获取图像信息

        #标题栏
pygame.display.set_caption('myDemo')          #修改标题栏里的文字

        #飞船
ship_image = pygame.image.load('img/bmp.bmp') #用image模块加载图像，赋值给ship_image

ship_rect = ship_image.get_rect()
                #获取图像信息
ship_rect.midbottom = screen_rect.midbottom  #飞船底部位于屏幕底部

moving_left = False
moving_right = False
#设置一个开关，它们最初的状态都是False(假)
#true(真),False(假)

#子弹
bullets = pygame.sprite.Group()     #精灵盒子，也是一个列表，不过只能装精灵
# bullets = []

'''
ship_rect.center = screen_rect.center         #center居中,飞船居中与屏幕中心
     #子弹
bullet_rect = pygame.Rect(0, 0, 3, 15)
                #        (x  y  宽  高)
bullet_rect.midbottom = ship_rect.midtop      #让子弹的底部中心与飞船的顶部中心相等
'''
        #文字
txt_font = pygame.font.Font('./Fonts/simhei.ttf', 70)   #.Font 指定字体文件夹
#txt_font = pygame.font.SysFont(None, 48)
#字体模块,None表示系统默认字体,48为字号
txt_image = txt_font.render("按ESC结束运行", True, settings.bg_color2, settings.bg_color1)
                                    #显示的文字，        前景色，            背景色
#生成文本的图像,在pygame里没有文字只有图像,所以想要文字就要先转换为图像
txt_rect = txt_image.get_rect()
                #获取图像信息
txt_rect.center = screen_rect.center  #文字居中与屏幕中心


while True:         #死循环
#建立一个循环（死循环）
#建立在死循环里既可以让程序一直运行，又可以持续捕获运行时的所有操作
#任何时候，只要我们按了退出，程序就会马上结束
    for event in pygame.event.get():         #for循环捕获鼠标操作，将捕获结果给到event
        if event.type == pygame.QUIT:
        #用条件语句判断是否点击退出按钮，pygame.QUIT: 代表退出按钮
           #如果点击了退出按钮，系统就退出 
            sys.exit()                       #退出
        elif event.type == pygame.KEYDOWN:   #如果不是系统退出而是键盘操作的情况
            if event.key == pygame.K_ESCAPE:       #检测按键q
                sys.exit()                      #系统退出
             
            #筛选按的是哪个按键
            if event.key == pygame.K_LEFT:   #如果按的是左键
                moving_left = True           #检测开关  true(真)
            #    ship_rect.x -= 10            #就让ship_rect的x轴减十个像素
            if event.key == pygame.K_RIGHT:  #如果右箭头
            #    ship_rect.x += 10            #加十个像素（移动）
                moving_right = True           #检测开关  true(真)
            if event.key == pygame.K_SPACE:
                if len(bullets) < settings.bullets_allowed:         #场景中子弹小于5才能创建
                    new_bullet = pygame.sprite.Sprite()  #调用精灵，这个精灵是一个可以有image属性和retc属性的对象
                                                        #也就是精灵名称后面也可以是.image 也可以是.retc
                                                        #这跟图像是有区别的，虽然图像文件也有image属性和retc属性，但名称后面不能有.image 或 .retc
                    new_bullet.rect = pygame.Rect(0, 0, 5, 15)   #子弹的rect给到精灵的.rect,注意 精灵的rect前面有个点
                    new_bullet.rect.midbottom = ship_rect.midtop  #精灵rect底部中心与飞船顶部中心对齐
                    bullets.add(new_bullet)  #把精灵加入到装精灵的盒子里，注意add只能加精灵，别的加不进去，因为源代码里规定只有带.image和.rect的才可以

            # if event.key == pygame.K_SPACE:   #检测是否按下空格建
            #         if len(bullets) < 5:      #场景中子弹小于5才能创建
            #             new_bullet_rect = pygame.Rect(0, 0, 5, 15)
            #             #生成一个子弹为3个像素宽，15个像素高
            #             new_bullet_rect.midbottom = ship_rect.midtop  #让子弹的底部中心与飞船的顶部中心对齐
            #             bullets.append(new_bullet_rect) #把生成的子弹放在子弹列表里

        elif event.type == pygame.KEYUP:     #如果松开按键
            if event.key == pygame.K_LEFT:   #如果松开左键
                moving_left = False          #检测开关  False(假)
            if event.key == pygame.K_RIGHT:  #如果松开右键
                 moving_right = False        #检测开关  False(假) 


    
    if moving_left and ship_rect.left > 0:        #检测到moving_left为True的同时，飞船的左边必须大于0(同时成立条件)
        ship_rect.x -= settings.ship_speed
    if moving_right and ship_rect.right < screen_rect.right:#检测到moving_right为True的同时，飞船右边必须小于窗口右边
        ship_rect.x += settings.ship_speed
            
            #if event.key == pygame.K_UP:     #按上箭头
            #    ship_rect.y -= 10            #减十个像素
            #if event.key ==pygame.K_DOWN:    #按下箭头
            #    ship_rect.y += 10            #加十个像素
            
            
    #bullet_rect.y -= 1  #子弹运动

    '''图像绘制'''
    screen_image.fill(settings.bg_color1)       #设置屏幕颜色为#颜色值变量
    screen_image.blit(ship_image, ship_rect)    #将飞船绘制出来
    
    
    screen_image.blit(txt_image, txt_rect)       #设置图像位置,默认出现在左上角

    #pygame.draw.rect(screen_image, settings.bg_color2, bullet_rect)#该模块有三个参数，第一个是在哪画，第二个是用什么颜色，第三个是画谁
    
    for bullet in bullets:
        pygame.draw.rect(screen_image, settings.bg_color2, bullet.rect)
        bullet.rect.y -= 1
        if bullet.rect.bottom < 0: #子弹与屏幕上方的距离小于0则删掉子弹
            bullets.remove(bullet)  #删除子弹
    # for bullet_rect in bullets: #吧列表中的rect一个一个取出来
    #     pygame.draw.rect(screen_image, settings.bg_color2, bullet_rect)#该模块有三个参数，第一个是在哪画，第二个是用什么颜色，第三个是画谁
    #     bullet_rect.y -= 1   #持续向y坐标-1
    #     if bullet_rect.bottom < 0:  
    #         bullets.remove(bullet_rect)
        


    pygame.display.flip()                        #刷新屏幕，如果不进行刷新将无法显示新设置的东西
