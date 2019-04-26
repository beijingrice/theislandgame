import sys
import random
import json
import os
import time as ptime
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import threading
import pickle
import datetime
import turtle
class pig():
    def __init__(self):
        self.x = random.randint(0,500)
        self.y = random.randint(0,500)
        self.blood = 20
class cow():
    def __init__(self):
        self.x = random.randint(0,500)
        self.y = random.randint(0,500)
        self.blood = 20
class sheep():
    def __init__(self):
        self.x = random.randint(0,500)
        self.y = random.randint(0,500)
        self.blood = 20
class snake():
    def __init__(self):
        self.x = random.randint(0,500)
        self.y = random.randint(0,500)
        self.blood = 20
class player():
    def __init__(self):
        self.weather = random.choice(["sunny","cloudly","rainy","snowy","thunder"])
        self.armerpoint = 0
        self.armerhead = None
        self.armerchest = None
        self.armerleg = None
        self.armerfoot = None
        self.hand = None
        self.time = [random.randint(0,23),random.randint(0,59)]
        self.x = random.randint(0,500)
        self.y = random.randint(0,500)
        self.backpack = []
        self.blood = 20
        self.food = 20
        self.water = 20
        self.allplayerthing = ["小刀","打火石","剑","绳子","椰子","牛肉罐头","金枪鱼罐头","辣椒","纸","笔","木棍","木板","淡水","头盔","胸甲","腿甲","靴子"]
        self.map = []
        self.postype = ["沙滩","地面","雨林","海洋"]
        self.mapthing = ["石头","沙子","淡水","椰子树","香蕉树"]
        self.sheepanimal = []
        self.cowanimal = []
        self.snakeanimal = []
        self.piganimal = []
        self.allanimal = []
        self.snakeanimal = []
        self.starttext = """
                 _
                / \                                 _
                | |                                / /
                | |                               /_/ 
           __   | |   ___                     _____________
          /  /  | |   \  \                   |  ________  |
         /  /   | |    \  \                  | |        | |
        /  /    | |     \  \                 | |  __    | |
       /__/     | |      \__\                | |  \ \  _| |
                | |                          | |   \_\ \  |
                | |                          | |        \_|
                | |                          | |___________
           __   | |                          |___________  |
           \ \  | |                             _        | |
            \ \ | |                         _  | |  _  _ | |
             \ \| |                        | |_| |_| |\ \| |
              \   |                        |_________| \   |
               \__|                                     \__|
欢迎来到小岛！。。。
"""
    def start(self):
        try:
            os.chdir("C:\\")
        except:
            try:
                os.chdir("D:\\")
            except:
                try:
                    os.chdir("E:\\")
                except:
                    sys.exit()
        ok = False
        print(self.starttext)
        while ok == False:
            level = input("设定游戏难度\n1 - 简单\n2 - 中等\n3 - 困难\n")
            if level == "1":
                return "easy"
                ok = True
                break
            if level == "2":
                return "middle"
                ok = True
                break
            if level == "3":
                return "hard"
                ok = True
                break
    def mapcreate(self):
        timer = 0
        for y in range(501):            
            for x in range(501):            
                first = random.choice(self.postype)
                if first == "海洋":
                    secode = None
                if first != "海洋":
                    secode = random.choice(self.mapthing)
                self.map.append((x,y,first,secode))
                timer += 1
        filename = tkinter.filedialog.asksaveasfilename(title="存储游戏存档") + ".dat"
        try:
            savefile = open(filename,"wb+")
            pickle.dump(self.map,savefile)
            savefile.close()
        except:
            print("存储游戏存档时出现问题！")
        print("存档创建完成！")
    def createsummon(self):
        for x in range(1):
            sheep1 = sheep()
            sheep2 = sheep()
            sheep3 = sheep()
            sheep4 = sheep()
            sheep5 = sheep()
            sheep6 = sheep()
            sheep7 = sheep()
            sheep8 = sheep()
            sheep9 = sheep()
            sheep10 = sheep()
            self.sheepanimal = [sheep1,sheep2,sheep3,sheep4,sheep5,sheep6,sheep7,sheep8,sheep9,sheep10]
            pig1 = pig()
            pig2 = pig()
            pig3 = pig()
            pig4 = pig()
            pig5 = pig()
            pig6 = pig()
            pig7 = pig()
            pig8 = pig()
            pig9 = pig()
            pig10 = pig()
            self.piganimal = [pig1,pig2,pig3,pig4,pig5,pig6,pig7,pig8,pig9,pig10]
            cow1 = cow()
            cow2 = cow()
            cow3 = cow()
            cow4 = cow()
            cow5 = cow()
            cow6 = cow()
            cow7 = cow()
            cow8 = cow()
            cow9 = cow()
            cow10 = cow()
            self.cowanimal = [cow1,cow2,cow3,cow4,cow5,cow6,cow7,cow8,cow9,cow10]
            snake1 = snake()
            snake2 = snake()
            snake3 = snake()
            snake4 = snake()
            snake5 = snake()
            self.snakeanimal = [snake1,snake2,snake3,snake4,snake5]
            for name in self.sheepanimal:
                self.allanimal.append(name)
            for name in self.piganimal:
                self.allanimal.append(name)
            for name in self.cowanimal:
                self.allanimal.append(name)
            allanimal = self.allanimal
            def threadmainanimalcontrolsfunction():
                global allanimal
                for name in self.allanimal:
                    direction = random.choice(["up","down","right","left"])
                    if direction == "up":
                        name.y -= 1
                    if direction == "down":
                        name.y += 1
                    if direction == "left":
                        name.x -= 1
                    if direction == "right":
                        name.x += 1
            threadmaincontrolanimal = threading.Thread(target=threadmainanimalcontrolsfunction)
            threadmaincontrolanimal.start()
            threadmaincontrolanimal.join()
if __name__ == "__main__":
    player1 = player()
    def timecheck():                                                                                                
        checker = 0
        hour = player1.time[0]
        minute = player1.time[1]
        if hour == 7 and minute == 0:
            player1.weather = random.randint(["sunny","cloudly","rainy","snowy","thunder"])
        if minute >= 59:
            player1.time[1] = 0     #BUG为这些控制游戏时间的代码没有执行，但检查血量的代码却持续执行
            player1.time[0] = player1.time[0] + 1
        if player1.water <= 5:
            print("您缺水了，正在掉血\n")
            player1.blood -= 1
            checker = 0
        if player1.food <= 5:
            print("您太饿了，正在掉血\n")
            player1.blood -= 1
            checker = 0                                                                                        
    print(player1.starttext)
    while True:
        ctrl = input("您要执行什么操作？\n1 - 打开存档\n2 - 新建存档\n3 - 退出\n")
        if ctrl == "2":
            level = player1.start()
            if level == "easy":
                for x in range(30):
                    player1.backpack.append((random.choice(player1.allplayerthing),random.randint(0,64)))
            if level == "middle":
                for x in range(20):
                    player1.backpack.append((random.choice(player1.allplayerthing),random.randint(0,32)))
            if level == "hard":
                for x in range(5):
                    player1.backpack.append((random.choice(player1.allplayerthing),random.randint(0,16)))
            tk = Tk()
            filenameX = tkinter.filedialog.asksaveasfilename(title="保存您的背包文件") + ".dat"
            try:
                savefile = open(filename,"rb")
                pickle.dump(player1.backpack,savefile)
                savefile.close()
            except:
                print("保存背包时出现错误！")
            tk.withdraw()
            try:
                tk.destroy()
            except:
                try:
                    del tk
                except:
                    pass
            tk = Tk()
            filename = tkinter.filedialog.asksaveasfilename(title="存储游戏存档") + ".dat"
            tk.withdraw()
            def mapcreate():
                global filename
                cmd = input("您想查看地图生成的细节吗？(Y/N）").upper()
                timer = 0
                for y in range(501):            
                    for x in range(501):            
                        first = random.choice(player1.postype)
                        if first == "海洋":
                            secode = None
                        if first != "海洋":
                            secode = random.choice(player1.mapthing)
                        tumple = (x,y,first,secode)
                        player1.map.append(tumple)
                        if cmd == "Y":
                            print(tumple)
                        if cmd == "N":
                            nownumber = y/5
                            if nownumber == int(nownumber):
                                print(str(int(nownumber))+"%")
                            if nownumber != int(nownumber):
                                print(str(nownumber)+"%")
                        timer += 1
                try:
                    savefile = open(filename,"wb+")
                    pickle.dump(player1.map,savefile)
                    savefile.close()
                    return None
                except:
                    print("存储游戏存档时出现问题！")
                    return None
            mapcreatethread = threading.Thread(target=mapcreate)
            mapcreatethread.start()
            mapcreatethread.join()
            print("存档创建完成！")
            break
        if ctrl == "1":
            tk = Tk()
            filename = tkinter.filedialog.askopenfilename(title="打开新存档",filetypes=[("游戏存档","*.dat")])
            tk.withdraw()
            def opendata():
                global filename
                try:
                    loadfile = open(filename,"rb")
                    gamemap = pickle.load(loadfile)
                    loadfile.close()
                    player1.map = gamemap
                except:
                    print("出现错误！您可以输入2来创建新存档")
            opendatathread = threading.Thread(target=opendata)
            opendatathread.start()
            opendatathread.join()
            filenameX = tkinter.filedialog.askopenfilename(title="打开背包文件",filetypes=[("打开背包文件","*.dat")])
            try:
                loadfile = open(filenameX,"rb")
                backpack = pickle.load(loadfile)
                loadfile.close()
                player1.backpack = backpack
                break
            except:
                try:
                    if level == "easy":
                        for x in range(30):
                            player1.backpack.append((random.choice(player1.allplayerthing),random.randint(0,64)))
                    if level == "middle":
                        for x in range(20):
                            player1.backpack.append((random.choice(player1.allplayerthing),random.randint(0,32)))
                    if level == "hard":
                        for x in range(5):
                            player1.backpack.append((random.choice(player1.allplayerthing),random.randint(0,16)))
                    break
                except:
                    for x in range(30):
                        player1.backpack.append((random.choice(player1.allplayerthing),random.randint(0,64)))
                    break
        if ctrl == "3":
            sys.exit()
            quit()
    timemessagedisplay = True
    player1.createsummon()
    while True:
        if player1.time[0] >= 18 and player1.time[0] <= 23 or player1.time[0] >= 0 and player1.time[0] <= 6 and timemessagedisplay == True:
            print("夜晚已经降临。。。您可以睡觉或生火。。。")
            timemessagedisplay = False
        if player1.time[0] >= 7 and player1.time[0] <= 17:
            timemessagedisplay = True
        try:
            for name in player1.allanimal:
                if name.x > xmin and name.x < xmax:
                    if name.y > ymin and name.y < ymax:
                        print("附近有中立生物")
                        tkinter.messagebox.showinfo("小岛","附近有中立生物")
            for name in player1.snakeanimal:
                if name.x > xmin and name.x < xmax:
                    if name.y > ymin and name.y < ymax:
                        tkinter.messagebox.showwarning("小岛","附近有蛇！！！")
                        print("附近有蛇！！！")
                        while True:
                            cmd = input("您要逃跑还是要战斗？\n逃跑 - 0\n战斗 - 1\n")
                            if cmd == "0":
                                player1.x = player1.x + 20
                            if cmd == "1" and fire == True:
                                player1.backpack.append(("生蛇肉",1))
                                player1.snakeanimal.remove(name)
                            elif cmd == "1":
                                cmd = random.choice(["player win","snake win"])
                                if cmd == "player win":
                                    player1.backpack.append(("生蛇肉",1))
                                    player1.snakeanimal.remove(name)
                                if cmd == "snake win":
                                    player1.blood = player1.blood - 2
        except NameError:
            print("此功能还在开发中......\n请过一段时间再下载最新版试试看")
        x = player1.x
        y = player1.y
        xmin = x - 2
        ymin = y - 2
        xmax = x + 2
        ymax = y + 2
        main = input(">>> ")
        timecheck()
        player1.checksummon()
        if main == "睡觉":
            print("正在睡觉。。。")
            ptime.sleep(10) 
            player1.time[0] = 7
            player1.time[1] = 0
            print("到早上了！")
        if main == "生火":
            mainX = input("您想使用什么生火方法？\n1 - 打火石\n2 - 摩擦生火\n3 - 火弓法\n")
            if mainX == "1":
                for name in player1.backpack:
                    if name[0] == "打火石":
                        print("正在生火。。。")
                        ptime.sleep(10)
                        print("生火完成！")
                        for name in player1.backpack:
                            if name[0] == "打火石":
                                oldtumple = player1.backpack.pop(name)
                                if oldtumple[1] == 1:
                                    break
                                if oldtumple[1] > 1:
                                    newtumple = (oldtumple[0],oldtumple[1] - 1)
                                    player1.backpack.append(newtumple)
                                    break
                    fire = True
            if mainX == "2":
                for name in player1.backpack:
                    if name[0] == "木棍":
                        lookafter = True
                    if lookafter == True:
                        del lookafter
                        for name in player1.backpack:
                            if name[0] == "木板":
                                print("正在摩擦生火。。。")
                                ptime.sleep(20)
                                print("生火完成！")
                                player1.water -= 2
                                player1.food -= 1
                                for name in player1.backpack:
                                    if name[0] == "木棍":
                                        oldtumple = player1.backpack.pop(name)
                                        if oldtumple[1] == 1:
                                            break
                                        if oldtumple[1] > 1:
                                            newtumple = (oldtumple[0],oldtumple[1] - 1)
                                            player1.backpack.append(newtumple)
                                            break
                                for name in player1.backpack:
                                    if name[0] == "木板":
                                        oldtumple = player1.backpack.pop(name)
                                        if oldtumple[1] == 1:
                                            break
                                        if oldtumple[1] > 1:
                                            newtumple = (oldtumple[0],oldtumple[1] - 1)
                                            player1.backpack.append(newtumple)
                                            break
                            fire = True
            if mainX == "3":
                for name in player1.backpack:
                    if name[0] == "木棍":
                        lookafter = True
                if lookafter == True:
                    del lookafter
                    for name in player1.backpack:
                        if name[0] == "木板":
                            lookafter = True
                if lookafter == True:
                    del lookafter
                    for name in player1.backpack:
                        if name[0] == "绳子":
                            print("正在制作火弓。。。")
                            ptime.sleep(5)
                            print("正在生火。。。")
                            ptime.sleep(5)
                            print("完成！")
                            for name in player1.backpack:
                                if name[0] == "木棍":
                                    oldtumple = player1.backpack.pop(player1.backpack.index(name))
                                    if oldtumple[1] == 1:
                                        break
                                    if oldtumple[1] > 1:
                                        newtumple = (oldtumple[0],oldtumple[1] - 1)
                                        player1.backpack.append(newtumple)
                                        break
                            for name in player1.backpack:
                                if name[0] == "木板":
                                    oldtumple = player1.backpack.pop(player1.backpack.index(name))
                                    if oldtumple[1] == 1:
                                        break
                                    if oldtumple[1] > 1:
                                        newtumple = (oldtumple[0],oldtumple[1] - 1)
                                        player1.backpack.append(newtumple)
                                        break
                            for name in player1.backpack:
                                if name[0] == "绳子":
                                    oldtumple = player1.backpack.pop(player1.backpack.index(name))
                                    if oldtumple[1] == 1:
                                        break
                                    if oldtumple[1] > 1:
                                        newtumple = (oldtumple[0],oldtumple[1] - 1)
                                        player1.backpack.append(newtumple)
                                        break
                        fire = True
        if main == "查看状态":
            print("血量：",player1.blood)
            print("饥饿值：",player1.food)
            print("饮水度：",player1.water)
            print("位置：","x：",player1.x,"y：",player1.y)
            print("时间：",str(player1.time[0])+":"+str(+player1.time[1]))
            print("主手：",player1.hand)
            x = player1.x
            y = player1.y
            for name in player1.map:
                if name[0] == x and name[1] == y:
                    print("类型：",name[2],"资源：",name[3])
        if main == "移动":
            cmdcmd = input("输入 上 或 下 或 左 或 右")
            if cmdcmd == "上":
                cmdX = int(input("距离："))
                oldy = player1.y
                player1.y = player1.y - cmdX
                if player1.y <= 0:
                    player1.y = 0
                player1.water -= int((oldy - player1.y)/200)
                player1.food -= int((oldy - player1.y)/200)
                del oldy
            if cmdcmd == "下":
                cmdX = int(input("距离："))
                oldy = player1.y
                player1.y = player1.y + cmdX
                if player1.y >= 500:
                    player1.y = 500
                player1.water -= int((player1.y - oldy)/200)
                player1.water -= int((player1.y - oldy)/200)
                del oldy
            if cmdcmd == "左":
                cmdX = int(input("距离："))
                oldx = player1.x
                player1.x = player1.x - cmdX
                if player1.x <= 0:
                    player1.x = 0
                player1.water -= int((oldx - player1.x)/200)
                player1.food -= int((oldx - player1.x)/200)
                del oldx
            if cmdcmd == "右":
                cmdX = int(input("距离："))
                oldx = player1.x
                player1.x = player1.x + cmdX
                if player1.x >= 500:
                    player1.x = 500
                player1.water -= int((player1.x - oldx)/200)
                player1.food -= int((player1.x - oldx)/200)
        if main == "资源":
            li = []
            for name in player1.map:
                X = name[0]
                Y = name[1]
                if X >= (x - 2) and Y >= (y - 2) and X <= (x + 2) and Y <= (y + 2):
                    li.append(name)
            for name in li:
                last = name[3]
                if last == None:
                    last = "什么都没有"
                print("在x:"+str(name[0])+"y:"+str(name[1])+"类型为:"+name[2]+"的土地上，有:"+last)
            try:
                time = int(input("您想要几件物品？输入数字："))
            except:
                print("输入有误！")
            if time != 0:
                for x in range(time):
                    thing = input("您想要什么？")
                    for name in li:
                        if name[3] == thing:
                            if name[3] == "香蕉树" and player1.hand == "斧头":
                                location = player1.map.index(name)
                                tumple = player1.map.pop(location)
                                newtumple = (tumple[0],tumple[1],tumple[2],None)
                                player1.map.insert(location,newtumple)
                                player1.backpack.append(("香蕉",5))
                            if name[3] == "香蕉树" and player1.hand != "斧头":
                                print("您手中没有斧头，无法砍树")
                            if name[3] == "椰子树" and player1.hand == "斧头":
                                location = player1.map.index(name)
                                tumple = player1.map.pop(location)
                                newtumple = (tumple[0],tumple[1],tumple[2],None)
                                player1.map.insert(location,newtumple)
                                player1.backpack.append(("椰子",5))
                            if name[3] == "椰子树" and player1.hand != "斧头":
                                print("您手中没有斧头，无法砍树")
                            if name[3] != "椰子树" and name[3] != "香蕉树":
                                location = player1.map.index(name)
                                tumple = player1.map.pop(location)
                                newtumple = (tumple[0],tumple[1],tumple[2],None)
                                player1.map.insert(location,newtumple)
                                player1.backpack.append((name[3],1))
                            if "house" in name[3]:
                                cmd = input("您想进入这个房子吗？")
                                if cmd == "Y":
                                    player1.x = name[0]
                                    player1.y = name[1]
                                    print("您已经进入了这个房子。")
                                if cmd == "N":
                                    pass
        if main == "查看背包":
            print(player1.backpack)
        if main == "退出":
            quit()
        if main == "退出并保存":
            if player1.armerhead != None:
                player1.backpack.append((player1.armerhead,1))
            if player1.armerchest != None:
                player1.backpack.append((player1.armerchest,1))
            if player1.armerleg != None:
                player1.backpack.append((player1.armerleg,1))
            if player1.armfoot != None:
                player1.backpack.append((player1.armerfoot,1))
            filename = tkinter.filedialog.asksaveasfilename(title="保存游戏地图") + ".dat"
            savefile = open(filename,"wb+")
            pickle.dump(player1.map,savefile)
            savefile.close()
            del filename
            del savefile
            filename = tkinter.filedialog.asksaveasfilename(title="保存玩家背包") + ".dat"
            savefile = open(filename,"wb+")
            pickle.dump(player1.backpack,savefile)
            savefile.close()
            quit()
        if main == "绘制地图":
            t = turtle.Pen()
            timer = 0
            t.penup()
            t.left(90)
            t.forward(200)
            t.left(90)
            t.forward(200)
            t.left(180)
            t.pendown()
            t.speed(10)
            t.pensize(4)
            for x in range(501):
                for x in range(501):
                    tumple = player1.map[timer]
                    if tumple[2] == "海洋":
                        t.pencolor("blue")
                    if tumple[2] == "沙滩":
                        t.pencolor("yellow")
                    if tumple[2] == "地面":
                        t.pencolor("grey")
                    if tumple[2] == "雨林":
                        t.pencolor("green")
                    for x in range(4):
                        t.begin_fill()
                        t.forward(4)
                        t.right(90)
                    t.forward(8)
                    t.end_fill()
                    timer += 1
                t.right(90)
                t.penup()
                t.forward(1)
                t.right(90)
                t.forward(501)
                t.left(180)
                t.pendown()
        if main == "喝水":
            timer = 0
            for name in player1.backpack:
                if name[0] == "淡水":
                    print("已经喝水！")
                    tumple = player1.backpack.pop(timer)
                    newtumple = (tumple[0],tumple[1] - 1)
                    if newtumple[1] > 0:
                        player1.backpack.append(newtumple)
                    player1.water += 4
                    if player1.water >= 20:
                        player1.water = 20
                    break
                timer += 1
            del timer
        if main == "进食":
            timer = 0
            cmdX = input("您要吃什么？")
            def eat(food):
                for name in player1.backpack:
                    if name[0] == food:
                        location = player1.backpack.index(name)
                        tumple = player1.backpack.pop(location)
                        newtumple = (tumple[0],tumple[1] - 1)
                        if newtumple[1] > 0:
                            player1.backpack.append(newtumple)
                        if food == "牛肉罐头":
                            player1.food += 4
                            print("已经吃了牛肉罐头！")
                        if food == "生蛇肉":
                            player1.food += 2
                            print("已经吃了生蛇肉！")
                        if food == "金枪鱼罐头":
                            player1.food += 4
                            print("已经吃了金枪鱼罐头！")
                        if food == "椰子":
                            player1.food += 2
                            player1.water += 2
                            print("已经吃了椰子！")
                        if food == "辣椒":
                            player1.food += 1
                            print("已经吃了辣椒！")
                        if player1.food >= 20:
                            player1.food = 20
                        if player1.water >= 20:
                            player1.water = 20               
            eat(cmdX)
        if main == "放到手中":
            okok = True
            if player1.hand != "" or player1.hand != None:
                okok = False
            if okok == True:
                thing = input("你要把什么东西放到手中？")
                for name in player1.backpack:
                    if name == thing:
                        player1.hand = thing
                        break
        if main == "清空手":
            player1.hand == None
        if main == "装备盔甲":
            armer = input("您要装备什么盔甲？")
            for name in player1.backpack:
                if armer in name:
                    if "胸甲" in armer:
                        armerchest = armer
                        del player1.backpack[player1.backpack.index(name)]
                        player1.armerpoint += 8
                    if "头盔" in armer:
                        armerhead = armer
                        del player1.backpack[player1.backpack.index(name)]
                        player1.armerpoint += 4
                    if "腿甲" in armer:
                        armerleg = armer
                        del player1.backpack[player1.backpack.index(name)]
                        player1.armerpoint += 5
                    if "靴子" in armer:
                        armerfoot = armer
                        del player1.backpack[player1.backpack.index(name)]
                        player1.armerpoint += 3
        if main == "建房子":
            house_x = int(input("输入该房屋的X坐标"))
            house_y = int(input("输入该房屋的Y坐标"))
            house_name = "house_" + input("输入该房屋的名称：")
            for name in player1.map:
                if name[0] == house_x and name[1] == house_y:
                    tumple = player1.map.pop(player1.map.index(name))
                    newtumple = (tumple[0],tumple[1],tumple[2],house_name)
                    player1.map.insert(player1.map.index(tumple),newtumple)
