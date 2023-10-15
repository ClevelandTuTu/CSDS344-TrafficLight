import time
import threading
import tkinter as tk

class VehicleLight:
    def __init__(self, left, straightRight):
        self.left = left
        self.straightRight = straightRight
        self.working = True

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
            time.sleep(16)
    
    def delayLooping(self, delay_time):
        time.sleep(delay_time)
        self.startLooping()


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
            self.lightGreen()
            time.sleep(4)
            self.lightOrange()
            time.sleep(2)
            self.lightRed()
            time.sleep(24)
    
    def delayLooping(self, delay_time):
        time.sleep(delay_time)
        self.startLooping()
            

def update_lights(vehicleNS, vehicleEW):
    canvas.itemconfig(north_straight_light, fill=vehicleNS.getStraightRight())
    canvas.itemconfig(south_straight_light, fill=vehicleNS.getStraightRight())
    canvas.itemconfig(east_straight_light, fill=vehicleEW.getStraightRight())
    canvas.itemconfig(west_straight_light, fill=vehicleEW.getStraightRight())
    canvas.itemconfig(north_left_light, fill=vehicleNS.getLeft())
    canvas.itemconfig(south_left_light, fill=vehicleNS.getLeft())
    canvas.itemconfig(east_left_light, fill=vehicleEW.getLeft())
    canvas.itemconfig(west_left_light, fill=vehicleEW.getLeft())
    root.after(1000, lambda: update_lights(vehicleNS, vehicleEW))

# start running vehicle lights
vehicleNS = VehicleLight("red", "red")
vehicleEW = VehicleLight("red", "red")
vehicleNS_thread = threading.Thread(target=vehicleNS.startLooping)
vehicleEW_thread = threading.Thread(target=vehicleEW.delayLooping, args=(15,))
pedestrianNS = PedestrianLight("red")
pedestrianEW = PedestrianLight("red")
pedestrianNS_thread = threading.Thread(target=pedestrianNS.startLooping)
pedestrianEW_thread = threading.Thread(target=pedestrianEW.delayLooping, args=(15,))
vehicleNS_thread.start()
vehicleEW_thread.start()
pedestrianNS_thread.start()
pedestrianEW_thread.start()

seconds = 0
while seconds < 32:
    print(seconds, ": ")
    print("Vehicle South North left: ", vehicleNS.getLeft())
    print("Vehicle South North straight and right: ", vehicleNS.getStraightRight())
    print("Pedestrian South North: ", pedestrianNS.getLight())
    print("Vehicle East West left: ", vehicleEW.getLeft())
    print("Vehicle East West straight and right: ", vehicleEW.getStraightRight())
    print("Pedestrian East West: ", pedestrianEW.getLight())
    time.sleep(1)
    seconds += 1

# drawcanvas
root = tk.Tk()
root.title("Traffic Light Simulation")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

def draw_light(x, y):
    return canvas.create_oval(x, y, x+30, y + 30, fill="gray")

straight_light_positions = [(160, 10), (320, 150), (160, 290), (20, 150)]
left_light_positions = [(120, 10), (280, 150), (120, 290), (-20, 150)]

north_straight_light = draw_light(*straight_light_positions[0])
south_straight_light = draw_light(*straight_light_positions[2])
east_straight_light = draw_light(*straight_light_positions[1])
west_straight_light = draw_light(*straight_light_positions[3])

north_left_light = draw_light(*left_light_positions[0])
south_left_light = draw_light(*left_light_positions[2])
east_left_light = draw_light(*left_light_positions[1])
west_left_light = draw_light(*left_light_positions[3])

update_lights(vehicleNS, vehicleEW)
root.mainloop()

