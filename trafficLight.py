import time
import threading
import tkinter as tk
from PIL import Image,ImageTk
class VehicleLight:
    def __init__(self, left, straightRight):
        self.left = left
        self.straightRight = straightRight
        self.working = True
    
    def setCanvas(self, canvas, leftSignP1, leftSignP2, straightRSignP1, straightRSignP2):
        self.canvas = canvas
        self.leftSignP1 = leftSignP1
        self.leftSignP2 = leftSignP2
        self.straightRSignP1 = straightRSignP1
        self.straightRSignP2 = straightRSignP2

    def setLeft(self, newLight):
        if newLight == "red":
            self.left = "red"
        elif newLight == "green":
            self.left = "green"
        elif newLight == "yellow":
            self.left = "yellow"
    
    def getLeft(self):
        return self.left
    
    def setStraightRight(self, newLight):
        if newLight == "red":
            self.straightRight = "red"
        elif newLight == "green":
            self.straightRight = "green"
        elif newLight == "yellow":
            self.straightRight = "yellow"
    
    def getStraightRight(self):
        return self.straightRight
    
    def straightRightGreen(self):
        self.setLeft("red")
        self.setStraightRight("green")
    
    def straightRightYellow(self):
        self.setLeft("red")
        self.setStraightRight("yellow")

    def leftGreen(self):
        self.setLeft("green")
        self.setStraightRight("red")

    def leftYellow(self):
        self.setLeft("yellow")
        self.setStraightRight("red")
    
    def allRed(self):
        self.setLeft("red")
        self.setStraightRight("red")
    
    def startLooping(self):
        while self.working:
            self.straightRightGreen()
            time.sleep(6)
            self.straightRightYellow()
            time.sleep(2)
            self.allRed()
            time.sleep(1)
            self.leftGreen()
            time.sleep(3)
            self.leftYellow()
            time.sleep(2)
            self.allRed()
            time.sleep(40)
    
    def delayLooping(self, delay_time):
        time.sleep(delay_time)
        self.startLooping()
    
    def updateCanvasImage(self, leftPhoto, straightRightPhoto, index):
        if self.getLeft() == "green":
            image1 = Image.open(leftPhoto)
            image1 = image1.resize((10, 10))
            image2 = image1
            img1 = ImageTk.PhotoImage(image1)
            img2 = ImageTk.PhotoImage(image2)
            self.canvas.create_image(self.leftSignP1[0], self.leftSignP1[1], image=img1)
            self.canvas.create_image(self.leftSignP2[0], self.leftSignP2[1], image=img2)
        elif self.getStraightRight() == "green":
            image1 = Image.open(straightRightPhoto)
            image1 = image1.resize((10, 10))
            image2 = image1
            img1 = ImageTk.PhotoImage(image1)
            img2 = ImageTk.PhotoImage(image2)
            self.canvas.create_image(self.straightRSignP1[0], self.straightRSignP1[1], image=img1)
            self.canvas.create_image(self.straightRSignP2[0], self.straightRSignP2[1], image=img2)
        else:
            img1 = None
            img2 = None
        
        if index == 1:
            self.canvas.img1 = img1  # 保存图像对象的引用
            self.canvas.img2 = img2  # 保存图像对象的引用
        else:
            self.canvas.img3 = img1  # 保存图像对象的引用
            self.canvas.img4 = img2  # 保存图像对象的引用


class PedestrianLight:
    def __init__(self, light):
        self.light = light
        self.working = True

    def setLight(self, newLight):
        if newLight == "red":
            self.light = "red"
        elif newLight == "green":
            self.light = "green"
        elif newLight == "orange":
            self.light = "orange"
    
    def getLight(self):
        return self.light
    
    def lightGreen(self):
        self.setLight("green")
    
    def lightOrange(self):
        self.setLight("orange")
    
    def lightRed(self):
        self.setLight("red")

    def startLooping(self):
        while self.working:
            self.lightRed()
            time.sleep(16)
            self.lightGreen()
            time.sleep(6)
            self.lightOrange()
            time.sleep(3)
            self.lightRed()
            time.sleep(2)
    
    def delayLooping(self, delay_time):
        time.sleep(delay_time)
        self.startLooping()
            

def update_lights(vehicleNS, vehicleEW, pedestrianAll):
    canvas.itemconfig(north_straight_light, fill=vehicleNS.getStraightRight())
    canvas.itemconfig(south_straight_light, fill=vehicleNS.getStraightRight())
    canvas.itemconfig(east_straight_light, fill=vehicleEW.getStraightRight())
    canvas.itemconfig(west_straight_light, fill=vehicleEW.getStraightRight())
    canvas.itemconfig(north_left_light, fill=vehicleNS.getLeft())
    canvas.itemconfig(south_left_light, fill=vehicleNS.getLeft())
    canvas.itemconfig(east_left_light, fill=vehicleEW.getLeft())
    canvas.itemconfig(west_left_light, fill=vehicleEW.getLeft())

    canvas.itemconfig(StoNlightRight, fill=pedestrianAll.getLight())
    canvas.itemconfig(NtoSlightRight, fill=pedestrianAll.getLight())
    canvas.itemconfig(WtoElightDown, fill=pedestrianAll.getLight())
    canvas.itemconfig(EtoWlightDown, fill=pedestrianAll.getLight())
    canvas.itemconfig(StoNlightLeft, fill=pedestrianAll.getLight())
    canvas.itemconfig(NtoSlightLeft, fill=pedestrianAll.getLight())
    canvas.itemconfig(WtoElightUp, fill=pedestrianAll.getLight())
    canvas.itemconfig(EtoWlightUp, fill=pedestrianAll.getLight())
    
    vehicleNS.updateCanvasImage("turnLeft.png", "turnRight.png", 1)  # update image
    vehicleEW.updateCanvasImage("turnLeft.png", "turnRight.png", 2)  # update image
    
    root.after(1000, lambda: update_lights(vehicleNS, vehicleEW, pedestrianAll))



# start running vehicle lights
vehicleNS = VehicleLight("red", "red")
vehicleEW = VehicleLight("red", "red")
vehicleNS_thread = threading.Thread(target=vehicleNS.startLooping)
vehicleEW_thread = threading.Thread(target=vehicleEW.delayLooping, args=(27,))
pedestrianAll = PedestrianLight("red")
#pedestrianNS = PedestrianLight("red")
#pedestrianEW = PedestrianLight("red")
pedestrianAll_thread = threading.Thread(target=pedestrianAll.startLooping)
#pedestrianNS_thread = threading.Thread(target=pedestrianNS.startLooping)
#pedestrianEW_thread = threading.Thread(target=pedestrianEW.delayLooping, args=(15,))
vehicleNS_thread.start()
vehicleEW_thread.start()
pedestrianAll_thread.start()
#pedestrianNS_thread.start()
#pedestrianEW_thread.start()




# drawcanvas
root = tk.Tk()
root.title("Traffic Light Simulation")
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

vehicleNS.setCanvas(canvas, (250,300), (250,200), (250,300), (250,200))  # set canvas
vehicleEW.setCanvas(canvas, (200,300), (200,200), (200,300), (200,200))  # set canvas
#image = Image.open("turnLeft.png")
#image = image.resize((10,10))
#img= ImageTk.PhotoImage(image)
def draw_light(x, y):
    return canvas.create_oval(x, y, x+30, y + 30, fill="gray")
def draw_pedestrain(x,y):
    return canvas.create_rectangle(x,y,x+30,y+30,fill='gray')

straight_light_positions = [(250, 150), (320, 250), (210, 310), (150, 210)]
left_light_positions = [(210, 150), (320, 210), (250, 310), (150, 250)]
canvas.create_rectangle(200, 0, 300, 1000, fill="gray", outline="gray") # N-S road
canvas.create_rectangle(0, 200, 1000, 300, fill="gray", outline="gray") # E-W road

StoNlightRight = draw_pedestrain(350,310)
NtoSlightRight = draw_pedestrain(350,150)
WtoElightDown  = draw_pedestrain(310,350)
EtoWlightDown  = draw_pedestrain(150,350)
StoNlightLeft  = draw_pedestrain(110,310)
NtoSlightLeft  = draw_pedestrain(110,150)
WtoElightUp    = draw_pedestrain(150,110)
EtoWlightUp    = draw_pedestrain(310,110)

north_straight_light = draw_light(*straight_light_positions[0])
south_straight_light = draw_light(*straight_light_positions[2])
east_straight_light = draw_light(*straight_light_positions[1])
west_straight_light = draw_light(*straight_light_positions[3])

north_left_light = draw_light(*left_light_positions[0])
south_left_light = draw_light(*left_light_positions[2])
east_left_light = draw_light(*left_light_positions[1])
west_left_light = draw_light(*left_light_positions[3])
turnleft_north = canvas.create_text(223, 160, text="←", font=("Arial", 15))
turnleft_sorth = canvas.create_text(263, 320, text="\u2192", font=("Arial", 15))
turnleft_east = canvas.create_text(333, 220, text="\u2191", font=("Arial", 15))
turnleft_west = canvas.create_text(163, 260, text="\u2193", font=("Arial", 15))
pedistranRight = canvas.create_rectangle(350,200,380,300,fill="black")
pedestrianLeft = canvas.create_rectangle(110,200,140,300,fill="black")
pedestrianUp = canvas.create_rectangle(200, 110, 300, 140, fill = "black")
pedestrianUp = canvas.create_rectangle(200, 350, 300, 380, fill = "black")
#canvas.create_image(10, 13, image=img)
update_lights(vehicleNS, vehicleEW, pedestrianAll)
root.mainloop()

vehicleNS.working = False
vehicleEW.working = False
pedestrianAll.working = False

vehicleNS_thread.join()
vehicleEW_thread.join()
pedestrianAll_thread.join()