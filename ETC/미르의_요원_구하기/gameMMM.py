## 소프트웨어코딩 게임 만들기 과제
#  219124116 김주영

from tkinter import *
from tkinter import messagebox
from PIL import Image
import pygame
import random
import time
import os
window = Tk() # 윈도우 생성
window.title("미르의 요원 구하기") # 제목을 설정
window.iconbitmap("image/ico.ico")
window.geometry("1280x800") # 윈도우 크기 설정

myBulletSpeed = 18
wa_x = 65
wa_y = 60

pygame.init()
attackSound = pygame.mixer.Sound("sound/attack.wav")
saveSound = pygame.mixer.Sound("sound/succes.wav")
unsaveSound = pygame.mixer.Sound("sound/faill.wav")
manaupSound = pygame.mixer.Sound("sound/countup.wav")

class GameMain():
    def __init__(self):
        self.start = 1
        self.keys=set()
        self.canvas = Canvas(window, bg = "black")
        self.canvas.pack(expand=True,fill=BOTH)
        self.bgimage = PhotoImage(file="image/main.png")
        self.canvas.create_image(0,0, image = self.bgimage,anchor = NW,tags="bg")
        window.bind("<KeyPress>",self.keyPressHandler)
        window.bind("<KeyRelease>",self.keyReleaseHandler)
        pygame.mixer.music.load("sound/main.wav")
        pygame.mixer.music.play(-1)

        self.mainstanding = [PhotoImage(file='image/main_standing.gif', format = 'gif -index %d' %(i)) for i in range(12)]
        self.mainstandinga = self.canvas.create_image(950,480, image = self.mainstanding[0], tags = "mainstt")
        self.mainmid = 0
        self.cflag = 0
        while (self.cflag == 0):
            self.mainst()
            self.canvas.after(70)   
            self.canvas.update()
        self.canvas.destroy()

    def mainst(self):
        mainframes = self.mainstanding[self.mainmid]
        if (self.mainmid >= 11):
            self.mainmid = 0
        else: 
            self.mainmid += 1
        self.canvas.itemconfig(self.mainstandinga, image = mainframes)

    def keyPressHandler(self,event):
        self.keys.add(event.keycode)
        self.cflag = 1
        #print(self.keys)

    def keyReleaseHandler(self,event):
        if event.keycode in self.keys:
            self.keys.remove(event.keycode)
        

class GameExample():
    def __init__(self):
      
        window.resizable(0,0)
        window.wm_attributes('-topmost', 1)
        self.lastTime = time.time()
        self.lightingTimer = time.time()
        self.countTimeTimer = time.time()
        self.keys = set()
        self.canvas = Canvas(window, bg = "black")
        self.canvas.pack(expand = True, fill = BOTH)
        window.bind("<KeyPress>", self.keyPressHandler)
        window.bind("<KeyRelease>", self.keyReleaseHandler)
        pygame.mixer.music.load("sound/bgm.wav")
        pygame.mixer.music.play(-1)
        ## 사진 반전 후 저장 코드 *gif는 반전이 제대로 저장되지 않음*
        #roImage = Image.open("image/b_dragon2.png")
        #_roImage = roImage.transpose(Image.FLIP_LEFT_RIGHT)
        #_roImage.save('image/_b_dragon2.png')

        # 이미지

        self.myimage = [PhotoImage(file='image/my_image/move.gif', format = 'gif -index %d' %(i)) for i in range(12)]
        self._myimage = [PhotoImage(file='image/my_image/_move.gif', format = 'gif -index %d' %(i)) for i in range(12)]
        self.m_attack = [PhotoImage(file='image/my_image/attack.gif', format = 'gif -index %d' %(i)) for i in range(7)]
        self._m_attack = [PhotoImage(file='image/my_image/_attack.gif', format = 'gif -index %d' %(i)) for i in range(7)]
        self.b_dragon = [PhotoImage(file='image/w_blue_dragon/fly.gif', format = 'gif -index %d' %(i)) for i in range(6)]
        self._b_dragon = [PhotoImage(file='image/w_blue_dragon/_fly.gif', format = 'gif -index %d' %(i)) for i in range(6)]
        self.b_dragon2 = [PhotoImage(file='image/w_r_dragon/fly.gif', format = 'gif -index %d' %(i)) for i in range(6)]
        self._b_dragon2 = [PhotoImage(file='image/w_r_dragon/_fly.gif', format = 'gif -index %d' %(i)) for i in range(6)]
        self.b_dragon3 = [PhotoImage(file='image/w_b_dragon/fly.gif', format = 'gif -index %d' %(i)) for i in range(6)]
        self._b_dragon3 = [PhotoImage(file='image/w_b_dragon/_fly.gif', format = 'gif -index %d' %(i)) for i in range(6)]
        self.bossframes = [PhotoImage(file='image/disad/_endline1.gif', format = 'gif -index %d' %(i)) for i in range(37)]
        self.bossframes2 = [PhotoImage(file='image/disad/endline1.gif', format = 'gif -index %d' %(i)) for i in range(37)]
        self.helpimage = PhotoImage(file='image/help.png')

        self.fire = PhotoImage(file="image/fire.png")#[PhotoImage(file='image/my_image/1set.gif', format = 'gif -index %d' %(i)) for i in range(44)]
        self._fire = PhotoImage(file="image/_fire.png")#[PhotoImage(file='image/my_image/2set.gif', format = 'gif -index %d' %(i)) for i in range(4)]
        self.bullet = [PhotoImage(file='image/bullet/move.gif', format = 'gif -index %d' %(i)) for i in range(6)]
        self._bullet = [PhotoImage(file='image/bullet/_move.gif', format = 'gif -index %d' %(i)) for i in range(6)]

        #self.bossframes = [PhotoImage(file='image/m_dragon/m_move.gif', format = 'gif -index %d' %(i)) for i in range(6)]

        # 배경
        self.bgimage = PhotoImage(file="image/back/5.png")
        self.lighting = PhotoImage(file="image/back/sky_down.png")
        self.canvas.create_image(0,0, image = self.bgimage,anchor = NW,tags="bg")
        
        #frames = PhotoImage(file = "image/mygif.gif", format="gif -index 28")

        self.myMoveSpeed = 12.5
        ppos = 0
        self.myind = 0
        self.m_ind = 0
        self.red_mind = 0
        self.blue_mind = 0
        self.black_mind = 0
        self.boss_mind = 0
        self.boss_mind2 = 0
        self.ind = 0
        self.bullet1_ind = 0
        self.bullet2_ind = 0
        self.moveFlag = 1
        self.m_attack_ind = 0
        self.attackFlag = 0
        self.my_Stend_ind = 0
        self.isMove = 0
        self.saveCount = 0
        self.timeCount = 0
        self.manaCount = 15
        self.canAttack = 1
        self.nonsaveCount = 0
        self.gamePoint = 0
        self.dieFlag = 0
        self.mstimeCount = 0
        self.mstimehelpCount = 0
        self.playFlag = 0
        self.falseCount = 3
        self.createPFlag = 0
        self.playplayFlag = 0
        self.trueFlag = 1


        self.canvas.create_text(1100, 35, fill = "white", font = "Times 20 italic bold", text = "떨어지는 요원을 구하세요!")
        self.canvas.create_text(120, 50, fill ="white", font = "Times 30 italic bold", text = "구한 요원 수 :")
        self.canvas.create_text(300, 50, fill ="white", font = "Times 30 italic bold", text = "%d" % self.saveCount, tags = "saveCount")
        self.canvas.create_text(600, 50, fill ="white", font = "Times 30 bold", text = "경과 시간 :")
        self.canvas.create_text(750, 50, fill ="white", font = "Times 30 bold", text = "%d" % self.timeCount, tags = "timeCount")
        self.canvas.create_text(120, 100, fill ="white", font = "Times 30 italic bold", text = "남은 마법탄 :")
        self.canvas.create_text(300, 100, fill ="white", font = "Times 30 italic bold", text = "%d" % self.manaCount, tags = "manaCount")
        self.canvas.create_text(1000, 100, fill ="white", font = "Times 30 italic bold", text = "남은 목숨 :")
        self.canvas.create_text(1200, 100, fill ="white", font = "Times 30 italic bold", text = "%d" % self.falseCount, tags = "falseCount")
        
        

        #   생성을 나중에 하면 레이어 순서가 올라감 

        self.bossDragon = self.canvas.create_image(905, 695, image = self.bossframes[0], tags = "bossdragon")
        self.bossDragon2 = self.canvas.create_image(370, 695, image = self.bossframes2[0], tags = "bossdragon2")
        self.b_Dragon = self.canvas.create_image(300, 100, image = self.b_dragon[0], tags = "b_dragon")
        self.b_Dragon2 = self.canvas.create_image(800, 300, image = self.b_dragon2[0], tags = "b_dragon2")
        self.b_Dragon3 = self.canvas.create_image(1200, 200, image = self.b_dragon3[0], tags = "b_dragon3")
        self.myPlayer = self.canvas.create_image(90,480/2, image = self.myimage[0], tags = "dragon")

        self.helpImage = self.canvas.create_image(600, 400, image = self.helpimage, tags = "help")
        

        while (self.trueFlag == 1):
            #print(self.canvas.winfo_width())
            self.display()
            
            if(self.playplayFlag == 1):
                if(self.timeCount == 0):
                    self.countTime()
                self.createPFlag = 1
                self.canvas.delete(self.helpImage)
                self.ob_b_dragon1()
                self.ob_b_dragon2()
                self.ob_b_dragon3()
                

            self.ob_boss()
            self.ob_boss2()

            fires = self.canvas.find_withtag("fire")
            _fires = self.canvas.find_withtag("_fire")
            lightings = self.canvas.find_withtag("lighting")
            manaCount = self.canvas.find_withtag("manaCount")
            falseCount = self.canvas.find_withtag("falseCount")
            self.canvas.itemconfig(manaCount, text = "%d" % self.manaCount)
            self.canvas.itemconfig(falseCount, text = "%d" % self.falseCount)

            for fire in fires:
                self.canvas.move(fire, myBulletSpeed, 0)
                fire1Frame = self.bullet[self.bullet1_ind]
                if (self.bullet1_ind >= 5):
                    self.bullet1_ind = 0
                else: 
                    self.bullet1_ind += 1
                self.canvas.itemconfig(fire, image = fire1Frame)

                if self.canvas.coords(fire)[0] > self.canvas.winfo_width():
                    self.canvas.delete(fire)
                if fire in self.canvas.find_overlapping(self.b_dragonPos[0] - 35, self.b_dragonPos[1] - 35, self.b_dragonPos[0] + 35, self.b_dragonPos[1] + 40):
                    self.canvas.move(self.b_Dragon, 110, -40)
                    self.canvas.delete(fire)
                if fire in self.canvas.find_overlapping(self.b_dragon2Pos[0] - 35, self.b_dragon2Pos[1] - 35, self.b_dragon2Pos[0] + 35, self.b_dragon2Pos[1] + 40):
                    self.canvas.move(self.b_Dragon2, 110, -40)
                    self.canvas.delete(fire)
                if fire in self.canvas.find_overlapping(self.b_dragon3Pos[0] - 35, self.b_dragon3Pos[1] - 35, self.b_dragon3Pos[0] + 35, self.b_dragon3Pos[1] + 40):
                    self.canvas.move(self.b_Dragon3, 110, -40)
                    self.canvas.delete(fire)
                       
            for _fire in _fires:
                self.canvas.move(_fire, -myBulletSpeed, 0)
                fire2Frame = self._bullet[self.bullet2_ind]
                if (self.bullet2_ind >= 5):
                    self.bullet2_ind = 0
                else: 
                    self.bullet2_ind += 1
                self.canvas.itemconfig(_fire, image = fire2Frame)

                if self.canvas.coords(_fire)[0] < -20:
                    self.canvas.delete(_fire)
                if _fire in self.canvas.find_overlapping(self.b_dragonPos[0] - 35, self.b_dragonPos[1] - 35, self.b_dragonPos[0] + 35, self.b_dragonPos[1] + 40):
                    self.canvas.move(self.b_Dragon, -110, -40)
                    self.canvas.delete(_fire)
                if _fire in self.canvas.find_overlapping(self.b_dragon2Pos[0] - 35, self.b_dragon2Pos[1] - 35, self.b_dragon2Pos[0] + 35, self.b_dragon2Pos[1] + 40):
                    self.canvas.move(self.b_Dragon2, -110, -40)
                    self.canvas.delete(_fire)
                if _fire in self.canvas.find_overlapping(self.b_dragon3Pos[0] - 35, self.b_dragon3Pos[1] - 35, self.b_dragon3Pos[0] + 35, self.b_dragon3Pos[1] + 40):
                    self.canvas.move(self.b_Dragon3, -110, -40)
                    self.canvas.delete(_fire)
                       

            for lighting in lightings:
                lightingPos = self.canvas.coords(lighting)
                self.canvas.move(lighting, 0, 5)
                if lightingPos[1] > 600:
                    self.canvas.delete(lighting)
                    self.nonsaveCount += 1
                    pygame.mixer.Sound.play(unsaveSound)
                    self.falseCount -= 1
                    if self.falseCount == 0:
                        self.dieFlag = 5
                if self.myPlayer in self.canvas.find_overlapping(lightingPos[0] - 45, lightingPos[1] - 110, lightingPos[0] + 45, lightingPos[1] + 110):
                    self.canvas.delete(lighting)
                    self.saveCount += 1
                    if (self.saveCount != 0) and (self.saveCount % 10 == 0):
                        self.manaCount += 5
                        pygame.mixer.Sound.play(manaupSound)
                    if (self.saveCount != 0) and (self.saveCount % 30 == 0):
                        self.falseCount += 1
                        pygame.mixer.Sound.play(manaupSound)
                    saveCount = self.canvas.find_withtag("saveCount")
                    self.canvas.itemconfig(saveCount, text = "%d" % self.saveCount)
                    pygame.mixer.Sound.play(saveSound)
              

            m_attack_list = self.m_attack[self.m_attack_ind]
            _m_attack_list = self._m_attack[self.m_attack_ind]

            if self.attackFlag == 1:
                if self.m_attack_ind >= 6:
                    self.m_attack_ind = 0
                else:
                    self.m_attack_ind += 1

                if self.moveFlag == 1 and self.attackFlag == 1:
                    self.canvas.itemconfig(self.myPlayer, image = m_attack_list)
                    if m_attack_list == 6:
                        self.attackFlag = 0
                elif self.moveFlag == 0 and self.attackFlag == 1:
                    self.canvas.itemconfig(self.myPlayer, image = _m_attack_list)
                    if m_attack_list == 6:
                        self.attackFlag = 0
              
            stend_myFrame = self.myimage[self.my_Stend_ind]
            _stend_myFrame = self._myimage[self.my_Stend_ind]
            
            if ((self.attackFlag == 0) and (self.isMove == 0)):
                if (self.my_Stend_ind >= 11):
                    self.my_Stend_ind = 0
                else: 
                    self.my_Stend_ind += 1

                if(self.moveFlag == 1):
                    self.canvas.itemconfig(self.myPlayer, image = stend_myFrame)
                else:
                    self.canvas.itemconfig(self.myPlayer, image = _stend_myFrame)

            if self.pos[1] > 600:
                self.dieFlag = 1

            if self.dieFlag == 1:
                self.canvas.delete(self.myPlayer)
                self.gamePoint = self.saveCount * 50 + self.timeCount * 5 + self.manaCount * 150 - self.nonsaveCount * 10 
                messagebox.showinfo(title="게임 종료", message="미르가 동족 상위 계층에게 불타버렸습니다.\n\n\n구한 요원 수 : %d명\n\n경과 시간 : %d초\n\n그리고\n\n%d명의 요원이 죽었습니다.\n\n점수 : %d" % (self.saveCount, self.timeCount, self.nonsaveCount, self.gamePoint))
                break

            elif self.dieFlag == 2:
                self.canvas.delete(self.myPlayer)
                self.gamePoint = self.saveCount * 50 + self.timeCount * 5 + self.manaCount * 150 - self.nonsaveCount * 10 
                messagebox.showinfo(title="게임 종료", message="미르가 블루와이번의 날카로운 발톱에 찢겨 죽었습니다.\n\n\n구한 요원 수 : %d명\n\n경과 시간 : %d초\n\n그리고\n\n%d명의 요원이 죽었습니다.\n\n점수 : %d" % (self.saveCount, self.timeCount, self.nonsaveCount, self.gamePoint))
                break

            elif self.dieFlag == 3:
                self.canvas.delete(self.myPlayer)
                self.gamePoint = self.saveCount * 50 + self.timeCount * 5 + self.manaCount * 150 - self.nonsaveCount * 10 
                messagebox.showinfo(title="게임 종료", message="미르가 레드와이번의 예리한 날개에 잘려 죽었습니다.\n\n\n구한 요원 수 : %d명\n\n경과 시간 : %d초\n\n그리고\n\n%d명의 요원이 죽었습니다.\n\n점수 : %d" % (self.saveCount, self.timeCount, self.nonsaveCount, self.gamePoint))
                break

            elif self.dieFlag == 4:
                self.canvas.delete(self.myPlayer)
                self.gamePoint = self.saveCount * 50 + self.timeCount * 5 + self.manaCount * 150 - self.nonsaveCount * 10 
                messagebox.showinfo(title="게임 종료", message="미르가 블랙와이번의 뾰족한 송곳니에 찍혀 죽었습니다.\n\n\n구한 요원 수 : %d명\n\n경과 시간 : %d초\n\n그리고\n\n%d명의 요원이 죽었습니다.\n\n점수 : %d" % (self.saveCount, self.timeCount, self.nonsaveCount, self.gamePoint))
                break

            elif self.dieFlag == 5:
                self.canvas.delete(self.myPlayer)
                self.gamePoint = self.saveCount * 50 + self.timeCount * 5 + self.manaCount * 150 - self.nonsaveCount * 10 
                messagebox.showinfo(title="게임 종료", message="요원 구출에 실패했습니다.\n\n\n구한 요원 수 : %d명\n\n경과 시간 : %d초\n\n그리고\n\n%d명의 요원이 죽었습니다.\n\n점수 : %d" % (self.saveCount, self.timeCount, self.nonsaveCount, self.gamePoint))
                break
                
            #self.canvas.find_overlapping
            #
            #print("x는 ", self.pos[0], "y는 ", self.pos[1])

            self.canvas.after(45)   
            self.canvas.update() # 캔버스를 업데이트

        self.canvas.destroy()
        GameDie()


    # 안됨;;;;
    def truetime(self, mstime = 3):
        self.mstimeCount += 1
        print("실행")
        if self.mstimeCount == mstime:
            self.mstimeCount = 0
            return 1
        else:
            self.canvas.after(1000, self.truetime)

    def ob_boss(self):
        bDragonFrame = self.bossframes[self.boss_mind]
        self.boss1pos = self.canvas.coords(self.bossDragon)
        if (self.boss_mind >= 36):
            self.boss_mind = 0
        else: 
            self.boss_mind += 1

        self.canvas.itemconfig(self.bossDragon, image = bDragonFrame)

    def ob_boss2(self):
        bDragonFrame2 = self.bossframes2[self.boss_mind2]
        self.boss2pos = self.canvas.coords(self.bossDragon2)
        if (self.boss_mind2 >= 36):
            self.boss_mind2 = 0
        else: 
            self.boss_mind2 += 1

        self.canvas.itemconfig(self.bossDragon2, image = bDragonFrame2)
    
    def ob_b_dragon1(self):
        b_dragonSpeed = 5.5
        bDragonFrame = self.b_dragon[self.blue_mind]
        _bDragonFrame = self._b_dragon[self.blue_mind]

        if (self.blue_mind >= 5):
            self.blue_mind = 0
        else: 
            self.blue_mind += 1

        if (self.pos > self.b_dragonPos):
            self.canvas.itemconfig(self.b_Dragon, image = bDragonFrame)
        else:
            self.canvas.itemconfig(self.b_Dragon, image = _bDragonFrame)

        if (self.pos[0] > self.b_dragonPos[0] and self.pos[1] < self.b_dragonPos[1]):
            self.canvas.move(self.b_Dragon, b_dragonSpeed, -b_dragonSpeed)
        elif (self.pos[0] < self.b_dragonPos[0] and self.pos[1] < self.b_dragonPos[1]):
            self.canvas.move(self.b_Dragon, -b_dragonSpeed, -b_dragonSpeed)
        elif (self.pos[0] < self.b_dragonPos[0] and self.pos[1] > self.b_dragonPos[1]):
            self.canvas.move(self.b_Dragon, -b_dragonSpeed, +b_dragonSpeed)
        elif (self.pos[0] > self.b_dragonPos[0] and self.pos[1] > self.b_dragonPos[1]):
            self.canvas.move(self.b_Dragon, b_dragonSpeed, b_dragonSpeed)
        else:
            self.canvas.move(self.b_Dragon, 0, 0) 
            
        self.canvas.move(self.b_Dragon, 0, 0.9) 

        if self.myPlayer in self.canvas.find_overlapping(self.b_dragonPos[0] - 35, self.b_dragonPos[1] - 35, self.b_dragonPos[0] + 35, self.b_dragonPos[1] + 40):
                self.dieFlag = 2

    
    def ob_b_dragon2(self):
        b_dragon2Speed = 3    
        bDragon2Frame = self.b_dragon2[self.red_mind]
        _bDragon2Frame = self._b_dragon2[self.red_mind]

        if (self.red_mind >= 5):
            self.red_mind = 0
        else: 
            self.red_mind += 1

        if (self.pos > self.b_dragon2Pos):
            self.canvas.itemconfig(self.b_Dragon2, image = bDragon2Frame)
        else:
            self.canvas.itemconfig(self.b_Dragon2, image = _bDragon2Frame)

        if (self.pos[0] > self.b_dragon2Pos[0] and self.pos[1] < self.b_dragon2Pos[1]):
            self.canvas.move(self.b_Dragon2, b_dragon2Speed, -b_dragon2Speed)
        elif (self.pos[0] < self.b_dragon2Pos[0] and self.pos[1] < self.b_dragon2Pos[1]):
            self.canvas.move(self.b_Dragon2, -b_dragon2Speed, -b_dragon2Speed)
        elif (self.pos[0] < self.b_dragon2Pos[0] and self.pos[1] > self.b_dragon2Pos[1]):
            self.canvas.move(self.b_Dragon2, -b_dragon2Speed, +b_dragon2Speed)
        elif (self.pos[0] > self.b_dragon2Pos[0] and self.pos[1] > self.b_dragon2Pos[1]):
            self.canvas.move(self.b_Dragon2, b_dragon2Speed, b_dragon2Speed)
        else:
            self.canvas.move(self.b_Dragon2, 0, 0) 

        self.canvas.move(self.b_Dragon2, 0, 0.9)  

        if ((self.pos[0] > self.b_dragon2Pos[0] - wa_x) and (self.pos[1] > self.b_dragon2Pos[1] - wa_y) and (self.pos[0] < self.b_dragon2Pos[0] + wa_x) and (self.pos[1] < self.b_dragon2Pos[1] + wa_y)):
            self.dieFlag = 3

    def ob_b_dragon3(self):
        b_dragon3Speed = 1.2 
        bDragon3Frame = self.b_dragon3[self.black_mind]
        _bDragon3Frame = self._b_dragon3[self.black_mind]

        if (self.black_mind >= 5):
            self.black_mind = 0
        else: 
            self.black_mind += 1

        if (self.pos > self.b_dragon3Pos):
            self.canvas.itemconfig(self.b_Dragon3, image = bDragon3Frame)
        else:
            self.canvas.itemconfig(self.b_Dragon3, image = _bDragon3Frame)

        if (self.pos[0] > self.b_dragon3Pos[0] and self.pos[1] < self.b_dragon3Pos[1]):
            self.canvas.move(self.b_Dragon3, b_dragon3Speed, -b_dragon3Speed)
        elif (self.pos[0] < self.b_dragon3Pos[0] and self.pos[1] < self.b_dragon3Pos[1]):
            self.canvas.move(self.b_Dragon3, -b_dragon3Speed, -b_dragon3Speed)
        elif (self.pos[0] < self.b_dragon3Pos[0] and self.pos[1] > self.b_dragon3Pos[1]):
            self.canvas.move(self.b_Dragon3, -b_dragon3Speed, +b_dragon3Speed)
        elif (self.pos[0] > self.b_dragon3Pos[0] and self.pos[1] > self.b_dragon3Pos[1]):
            self.canvas.move(self.b_Dragon3, b_dragon3Speed, b_dragon3Speed)
        else:
            self.canvas.move(self.b_Dragon3, 0, 0) 

        self.canvas.move(self.b_Dragon3, 0, 0.9)

        if (self.pos[0] > self.b_dragon3Pos[0] -wa_x and self.pos[1] > self.b_dragon3Pos[1] - wa_y and self.pos[0] < self.b_dragon3Pos[0] + wa_x and self.pos[1] < self.b_dragon3Pos[1] + wa_y):
            self.dieFlag = 4
    
    def countTime(self):
        timeCount = self.canvas.find_withtag("timeCount")
        self.canvas.itemconfig(timeCount, text = "%d" % self.timeCount)
        self.timeCount += 1
        self.slowSpeed = self.timeCount * 0.001
        self.myMoveSpeed -= self.slowSpeed
        self.canvas.after(1000, self.countTime)
        
      
    def keyReleaseHandler(self, event):
        if event.keycode in self.keys:
            self.keys.remove(event.keycode)

    def display(self):
        myFrame = self.myimage[self.myind]
        _myFrame = self._myimage[self.myind]

        if (self.myind >= 11):
            self.myind = 0
        else: 
            self.myind += 1

            if(self.moveFlag == 1):
                self.canvas.itemconfig(self.myPlayer, image = myFrame)
            else:
                self.canvas.itemconfig(self.myPlayer, image = _myFrame)

        dragon = self.canvas.find_withtag("dragon")
        #b_Dragon = self.canvas.find_withtag("b_dragon")
        #b_Dragon2 = self.canvas.find_withtag("b_dragon2")
        
        self.canvas.move(dragon, 0, 0.9)
        self.pos = self.canvas.coords(dragon)

        self.b_dragonPos = self.canvas.coords(self.b_Dragon)
        self.b_dragon2Pos = self.canvas.coords(self.b_Dragon2)
        self.b_dragon3Pos = self.canvas.coords(self.b_Dragon3)

        for key in self.keys:
            if key == 39:   # right
                self.canvas.move(dragon, self.myMoveSpeed, 0)
                self.moveFlag = 1
                self.isMove = 1
            else:
                self.isMove = 0

            if key == 37:   # left
                self.canvas.move(dragon, -self.myMoveSpeed, 0)
                self.moveFlag = 0
                self.isMove = 1
            else:
                self.isMove = 0
            if key == 38:   # down
                self.canvas.move(dragon, 0, -self.myMoveSpeed)
                self.isMove = 1
            else:
                self.isMove = 0
            if key == 40:   # up
                self.canvas.move(dragon, 0, self.myMoveSpeed)
                self.isMove = 1
            else:
                self.isMove = 0

            if self.manaCount >= 1:
                self.canAttack = 1

            if key == 32 and self.canAttack == 1:   # space
                self.attackFlag = 1
                now = time.time()
                if(now - self.lastTime) > 0.5:
                    self.manaCount -= 1
                    self.lastTime = now
                    manaCount = self.canvas.find_withtag("manaCount")
                    pygame.mixer.Sound.play(attackSound)
                    if self.manaCount == 0:
                        self.canAttack = 0
                    if(self.moveFlag == 1):
                        self.canvas.create_image(self.pos[0] + 60, self.pos[1] + 17, image = self.fire, tags = "fire")
                    else:
                        self.canvas.create_image(self.pos[0] - 60, self.pos[1] + 17, image = self._fire, tags = "_fire")
            
            if key != 32:
                self.attackFlag = 0
                        
        if(self.lightingTimer == -1):
            self.lightingTimer = time.time()
            for i in range(0, 1):
                if(self.createPFlag == 1):
                    self.canvas.create_image(random.randint(0,self.canvas.winfo_width()),0, image = self.lighting, anchor = CENTER, tags="lighting")
        else:
            now = time.time()
            if(now - self.lightingTimer > 2.0):
                self.lightingTimer = -1
            
    def keyPressHandler(self, event):
        #print(event.keycode)
        self.keys.add(event.keycode)
        self.playplayFlag = 1

class GameDie():
    def __init__(self):
        self.start = 1
        self.keys=set()
        self.canvas = Canvas(window, bg = "black")
        self.canvas.pack(expand=True,fill=BOTH)
        self.bgimage = PhotoImage(file="image/die.png")
        self.canvas.create_image(0,0, image = self.bgimage,anchor = NW,tags="bg")
        window.bind("<KeyPress>",self.keyPressHandler)
        window.bind("<KeyRelease>",self.keyReleaseHandler)
        pygame.mixer.music.load("sound/die.wav")
        pygame.mixer.music.play(-1)

        self.mainstanding = [PhotoImage(file='image/_die.gif', format = 'gif -index %d' %(i)) for i in range(12)]
        self.mainstandinga = self.canvas.create_image(1280/2,520, image = self.mainstanding[0], tags = "mainstt")
        self.mainmid = 0
        self.cflag = 0
        while (self.cflag == 0):
            self.mainst()
            self.canvas.after(45)   
            self.canvas.update()
        self.canvas.destroy()
        GameExample()

    def mainst(self):
        mainframes = self.mainstanding[self.mainmid]
        if (self.mainmid >= 11):
            self.mainmid = 0
        else: 
            self.mainmid += 1
        self.canvas.itemconfig(self.mainstandinga, image = mainframes)
        for key in self.keys:
            if(key == 82):
                self.cflag = 1


    def keyPressHandler(self,event):
        self.keys.add(event.keycode)
        
    def keyReleaseHandler(self,event):
        if event.keycode in self.keys:
            self.keys.remove(event.keycode)
        


GameMain()
GameExample()
