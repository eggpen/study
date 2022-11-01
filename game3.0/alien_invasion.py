from asyncore import loop
from hashlib import new
from operator import truediv
from random import gammavariate

import sys
import wave
#内置标准模块
import pygame           #调用pygame库
import settings         #调用自己做的模块


pygame.init()
#初始pygame所有化模块，虽然大多数模块没有这行也能运行，但没有这行代码字体模块可能会出错。

        #音乐
jntm_bgm = pygame.mixer.Sound('./bgm/jntm.mp3')
jntm_bgm.play(loops=-1)


        #主窗口
screen_image = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#创建一个窗口，宽800像素高600像素，有两个括号，说明里面的参数是一个元组
screen_rect = screen_image.get_rect()
                    #获取图像信息

        #标题栏
pygame.display.set_caption('myDemo')          #修改标题栏里的文字

        #飞船
ship_image = pygame.image.load('img/jige100xp.bmp') #用image模块加载图像，赋值给ship_image

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
        
        #计算
an_alien_image = pygame.image.load('img/jige.bmp')    #加载外星人的图像
an_alien_image_rect = an_alien_image.get_rect()         #用get_rect()获取它的rect
an_alien_width = an_alien_image_rect.width              #有了rect那么单个图像的宽度就有了
an_alien_height = an_alien_image_rect.height            #同样的高度也有了
screen_width, screen_height = screen_rect.size          #表达主窗口的宽度和高度
ship_width, ship_height = ship_rect.size                #飞船的宽和高
space_x = screen_width -2 * an_alien_width              #外星人在水平方向上的可用空间，主窗口宽度减去两个外星人的宽度
                                                        #就是不要外星人把屏幕沾满，两边各留一个外星人的空间
space_y = screen_height - ship_height -3 *an_alien_height   #同样，垂直方向上的可用空间，主窗口高度减去飞船的高度，再减去三个外星人的高度
                                                            #这三个外星人的高度，一个是给屏幕顶部留的，两个是给飞船与方阵留的
                                                            #现在外星人的垂直空间个飞船的垂直空间都有了
column_number = space_x // (2 * an_alien_width)         #列数 #两个外星人之间要相隔一个外星人的距离，那么方阵的列数，就用水平空间整除两倍的外星人宽度
                                                        #双斜杠意思就是两数相除之后，去掉余数只留整数
line_number = space_y // (2 * an_alien_height)          #行数 #垂直空间整除两倍的单个外星人高度


         
            #外星人
aliens = pygame.sprite.Group()  #创建一个精灵盒子
for y_number in range(line_number):     
    for x_number in range(column_number):
        alien_sprite = pygame.sprite.Sprite()   #创建精灵
        alien_sprite.image = pygame.image.load('img/jige.bmp')
        alien_sprite.rect = alien_sprite.image.get_rect()
        alien_sprite.rect.x = an_alien_width + 2 * an_alien_width * x_number
        alien_sprite.rect.y = an_alien_height + 2 * an_alien_height * y_number
        aliens.add(alien_sprite)

alien_direction = 1

'''
aliens = {}
for y_number in range(line_number):     #行数
    for x_number in range(column_number):   #列数
        alien_image = pygame.image.load('img/jige.bmp')      #加载图像
        alien_rect = alien_image.get_rect()     #获取rect
        alien_rect.x = an_alien_width + 2 * an_alien_width * x_number  #横坐标x
        alien_rect.y = an_alien_height + 2 *an_alien_height * y_number  #纵坐标y
        aliens[alien_image] = alien_rect    #把外星人加到字典里，这里image就是字典的key值 #外星人rect形状位置就是字典的value值
'''    



'''
ship_rect.center = screen_rect.center         #center居中,飞船居中与屏幕中心
     #子弹
bullet_rect = pygame.Rect(0, 0, 3, 15)
                #        (x  y  宽  高)
bullet_rect.midbottom = ship_rect.midtop      #让子弹的底部中心与飞船的顶部中心相等
'''
        #文字
txt_font = pygame.font.Font('./Fonts/simhei.ttf', 80)   #.Font 指定字体文件夹
#txt_font = pygame.font.SysFont(None, 48)
#字体模块,None表示系统默认字体,48为字号
txt_image = txt_font.render("IKUN才会赢", True, settings.bg_color2, settings.bg_color1)
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
                    new_bullet.rect = pygame.Rect(0, 0, 13, 20)   #子弹的rect给到精灵的.rect,注意 精灵的rect前面有个点
                    new_bullet.rect.midbottom = ship_rect.midtop  #精灵rect底部中心与飞船顶部中心对齐
                    bullets.add(new_bullet)  #把精灵加入到装精灵的盒子里，注意add只能加精灵，别的加不进去，因为源代码里规定只有带.image和.rect的才可以

            # if event.key == pygame.K_SPACE:   #检测是否按下空格建
            #         if len(bullets) < 5:      #场景中子弹小于5才能创建
            #             new_bullet_rect = pygame.Rect(0, 0, 5, 15)
            #             #生成一个子弹为5个像素宽，15个像素高
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

    for alien in aliens:  #检测外星人精灵碰撞屏幕边缘，如果有一个碰到边缘，全部都会反方向移动
        if alien.rect.right >= screen_rect.right or alien.rect.left <= 0:
            alien_direction *=-1
            break


    for alien in aliens:        #for循环把精灵盒子里的精灵挨个取出来
        alien.rect.x += 1 *alien_direction      #把它们的x横坐标都加一 #在让速度乘以方向变量，如果方向变量是正一整体向右，负一向左

    aliens.draw(screen_image)   #把盒子里的精灵都绘制出来，这里不需要for循环，精灵盒子自带draw()方法，只需要告诉参数画在哪就行了
    pygame.sprite.groupcollide(bullets, aliens, True, True)     #调用精灵模块的群组碰撞功能，群组碰撞功能有四个参数
                        #前两个是哪两个碰撞，后两个是希望谁被消灭
    
    
    '''
    for key_image, value_rect in aliens.items():    #用for循环把字典里的key值和value值取出来
            screen_image.blit(key_image, value_rect)    #然后用主窗口的绘制方法正好接受两个参数
                        #第一个参数是绘制什么，第二个参数是在哪绘制
    '''
    pygame.display.flip()                        #刷新屏幕，如果不进行刷新将无法显示新设置的东西
