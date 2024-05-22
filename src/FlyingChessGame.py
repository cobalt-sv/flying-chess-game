import sys
import pygame
from  math import  pi
import  dicing
from random import randint

pygame.init()
#窗口大小
window=pygame.display.set_mode((800,900))
#标题
pygame.display.set_caption("FlyingChessGame")
#背景色
window.fill((15, 45, 79))

font_01=pygame.font.Font('files/AGENCYB.TTF',50)
text_01=font_01.render('FlyingChessGame',False,(217, 104, 49))
window.blit(text_01,(250,25))

x_01=80
y_01=120

#摇到的数字
playerNum=0

walkNum=0
#玩家A与B现在的位置
player_A_nowPos=0
player_B_nowPos=0
#是不是玩家A的回合
isPlayer_ATurn=True
#播放格子浮动动画
aniGoingOn=True



#互换的格子的位置,一共四个
switchGridPos_01=randint(2, 7)
switchGridPos_02=dicing.Dicing().dice(6)
# switchGridPos_02=6
switchGridPos_03=dicing.Dicing().dice(6)
switchGridPos_04=dicing.Dicing().dice(6)
# print(switchGridPos_01)
# print(switchGridPos_02)
# print(switchGridPos_03)
# print(switchGridPos_04)
#换算为玩家位置
switchGridPositions=[switchGridPos_01,switchGridPos_02+8+2,switchGridPos_03+8+2+7+2,switchGridPos_04+8+2+7+2+7+2]
# switchGridPositions=[6,16,25,34]

#后退的格子的位置,一共三个
# backUpGridPos_01=randint(2, 7)
# 特殊的格子不能重合
# while backUpGridPos_01==switchGridPos_01:
#     backUpGridPos_01 = randint(2, 7)
backUpGridPos_02=dicing.Dicing().dice(6)
#特殊的格子不能重合
while backUpGridPos_02==switchGridPos_02:
    backUpGridPos_02 = randint(2, 6)
backUpGridPos_03=dicing.Dicing().dice(6)
#特殊的格子不能重合
while backUpGridPos_03==switchGridPos_03:
    backUpGridPos_03 = randint(2, 6)
backUpGridPos_04=dicing.Dicing().dice(6)
#特殊的格子不能重合
while backUpGridPos_04==switchGridPos_04:
    backUpGridPos_04 = randint(2, 6)
#换算为玩家位置
backUpGridPositions=[backUpGridPos_02+8+2,backUpGridPos_03+8+2+7+2,backUpGridPos_04+8+2+7+2+7+2]
print("backUpGridPositions")
print(backUpGridPositions)

# AB玩家互相交换的格子
ExchangeGridPos_01=randint(2, 7)
while ExchangeGridPos_01==switchGridPos_01:
       ExchangeGridPos_01 = randint(2, 6)
# ExchangeGridPos_01=2

ExchangeGridPos_02=randint(2, 6)
while ExchangeGridPos_02==switchGridPos_02 or ExchangeGridPos_02==backUpGridPos_02:
      ExchangeGridPos_02 = randint(2, 6)

ExchangeGridPos_03=randint(2, 6)
while ExchangeGridPos_03==switchGridPos_03 or ExchangeGridPos_03==backUpGridPos_03:
      ExchangeGridPos_03 = randint(2, 6)

ExchangeGridPos_04=randint(2, 6)
while ExchangeGridPos_04==switchGridPos_04 or ExchangeGridPos_04==backUpGridPos_04:
      ExchangeGridPos_04 = randint(2, 6)

#换算为玩家位置
ExchangeGridPositions=[ExchangeGridPos_01,ExchangeGridPos_02+8+2,ExchangeGridPos_03+8+2+7+2,ExchangeGridPos_04+8+2+7+2+7+2]
print("ExchangeGridPositions")
print(ExchangeGridPositions)

#棋子们的位置
positions_01=[(x_01,y_01),(x_01+80,y_01),(x_01+160,y_01),(x_01+240,y_01),(x_01+320,y_01),(x_01+400,y_01),(x_01+480,y_01),(x_01+560,y_01)]
positions_02=[(x_01+560,y_01+80),(x_01+560,y_01+160)]
positions_03=[(x_01+480,y_01+160),(x_01+400,y_01+160),(x_01+320,y_01+160),(x_01+240,y_01+160),(x_01+160,y_01+160),(x_01+80,y_01+160),(x_01,y_01+160)]
positions_04=[(x_01,y_01+240),(x_01,y_01+320)]
positions_05=[(x_01+80,y_01+320),(x_01+160,y_01+320),(x_01+240,y_01+320),(x_01+320,y_01+320),(x_01+400,y_01+320),(x_01+480,y_01+320),(x_01+560,y_01+320)]
positions_06=[(x_01+560,y_01+400),(x_01+560,y_01+480)]
positions_07=[(x_01+480,y_01+480),(x_01+400,y_01+480),(x_01+320,y_01+480),(x_01+240,y_01+480),(x_01+160,y_01+480),(x_01+80,y_01+480),(x_01,y_01+480)]
#玩家的位置
player_positions_01=[(x_01+20,y_01+21),(x_01+80+20,y_01+21),(x_01+160+20,y_01+21),(x_01+240+20,y_01+21),(x_01+320+20,y_01+21),(x_01+400+20,y_01+21),(x_01+480+20,y_01+21),(x_01+560+20,y_01+21),
                     (x_01+560+20,y_01+80+21),(x_01+560+20,y_01+160+21),
                     (x_01+480+20,y_01+160+21),(x_01+400+20,y_01+160+21),(x_01+320+20,y_01+160+21),(x_01+240+20,y_01+160+21),(x_01+160+20,y_01+160+21),(x_01+80+20,y_01+160+21),(x_01+20,y_01+160+21),
                     (x_01+ 20,y_01+240+21),(x_01+ 20,y_01+320+ 21),
                     (x_01+80+ 20,y_01+320+21),(x_01+160+ 20,y_01+320+21),(x_01+240+ 20,y_01+320+21),(x_01+320+ 20,y_01+320+21),(x_01+400+ 20,y_01+320+21),(x_01+480+ 20,y_01+320+21),(x_01+560+ 20,y_01+320+21),
                     (x_01+560+ 20,y_01+400+21),(x_01+560+ 20,y_01+480+21),
                     (x_01+480+ 20,y_01+480+21),(x_01+400+ 20,y_01+480+21),(x_01+320+ 20,y_01+480+21),(x_01+240+ 20,y_01+480+21),(x_01+160+ 20,y_01+480+21),(x_01+80+ 20,y_01+480+21),(x_01+ 20,y_01+480+21)]
#基本的格子
image_01= pygame.image.load('files/icon_05.png')
new_01=pygame.transform.rotozoom(image_01,0,0.3)
#拐角的格子
image_02= pygame.image.load('files/coner_01.png')
new_02=pygame.transform.rotozoom(image_02,0,0.3)
#玩家A
player_A= pygame.image.load('files/icon_8.png')
new_player_A=pygame.transform.rotozoom(player_A,45,0.06)
window.blit(new_player_A,  (player_positions_01[0]))
#玩家A在交换格子上
playerAOnSwitchGrid= pygame.image.load('files/playerAOnSwitchGrid.png')
new_playerAOnSwitchGrid=pygame.transform.rotozoom(playerAOnSwitchGrid,0,0.3)
#玩家A在AB互换格子上
playerAOnExchangeGrid= pygame.image.load('files/PlayerAOnchangeGrid.png')
new_playerAOnExchangeGrid=pygame.transform.rotozoom(playerAOnExchangeGrid,0,0.3)
#玩家B
player_B= pygame.image.load('files/player_02.png')
new_player_B=pygame.transform.rotozoom(player_B,0,0.09)
window.blit(new_player_B,  (player_positions_01[0]))
#玩家B在交换格子上
playerBOnSwitchGrid= pygame.image.load('files/playerBOnSwitchGrid.png')
new_playerBOnSwitchGrid=pygame.transform.rotozoom(playerBOnSwitchGrid,0,0.3)
#玩家B在AB互换格子上
playerBOnExchangeGrid= pygame.image.load('files/PlayerBOnchangeGrid.png')
new_playerBOnExchangeGrid=pygame.transform.rotozoom(playerBOnExchangeGrid,0,0.3)
#互换的格子
image_03 = pygame.image.load('files/icon_07.png')
new_03 = pygame.transform.rotozoom(image_03, 0, 0.3)
#后退的格子
backUpImage = pygame.image.load('files/backUpGrid.png')
backUpGrid = pygame.transform.rotozoom(backUpImage, 0, 0.3)
backUpGrid_01 = pygame.transform.rotozoom(backUpImage, 180, 0.3)
#  最后的格子
finalImage=pygame.image.load('files/finalGrid_01.png')
finalGrid = pygame.transform.rotozoom(finalImage, 0, 0.3)
#  胜利的祝福
win_font=pygame.font.Font('files/AGENCYB.TTF',50)
win_text=win_font.render('PlayerA reached the finish line first. Congratulations to PlayerA',False,(217, 104, 49))
# AB互换的格子
ExchangeImage = pygame.image.load('files/changeGrid_02.png')
ExchangeGrid = pygame.transform.rotozoom(ExchangeImage, 0, 0.3)
# AB踩在哪个交换格子上了
whichABExchange=-1
# 背景音乐
pygame.mixer.music.load('files/TSAR - 0.0.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
# 音效
move_sound = pygame.mixer.Sound('files/switchCam.mp3')
move_sound.set_volume(0.8)
# 音效
backUp_sound = pygame.mixer.Sound('files/backUp.wav')
backUp_sound.set_volume(0.8)
# 音效
switch_sound = pygame.mixer.Sound('files/switch.mp3')
switch_sound.set_volume(0.8)
# 音效
win_sound = pygame.mixer.Sound('files/win.mp3')
win_sound.set_volume(0.8)
# 胜利界面
WinImage = pygame.image.load('files/winPanle_01.png')
WinPanle = pygame.transform.rotozoom(WinImage, 0, 0.85)

class Mapping(object):
    def __init__(self): # __init__构造函数

        pass

    def map():
        #标题
        pygame.display.set_caption("FlyingChessGame")
        font_01 = pygame.font.Font('files/AGENCYB.TTF', 50)
        text_01 = font_01.render('FlyingChessGame', False, (217, 104, 49))
        window.blit(text_01, (250, 25))
        # 玩家A
        player_A = pygame.image.load('files/icon_8.png')
        new_player_A = pygame.transform.rotozoom(player_A, 45, 0.06)
        window.blit(new_player_A, (90, 680+20))
        # 底部提示
        font_02=pygame.font.Font('files/GILB____.TTF',22)
        text_02 = font_02.render(':PLAYER  A', False, (217, 104, 49))
        window.blit(text_02, (120, 675+20))
        # 玩家B
        player_B= pygame.image.load('files/player_02.png')
        new_player_B = pygame.transform.rotozoom(player_B, 0, 0.09)
        window.blit(new_player_B, (90, 680+50))
        # 底部提示
        text_03 = font_02.render(':PLAYER  B', False, (217, 104, 49))
        window.blit(text_03, (120, 675+50))
        # 底部规则
        rules_font = pygame.font.Font('files/GILB____.TTF', 20)
        rules = rules_font.render(': Switch the positions of  A and  B', False, (39, 175, 189))

        new_03_01 = pygame.transform.rotozoom(image_03, 0, 0.13)
        window.blit(new_03_01, (315, 695))

        # backUpImage = pygame.image.load('files/backUpGrid.png')
        backUpGrid_011 = pygame.transform.rotozoom(backUpImage, 0, 0.13)
        window.blit(backUpGrid_011, (315, 745))

        ExchangeGrid_01 = pygame.transform.rotozoom(ExchangeImage, 0, 0.13)
        window.blit(ExchangeGrid_01, (315, 720))

        rules_01 = rules_font.render(': Cross over to another identical grid', False, (39, 175, 189))
        rules_02 = rules_font.render(': Back random steps', False, (39, 175, 189))
        window.blit(rules_01, (360, 695))
        window.blit(rules, (360, 720))
        window.blit(rules_02, (360, 745))
        # 交换的格子
        new_03 = pygame.transform.rotozoom(image_03, 0, 0.3)
        # 后退的格子
        backUpGrid = pygame.transform.rotozoom(backUpImage, 0, 0.3)
        # AB互换的格子
        ExchangeGrid = pygame.transform.rotozoom(ExchangeImage, 0, 0.3)
        # 最后的格子
        finalGrid = pygame.transform.rotozoom(finalImage, 0, 0.3)
        # 拐角的格子的装饰线_01
        pygame.draw.line(window, (239, 169, 109), (x_01 + 560 + 8, y_01 + 3), (x_01 + 615, y_01 + 3), 2)
        pygame.draw.line(window, (239, 169, 109), (x_01 + 615, y_01 + 3), (x_01 + 615, y_01 + 50), 2)
        # 拐角的格子的装饰线_02
        pygame.draw.line(window, (239, 169, 109), (x_01 + 615, y_01 + 167), (x_01 + 615, y_01 + 215), 2)
        pygame.draw.line(window, (239, 169, 109), (x_01 + 615, y_01 + 215), (x_01 + 567, y_01 + 215), 2)
        # 拐角的格子的装饰线_03
        pygame.draw.line(window, (239, 169, 109), (x_01 + 3, y_01 + 163), (x_01 + 3, y_01 + 210), 2)
        pygame.draw.line(window, (239, 169, 109), (x_01 + 3, y_01 + 163), (x_01 + 50, y_01 + 163), 2)
        # 拐角的格子的装饰线_05
        pygame.draw.line(window, (239, 169, 109), (x_01 + 560 + 8, y_01 + 313 + 10), (x_01 + 615, y_01 + 313 + 10), 2)
        pygame.draw.line(window, (239, 169, 109), (x_01 + 615, y_01 - 7 + 320 + 10), (x_01 + 615, y_01 + 50 + 320), 2)
        # 拐角的格子的装饰线_06
        pygame.draw.line(window, (239, 169, 109), (x_01 + 615, y_01 + 167 + 320), (x_01 + 615, y_01 + 215 + 320), 2)
        pygame.draw.line(window, (239, 169, 109), (x_01 + 615, y_01 + 215 + 320), (x_01 + 567, y_01 + 215 + 320), 2)

        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0

        # 画出每一个格子
        for items in positions_01:
            a += 1
            if a == 8:
                window.blit(new_02, items)
            elif a == switchGridPos_01:
                window.blit(new_03, items)
            elif a==ExchangeGridPos_01:
                window.blit(ExchangeGrid,items)
            else:
                window.blit(new_01, items)

        for items in positions_02:
            b += 1
            if b == 2:
                window.blit(new_02, items)
            else:
                window.blit(new_01, items)

        for items in positions_03:
            c += 1
            if c == 7:
                window.blit(new_02, items)
            elif c == switchGridPos_02:
                window.blit(new_03, items)
            elif c==backUpGridPos_02:
                window.blit(backUpGrid_01,items)
            elif c==ExchangeGridPos_02:
                window.blit(ExchangeGrid,items)
            else:
                window.blit(new_01, items)

        for items in positions_04:
            d += 1
            if d == 2:
                window.blit(new_02, items)
            else:
                window.blit(new_01, items)

        for items in positions_05:
            e += 1
            if e == 7:
                window.blit(new_02, items)
            elif e == switchGridPos_03:
                window.blit(new_03, items)
            elif e==backUpGridPos_03:
                window.blit(backUpGrid,items)
            elif e==ExchangeGridPos_03:
                window.blit(ExchangeGrid,items)
            else:
                window.blit(new_01, items)

        for items in positions_06:
            f += 1
            if f == 2:
                window.blit(new_02, items)
            else:
                window.blit(new_01, items)

        for items in positions_07:
            g += 1
            if g == 8:
                window.blit(new_02, items)
            elif g == switchGridPos_04:
                window.blit(new_03, items)
            elif g==backUpGridPos_04:
                window.blit(backUpGrid_01,items)
            elif g==ExchangeGridPos_04:
                window.blit(ExchangeGrid,items)
            elif g==7:
                window.blit(finalGrid,items)
            else:
                window.blit(new_01, items)

class Tips(object):
    def __init__(self): # __init__构造函数

        pass

    def tips(self, WhosTurn): # 判断正确与否
        self.WhosTurn=True
        font_05 = pygame.font.Font('files/GILB____.TTF', 22)

        if WhosTurn:
           text_05 = font_05.render('It’s  PLAYER  A’s  turn. Press  A  to roll the dice', False, (217, 104, 49))
           window.blit(text_05, (90, 800))
        else:
            text_05 = font_05.render('It’s  PLAYER  B’s  turn. Press  A  to roll the dice', False, (217, 104, 49))
            window.blit(text_05, (90, 800))

class IsWin(object):
    def __init__(self): # __init__构造函数

        pass

    def isWin(self, WhoWin): # 判断正确与否
        self.WhosWin="someone"
        win_sound.play()
        window.blit(WinPanle,(0,0))
        # finalGrid_02 = pygame.transform.rotozoom(finalImage, 0, 1.5)
        # window.blit(finalGrid_02, (300, 300))

        #  胜利的祝福
        win_font = pygame.font.Font('files/AGENCYB.TTF', 50)
        win_text_01 = win_font.render(WhoWin+' reached the finish line first.', False,
                                   (217, 104, 49))
        win_text_02 = win_font.render('Congratulations to ' + WhoWin+'!(*^▽^*)', False,
                                   (217, 104, 49))
        window.blit(win_text_01, (100, 400))
        window.blit(win_text_02, (100, 470))
        tips_font = pygame.font.Font('files/GILB____.TTF', 22)
        # rules_font = pygame.font.Font('files/GILB____.TTF', 20)
        tips_text_01 = tips_font.render('Press R to Restart.', False,
                                      (39, 175, 189))
        tips_text_04 = tips_font.render('(This will not refresh the grid).', False,
                                        (31, 110, 141))
        tips_text_02 = tips_font.render('Or re-enter the game', False,
                                       (39, 175, 189))
        tips_text_03 = tips_font.render(
            '(This will randomly generate the map)', False,
            (31, 110, 141))
        window.blit(tips_text_01, (300, 650))
        window.blit(tips_text_04, (240, 680))
        window.blit(tips_text_02, (285, 730))
        window.blit(tips_text_03, (200, 760))





Mapping.map()#画地图
Tips().tips(isPlayer_ATurn)

#行走类
class Walk(object):
    def __init__(self): # __init__构造函数

        pass

    def walk(self, ints,player,time,number,nowPos,AnotherPos,AnotherPlayer): # 判断正确与否
        self.ints = []
        self.player=pygame.image
        self.time=0
        self.number= 1
        self.nowPos = 0
        self.AnotherPos=0
        self.AnotherPlayer = pygame.image
        playtimes=0
        pos=nowPos
        num=0
        isOver=True

        while isOver:
            num += 1
            if num % time == 0:
                pygame.time.wait(1000)
                if nowPos <= pos+number:
                    playtimes+=1
                    window.fill((15, 45, 79))
                    #重新画地图
                    Mapping.map()
                    if nowPos!=34:
                    #重新画玩家
                        print("nowPos")
                        print(nowPos)
                        print("AnotherPos")
                        print(AnotherPos)
                        window.blit(AnotherPlayer,ints[AnotherPos])
                        window.blit(player, ints[nowPos])
                        StepNum().stepNum(playerNum, isPlayer_ATurn,False)
                        nowPos += 1
                        if playtimes>1:
                            move_sound.play()
                        pygame.display.update()
                    else:
                        isOver = False
                        return 34
                        playtimes=0
                elif nowPos>pos+number:
                    playtimes = 0
                    return  nowPos-1
                    isOver=False

class StepNum(object):
    def __init__(self): # __init__构造函数

        pass

    def stepNum(self, num,WhosTurn,isClear): # 判断正确与否
        self.num=0
        # isClear=False，这句千万别加，不然你传入什么都会变成false
        font_06 = pygame.font.Font('files/GILB____.TTF', 22)

        if WhosTurn:
                text_06 = font_06.render(('PLAYER A’s die hits'+ str(num)+' .PLAYER A move forward'+str(num)+' space'), False, (217, 104, 49))
                window.blit(text_06, (90, 830))

        else:
                text_06 = font_06.render('PLAYER B’s die hits'+ str(num) + ' .PLAYER B move forward'+ str(num)+' space', False, (217, 104, 49))
                window.blit(text_06, (90, 830))

        if isClear==True:
            text_06 = font_06.render(
                ('PLAYER A’s die hits' + str(num) + ' .PLAYER A move forward' + str(num) + ' space'), False,
                (15, 45, 79))
            window.blit(text_06, (90, 830))
            pygame.draw.rect(window, (15, 45, 79), (90, 830, 600, 25))

class CanSwitch(object):
    def __init__(self):  # __init__构造函数

        pass

    def canSwitch(self,canSwitchBegin,playerNowPosition,switchGridPositions,whichSwitchGrid,picture):
        self.canSwitchBegin=False
        self.playerNowPosition = 1
        self.switchGridPositions = []
        self.whichSwitchGrid = 0
        self.picture = pygame.image
        switchGridPicture=new_03

        if (playerNowPosition + 1 == switchGridPositions[whichSwitchGrid] and whichSwitchGrid!=3 and canSwitchBegin):
            playerNowPosition = (switchGridPositions[whichSwitchGrid+1] - 1)
            switch_sound.play()
            return  playerNowPosition
        elif(whichSwitchGrid==3 and canSwitchBegin):
            if (playerNowPosition + 1 == switchGridPositions[3]):
                print("GoBack!!!")
                switch_sound.play()
                playerNowPosition = (switchGridPositions[2] - 1)
                return playerNowPosition
        else:
            return 0

class CanBackup(object):
    def __init__(self):  # __init__构造函数

        pass

    def canBackup(self,ints,playerNowPosition,backUpGridPositions,player,anotherPlayer,time,anotherPos):
        # self.playerNowPosition=False
        self.ints = []
        self.playerNowPosition = 1
        self.backUpGridPositions = []
        # self.whichBackUpGrid = 0
        self.player = pygame.image
        self.anotherPlayer = pygame.image
        self.time=0
        self.anotherPos=1
        # 保证第一遍等待是不播放的
        times=0
        font_06 = pygame.font.Font('files/GILB____.TTF', 22)
        # switchGridPicture=new_03
        tempNum=-1

        pos = playerNowPosition
        num = 0
        isOver = True
        # count=0
        for items in backUpGridPositions:
            # count+=1
            if playerNowPosition+1==items:
                backUp_sound.play()
                tempNum = dicing.Dicing().dice(6)
                print("tempNum")
                print(tempNum)
        if tempNum==-1:
            isOver=False
            return playerNowPosition

        while isOver:
            num += 1
            if num % time == 0:
                pygame.time.wait(1000)
                times+=1
                if playerNowPosition >= pos -  tempNum :
                    window.fill((15, 45, 79))
                    # 重新画地图
                    Mapping.map()
                    # 重新画玩家
                    if(times>1):
                        move_sound.play()
                    window.blit(anotherPlayer, ints[anotherPos])
                    window.blit(player, ints[playerNowPosition])
                    # move_sound.play()
                    # StepNum().stepNum(playerNum, isPlayer_ATurn, False)
                    playerNowPosition -= 1
                    print('playerNowPosition')
                    print(playerNowPosition)
                    text_06 = font_06.render(
                        'The die hits' + str(tempNum) + ' .Go back' + str(tempNum) + ' spaces', False,
                        (217, 104, 49))
                    window.blit(text_06, (90, 810))
                    pygame.display.update()
                elif playerNowPosition < pos -  tempNum:
                    pygame.draw.rect(window, (15, 45, 79), (90, 810, 600, 25))
                    pygame.display.update()
                    return playerNowPosition+1
                    print('playerNowPosition')
                    print(playerNowPosition)
                    isOver = False
                    times=0

class CanExchange(object):
    def __init__(self):  # __init__构造函数

        pass

    def canExchange(self,playerNowPosition,exchangeGridPositions,anotherPos,player,anotherPlayer,ints,temp):
        self.canSwitchBegin=False
        self.playerNowPosition = 1
        self.exchangeGridPositions = []
        self.anotherPos=1
        self.player = pygame.image
        self.anotherPlayer = pygame.image
        self.ints = []
        self.temp=-1

        # for items in exchangeGridPositions:
        #     temp+=1
        #     print("temp")
        #     print(temp)

        print('playerNowPosition+1')
        print(playerNowPosition + 1)
        if playerNowPosition + 1 == exchangeGridPositions[0]:
            print("进入方法了么")
            window.fill((15, 45, 79))
            # 重新画地图
            Mapping.map()
            # 重新画玩家
            window.blit(anotherPlayer, ints[playerNowPosition])
            window.blit(player, ints[anotherPos])
            whichABExchange=temp
            switch_sound.play()
            pygame.display.update()
            return 0
        elif playerNowPosition + 1 == exchangeGridPositions[1]:
            window.fill((15, 45, 79))
            # 重新画地图
            Mapping.map()
            # 重新画玩家
            window.blit(anotherPlayer, ints[playerNowPosition])
            window.blit(player, ints[anotherPos])
            whichABExchange = temp
            switch_sound.play()
            pygame.display.update()
            return 1
        elif playerNowPosition + 1 == exchangeGridPositions[2]:
            window.fill((15, 45, 79))
            # 重新画地图
            Mapping.map()
            # 重新画玩家
            window.blit(anotherPlayer, ints[playerNowPosition])
            window.blit(player, ints[anotherPos])
            whichABExchange = temp
            switch_sound.play()
            pygame.display.update()
            return 2
        elif playerNowPosition + 1 == exchangeGridPositions[3]:
            window.fill((15, 45, 79))
            # 重新画地图
            Mapping.map()
            # 重新画玩家
            window.blit(anotherPlayer, ints[playerNowPosition])
            window.blit(player, ints[anotherPos])
            whichABExchange = temp
            switch_sound.play()
            pygame.display.update()
            return 3
        else:
            return -1

switchGrid_y=positions_01[switchGridPos_01 - 1][1]
y_speed=0.02
y=positions_01[switchGridPos_01 - 1][1]

switchGrid_y_02=positions_01[switchGridPos_01 - 1][1]
y_speed_02=0.02
y_02=positions_01[switchGridPos_01 - 1][1]

num=0

#不能让AB一直交换
canASwitch=True
canBSwitch=True

temp_A_Pos=0
temp_B_Pos=0

countA=-1
countB=-1
#游戏第一次刷新
pygame.display.flip()

isGameOver=False

while True:
    # aniGoingOn = False
    # isGameOver=True

    # 播放特殊格子的动画
    if aniGoingOn:
        num += 1
        if num % 500 == 0:
            # 画跨越格子的遮挡物
            pygame.draw.rect(window, (15, 45, 79), (positions_01[switchGridPos_01 - 1][0] - 20, switchGrid_y-20, 100, 100))
            pygame.draw.rect(window, (15, 45, 79), (positions_03[switchGridPos_02 - 1][0] - 20, switchGrid_y_02+160, 100, 100))
            pygame.draw.rect(window, (15, 45, 79), (positions_05[switchGridPos_03 - 1][0] - 20, switchGrid_y+320 - 20, 90, 100))
            pygame.draw.rect(window, (15, 45, 79), (positions_07[switchGridPos_04 - 1][0] - 20, switchGrid_y_02+480, 100, 85))
            # 画后退格子的遮挡物
            # pygame.draw.rect(window, (15, 45, 79), (positions_01[backUpGridPos_01 - 1][0] - 20, switchGrid_y-20, 100, 100))
            pygame.draw.rect(window, (15, 45, 79), (positions_03[backUpGridPos_02 - 1][0] - 20, switchGrid_y_02+160, 100, 100))
            pygame.draw.rect(window, (15, 45, 79), (positions_05[backUpGridPos_03 - 1][0] - 20, switchGrid_y+320 - 20, 90, 100))
            pygame.draw.rect(window, (15, 45, 79), (positions_07[backUpGridPos_04 - 1][0] - 20, switchGrid_y_02+480, 100, 85))
            # 画AB互换格子的遮挡物
            pygame.draw.rect(window, (15, 45, 79),
                             (positions_01[ExchangeGridPos_01 - 1][0] - 20, switchGrid_y - 20, 100, 100))
            pygame.draw.rect(window, (15, 45, 79),
                             (positions_03[ExchangeGridPos_02 - 1][0] - 20, switchGrid_y_02 + 160, 100, 100))
            pygame.draw.rect(window, (15, 45, 79),
                             (positions_05[ExchangeGridPos_03 - 1][0] - 20, switchGrid_y + 320 - 20, 90, 100))
            pygame.draw.rect(window, (15, 45, 79),
                             (positions_07[ExchangeGridPos_04 - 1][0] - 20, switchGrid_y_02 + 480, 100, 85))

            switchGrid_y += y_speed
            switchGrid_y_02-=y_speed

            if switchGrid_y >= y + 10:
                y_speed = y_speed * -1

            if switchGrid_y <= y-10:
                y_speed = y_speed * -1

            if switchGrid_y_02 >= y_02 + 10:
                y_speed_02 = y_speed_02 * -1

            if switchGrid_y_02 <= y_02-10:
                y_speed_02 = y_speed_02 * -1

            # 画交换格子
            window.blit(new_03, (positions_01[switchGridPos_01 - 1][0], switchGrid_y))
            window.blit(new_03, (positions_03[switchGridPos_02 - 1][0], switchGrid_y_02 + 160))
            window.blit(new_03, (positions_05[switchGridPos_03 - 1][0], switchGrid_y + 320))
            window.blit(new_03, (positions_07[switchGridPos_04 - 1][0], switchGrid_y_02 + 480))
            # 画后退格子
            # window.blit(backUpGrid, (positions_01[backUpGridPos_01 - 1][0], switchGrid_y))
            window.blit(backUpGrid_01, (positions_03[backUpGridPos_02 - 1][0], switchGrid_y_02 + 160))
            window.blit(backUpGrid, (positions_05[backUpGridPos_03 - 1][0], switchGrid_y + 320))
            window.blit(backUpGrid_01, (positions_07[backUpGridPos_04 - 1][0], switchGrid_y_02 + 480))
            # 画AB互换的格子
            window.blit(ExchangeGrid, (positions_01[ExchangeGridPos_01 - 1][0], switchGrid_y))
            window.blit(ExchangeGrid, (positions_03[ExchangeGridPos_02 - 1][0], switchGrid_y_02 + 160))
            window.blit(ExchangeGrid, (positions_05[ExchangeGridPos_03 - 1][0], switchGrid_y + 320))
            window.blit(ExchangeGrid, (positions_07[ExchangeGridPos_04 - 1][0], switchGrid_y_02 + 480))

            temp_A_Pos = CanSwitch().canSwitch(canASwitch,player_A_nowPos,switchGridPositions,0,new_player_A)
            temp_B_Pos = CanSwitch().canSwitch(canBSwitch,player_B_nowPos,switchGridPositions,0,new_player_B)

            if temp_A_Pos != 0 and temp_A_Pos != None:
                player_A_nowPos = temp_A_Pos
                countA=1#在最下面统一刷新

                canASwitch = False

            if temp_B_Pos != 0 and temp_B_Pos != None:
                player_B_nowPos = temp_B_Pos
                countB = 1
                canBSwitch = False

            #判断玩家A是否可以交换
            temp_A_Pos = CanSwitch().canSwitch(canASwitch,player_A_nowPos, switchGridPositions, 1,new_player_A)
            temp_B_Pos = CanSwitch().canSwitch(canBSwitch,player_B_nowPos, switchGridPositions, 1,new_player_B)

            if temp_A_Pos != 0 and temp_A_Pos != None:
                player_A_nowPos = temp_A_Pos
                countA=2
                canASwitch = False

            if temp_B_Pos != 0 and temp_B_Pos != None:
                player_B_nowPos = temp_B_Pos
                countB = 2
                canBSwitch = False

            temp_A_Pos = CanSwitch().canSwitch(canASwitch,player_A_nowPos, switchGridPositions, 2,new_player_A)
            temp_B_Pos = CanSwitch().canSwitch(canBSwitch,player_B_nowPos, switchGridPositions, 2,new_player_B)

            if temp_A_Pos != 0 and temp_A_Pos != None:
                player_A_nowPos = temp_A_Pos
                countA=3
                canASwitch = False

            if temp_B_Pos != 0 and temp_B_Pos != None:
                player_B_nowPos = temp_B_Pos
                countB = 3
                canBSwitch = False

            temp_A_Pos = CanSwitch().canSwitch(canASwitch,player_A_nowPos, switchGridPositions, 3,new_player_A)
            temp_B_Pos = CanSwitch().canSwitch(canBSwitch,player_B_nowPos, switchGridPositions, 3,new_player_B)

            if temp_A_Pos != 0 and temp_A_Pos!=None:
                player_A_nowPos = temp_A_Pos
                countA=2
                canASwitch = False

            if temp_B_Pos != 0 and temp_B_Pos!=None:
                player_B_nowPos = temp_B_Pos
                countB = 2
                canBSwitch = False

            if countA==1:
                    window.blit(new_playerAOnSwitchGrid, (positions_03[switchGridPos_02 - 1][0], switchGrid_y_02 + 160))
            elif countA==2:
                    window.blit(new_playerAOnSwitchGrid, (positions_05[switchGridPos_03 - 1][0], switchGrid_y + 320))
            elif countA==3:
                    window.blit(new_playerAOnSwitchGrid, (positions_07[switchGridPos_04 - 1][0], switchGrid_y_02 + 480))

            if countB==1:
                window.blit(new_playerBOnSwitchGrid, (positions_03[switchGridPos_02 - 1][0], switchGrid_y_02 + 160))
            elif countB==2:
                window.blit(new_playerBOnSwitchGrid, (positions_05[switchGridPos_03 - 1][0], switchGrid_y + 320))
            elif countB==3:
                window.blit(new_playerBOnSwitchGrid, (positions_07[switchGridPos_04 - 1][0], switchGrid_y_02 + 480))
            print("whichABExchange")
            print(whichABExchange)

            if whichABExchange==0 and isPlayer_ATurn==False:
                print("whichABExchange")
                print(whichABExchange)
                window.blit(new_playerBOnExchangeGrid, (positions_01[ExchangeGridPos_01 - 1][0], switchGrid_y))
            if whichABExchange==1 and isPlayer_ATurn==False:
                print(whichABExchange)
                window.blit(new_playerBOnExchangeGrid, (positions_03[ExchangeGridPos_02 - 1][0], switchGrid_y_02 + 160))
            if whichABExchange==2 and isPlayer_ATurn==False:
                print(whichABExchange)
                window.blit(new_playerBOnExchangeGrid, (positions_05[ExchangeGridPos_03 - 1][0], switchGrid_y + 320))
            if whichABExchange == 3 and isPlayer_ATurn == False:
                print(whichABExchange)
                window.blit(new_playerBOnExchangeGrid, (positions_07[ExchangeGridPos_04 - 1][0], switchGrid_y_02 + 480))

            if whichABExchange==0 and isPlayer_ATurn==True:
                print("whichABExchange")
                print(whichABExchange)
                window.blit(new_playerAOnExchangeGrid, (positions_01[ExchangeGridPos_01 - 1][0], switchGrid_y))
            if whichABExchange==1 and isPlayer_ATurn==True:
                print("whichABExchange")
                print(whichABExchange)
                window.blit(new_playerAOnExchangeGrid, (positions_03[ExchangeGridPos_02 - 1][0], switchGrid_y_02 + 160))
            if whichABExchange==2 and isPlayer_ATurn==True:
                print("whichABExchange")
                print(whichABExchange)
                window.blit(new_playerAOnExchangeGrid, (positions_05[ExchangeGridPos_03 - 1][0], switchGrid_y + 320))
            if whichABExchange == 3 and isPlayer_ATurn == True:
                print("whichABExchange")
                print(whichABExchange)
                window.blit(new_playerAOnExchangeGrid, (positions_07[ExchangeGridPos_04 - 1][0], switchGrid_y_02 + 480))

            elif whichABExchange==-1:
                window.blit(ExchangeGrid, (positions_01[ExchangeGridPos_01 - 1][0], switchGrid_y))
                window.blit(ExchangeGrid, (positions_03[ExchangeGridPos_02 - 1][0], switchGrid_y_02 + 160))
                window.blit(ExchangeGrid, (positions_05[ExchangeGridPos_03 - 1][0], switchGrid_y + 320))
                window.blit(ExchangeGrid, (positions_07[ExchangeGridPos_04 - 1][0], switchGrid_y_02 + 480))

            pygame.display.update()

        if isGameOver:
            print(isGameOver)
            window.fill((15, 45, 79))
            window.blit(win_text, (250, 250))
            pygame.display.update()


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            print("按键按下", event.key, chr(event.key))
            if chr(event.key) == 'a':
                playerNum=dicing.Dicing().playerDice(6)
                # playerNum=1
                pygame.display.update()
                if isPlayer_ATurn:
                    countA = -1
                    player_A_nowPos = Walk().walk(player_positions_01, new_player_A, 1000, playerNum,player_A_nowPos,player_B_nowPos,new_player_B)
                    # 玩家A有没有踩到后退的格子
                    player_A_nowPos=CanBackup().canBackup(player_positions_01,player_A_nowPos,backUpGridPositions,new_player_A,new_player_B,1000,player_B_nowPos)
                    #玩家A有没有踩到AB互换的格子
                    whichABExchange=CanExchange().canExchange(player_A_nowPos,ExchangeGridPositions,player_B_nowPos,new_player_A,new_player_B,player_positions_01,-1)
                    # 如果踩到了
                    if whichABExchange!=-1:
                        tempNumber=0
                        tempNumber= player_A_nowPos
                        player_A_nowPos=player_B_nowPos
                        player_B_nowPos=tempNumber
                    # 再判断一遍以防万一
                    # player_A_nowPos = Walk().walk(player_positions_01, new_player_A, 1000, playerNum, player_A_nowPos,
                    #                               player_B_nowPos, new_player_B)
                    player_A_nowPos = CanBackup().canBackup(player_positions_01, player_A_nowPos, backUpGridPositions,
                                                            new_player_A, new_player_B, 1000, player_B_nowPos)
                    # 再判断一遍以防万一
                    # whichABExchange = CanExchange().canExchange(player_A_nowPos, ExchangeGridPositions, player_B_nowPos,
                    #                                             new_player_A, new_player_B, player_positions_01, -1)
                    # # 再判断一遍以防万一
                    # if whichABExchange != -1:
                    #     tempNumber = 0
                    #     tempNumber = player_A_nowPos
                    #     player_A_nowPos = player_B_nowPos
                    #     player_B_nowPos = tempNumber
                    # 玩家A走完之后开始计算是不是在互换格子上
                    canASwitch = True
                    # 清屏幕下方的文字
                    StepNum().stepNum(playerNum, isPlayer_ATurn, True)
                    # 测试结算页面用的
                    # player_A_nowPos=34

                    # 玩家A是否到达终点,写到这里了
                    if player_A_nowPos == 34:
                        print("游戏结束")
                        aniGoingOn = False
                        # player_A_nowPos = 0
                        window.fill((15, 45, 79))
                        isGameOver = True
                        IsWin().isWin("PlayerA")
                        # window.blit(win_text, (250, 250))
                        pygame.display.update()
                else:
                    countB = -1
                    player_B_nowPos = Walk().walk(player_positions_01, new_player_B, 1000, playerNum, player_B_nowPos,player_A_nowPos,new_player_A)
                    # 玩家B有没有踩到后退的格子
                    player_B_nowPos=CanBackup().canBackup(player_positions_01,player_B_nowPos,backUpGridPositions,new_player_B,new_player_A,1000,player_A_nowPos)
                    # 玩家B有没有踩到AB互换的格子
                    whichABExchange = CanExchange().canExchange(player_B_nowPos, ExchangeGridPositions, player_A_nowPos,
                                                                new_player_B, new_player_A, player_positions_01,-1)
                    print('whichABExchange')
                    print(whichABExchange)
                    # 如果踩到了
                    if whichABExchange != -1:
                        tempNumberB = 0
                        tempNumberB = player_B_nowPos
                        player_B_nowPos = player_A_nowPos
                        player_A_nowPos = tempNumberB

                    # 再判断一遍以防万一
                    player_B_nowPos = CanBackup().canBackup(player_positions_01, player_B_nowPos, backUpGridPositions,
                                                            new_player_B, new_player_A, 1000, player_A_nowPos)
                    # # 再判断一遍以防万一
                    # whichABExchange = CanExchange().canExchange(player_B_nowPos, ExchangeGridPositions, player_A_nowPos,
                    #                                             new_player_B, new_player_A, player_positions_01, -1)
                    # print('whichABExchange')
                    # print(whichABExchange)
                    # # 再判断一遍以防万一
                    # if whichABExchange != -1:
                    #     tempNumberB = 0
                    #     tempNumberB = player_B_nowPos
                    #     player_B_nowPos = player_A_nowPos
                    #     player_A_nowPos = tempNumberB
                    # 玩家B走完之后开始计算是不是在互换格子上
                    canBSwitch = True
                    # 清屏幕下方的文字
                    StepNum().stepNum(playerNum, isPlayer_ATurn, True)
                    # 玩家B是否到达终点
                    if player_B_nowPos==34:
                        print("游戏结束")
                        aniGoingOn = False
                        # player_B_nowPos = 0
                        window.fill((15, 45, 79))
                        isGameOver = True
                        IsWin().isWin("PlayerB")
                        pygame.display.update()

                if isPlayer_ATurn==True:
                    isPlayer_ATurn=False
                else:
                    isPlayer_ATurn=True

                print("player_A_nowPos")
                print(player_A_nowPos)
                print("player_B_nowPos")
                print(player_B_nowPos)
                print(playerNum)
                print("isGameOver")
                print(isGameOver)

                if isGameOver!=True:
                    Tips().tips(isPlayer_ATurn)
                    aniGoingOn=True
                    pygame.display.update()
                    print(aniGoingOn)
                else:
                    aniGoingOn=False
                    isGameOver=True
                    print(aniGoingOn)

            if chr(event.key) == 'r' and isGameOver:
                window.fill((15, 45, 79))
                window.blit(new_player_A, (player_positions_01[0]))
                window.blit(new_player_B, (player_positions_01[0]))
                player_B_nowPos = 0
                player_A_nowPos=0
                aniGoingOn = True
                print(aniGoingOn)
                Mapping.map()  # 画地图
                Tips().tips(isPlayer_ATurn)
                print(isGameOver)
                isGameOver = False
