#encoding=utf-8
import pygame
import time
import random
from pygame.locals import *
class Base(object):
    def __init__(self,x,y,imageName):
        self.x=x
        self.y=y
        self.imageName=imageName
        self.image = pygame.image.load(self.imageName).convert()

    def display(self):
        screen.blit(self.image,(self.x,self.y))

class Plane(Base):
    def __init__(self, screen ,x,y,imageName,planeName):
        Base.__init__(self,x,y,imageName)
        self.screen=screen
        self.bulletList = []
        self.planeName = planeName


    def display(self):
        Base.display(self)
class EnemyPlane(Plane):
    def __init__(self,screen):
        Plane.__init__(self,screen,0,0,"./feiji/enemy-3.gif","Enemy")
        self.directioin = "right"  # right表示向右  left表示向左
        self.speed = random.randint(1, 5)

    def move(self):
        if self.directioin == "right":
            self.x += self.speed
        elif self.directioin == "left":
            self.x -= self.speed
            # 到达另外一个边界时，需要反转方向
        if self.x > 480:
            self.directioin = "left"
        elif self.x < 0:
            self.directioin = "right"

    def shoot(self):
        shootFlagList = [2, 6]
        shootFlag = random.randint(1, 100)
        if shootFlag in shootFlagList:
            self.bulletList.append(Bullet(self.screen, self.planeName, self.x, self.y))
            #print("x:%d,y:%d"%(self.x, self.y))
    def display(self):
        Plane.display(self)
        #print(self.bulletList)

        for bullett in self.bulletList:
            if bullett.y<=700:
                bullett.display()
                bullett.move()
                global hero
                # 以中点为心
                if ((bullett.x - hero.x - 40) ** 2 + (bullett.y - hero.y - 40) ** 2) ** 0.5 < 40 and bullett.baozhaflag==0:
                    bullett.baozhaflag = 1
                    global score
                    if score>20:
                        score-=20
                    else :
                        score=0
                    global flagg
                    flagg = 1
                    print(hero.x, hero.y)
                    imageName = "./feiji/hero_blowup_n3.gif"
                    im = hero.image
                    hero.image = pygame.image.load(imageName).convert()
                    print("END")
            else :
                self.bulletList.remove(bullett)






class playerPlane(Plane):
    def __init__(self,screen):
        Plane.__init__(self,screen,230,600,"./feiji/hero.gif","player")
        self.speed = 20
    def display(self):
        Plane.display(self)
        #print(self.bulletList)

        for bullett in self.bulletList:
            if bullett.y>=0:
                bullett.display()
                bullett.move()
                global enemy
                if ((enemy.x + 40-bullett.x ) ** 2 + ( enemy.y + 80-bullett.y) ** 2) ** 0.5 < 40 and bullett.baozhaflag==0:
                    bullett.baozhaflag=1
                    global escore
                    if escore>0:
                        escore-=20
                    global flagge
                    flagge = 1
                    print(enemy.x, enemy.y)
                    imageName = "./feiji/enemy2_down1.gif"
                    im = enemy.image
                    enemy.image = pygame.image.load(imageName).convert()
                    print("END")
            else :
                self.bulletList.remove(bullett)

    def moveRight(self):
        if self.x >= 0 and self.x <= 420:
            self.x += self.speed

    def moveLeft(self):
        if self.x <= 480 and self.x >= 20:
            self.x -= self.speed

    def sheBullet(self):
        bui = Bullet(self.screen, "player",self.x+40,self.y-4)
        self.bulletList.append(bui)
#导弹类
class Bullet(Base):
    def __init__(self,screen,bulletName,x,y):
        self.bulletName=bulletName
        imageName1 = "./feiji/bullet-1.gif"
        self.baozhaflag=0
        if bulletName=="player":
            imageName1="./feiji/bullet-3.gif"

        Base.__init__(self, x, y, imageName1)
    def move(self):
        if self.bulletName=="player":
            self.y -= 2
        else :
            self.y+=2
    def display(self):
        Base.display(self)

if __name__=='__main__':
    score=200
    escore=100
    #1.创建一个窗口
    screen = pygame.display.set_mode((480,700),0,32)
    #2.创建一个图片
    background=pygame.image.load("./feiji/background.png").convert()

    color_red = (255, 0, 0)
    color_green = (0, 255, 0)
    color_blue = (0, 0, 255)
    print(pygame.font.get_fonts())
    pygame.font.init()
    #font = pygame.font.SysFont(None, 48)

    # 使用系统字体
    fontObj3 = pygame.font.SysFont('arial', 20)

    # 加粗
    fontObj3.set_bold(True)

    # 斜体
    fontObj3.set_italic(True)

    # 文字具有蓝色背景
    textSurfaceObj3 = fontObj3.render("敌方血量："+str(score), True, color_red, color_blue)
    textRectObj3 = textSurfaceObj3.get_rect()
    textRectObj3.center = (60, 510)

    # 文字具有蓝色背景
    textSurfaceObj2 = fontObj3.render("我方血量：" + str(escore), True, color_red, color_blue)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (60, 10)

    #创建玩家飞机
    #hero = pygame.image.load("./feiji/hero.gif").convert()
    global flagg
    flagg=0
    flagge=0
    global hero
    hero=playerPlane(screen)
    global enemy
    enemy = EnemyPlane(screen)
    #3.图片到背景去
    imm = hero.image
    imme=enemy.image
    while True:
        screen.blit(background,(0,0))
        textSurfaceObj3 = fontObj3.render("Me   :"+str(score), True, color_red, color_blue)
        textRectObj3 = textSurfaceObj3.get_rect()
        textRectObj3.center = (60, 510)

        # 文字具有蓝色背景
        textSurfaceObj2 = fontObj3.render("Enemy :" + str(escore), True, color_red, color_blue)
        textRectObj2 = textSurfaceObj2.get_rect()
        textRectObj2.center = (60, 10)

        screen.blit(textSurfaceObj3, textRectObj3)
        screen.blit(textSurfaceObj2, textRectObj2)
        #screen.blit(hero, (x, 600))
        #hero.display()
        # 获取事件，比如按键等
        for event in pygame.event.get():

            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            # 判断是否是按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    hero.moveLeft()

                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    hero.moveRight()

                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')
                    hero.sheBullet()

                    # 更新需要显示的内容

        hero.display()
        if flagg==1:
            hero.image=imm
            flagg=0

        # 让敌机自己移动以及发射子弹
        enemy.move()
        enemy.shoot()
        enemy.display()
        if flagge==1:
            enemy.image=imme
            flsgge=0
        pygame.display.update()
        time.sleep(0.01)