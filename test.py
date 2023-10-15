import tkinter as tk

def update_lights():
    colors = ["red", "yellow", "green"]
    canvas.itemconfig(north_light, fill=colors[light_state])
    canvas.itemconfig(south_light, fill=colors[light_state])
    canvas.itemconfig(east_light, fill=colors[east_west_light_state])
    canvas.itemconfig(west_light, fill=colors[east_west_light_state])

    if light_state == 0 and east_west_light_state == 0:
        canvas.itemconfig(left_turn_light, fill="green")
    else:
        canvas.itemconfig(left_turn_light, fill="red")
    
    if light_state == 1 or east_west_light_state == 1:
        # Yellow light: Change after 2 seconds
        root.after(2000, change_lights)
    elif light_state == 0 or east_west_light_state == 0:
        # Red light: Change after 7 seconds
        root.after(7000, change_lights)
    else:
        # Green light: Change after 5 seconds
        root.after(5000, change_lights) 

def update_pedestrian_lights():
    colors = ["red", "yellow", "green"]
    canvas.itemconfig(east_pedestrian_light, fill=colors[light_state])
    canvas.itemconfig(north_pedestrian_light, fill=colors[light_state])
    canvas.itemconfig(west_pedestrian_light, fill=colors[east_west_light_state])
    canvas.itemconfig(south_pedestrian_light, fill=colors[east_west_light_state])

    if light_state == 0 and east_west_light_state == 0:
        canvas.itemconfig(left_turn_light, fill="green")
    else:
        canvas.itemconfig(left_turn_light, fill="red")
    
    if light_state == 1 or east_west_light_state == 1:
        # Yellow light: Change after 2 seconds
        root.after(2000, change_lights)
    elif light_state == 0 or east_west_light_state == 0:
        # Red light: Change after 7 seconds
        root.after(7000, change_lights)
    else:
        # Green light: Change after 5 seconds
        root.after(5000, change_lights)

def change_pedestrian_lights():
    global light_state, east_west_light_state
    
    if light_state == 1: 
        light_state = 0
    elif light_state == 0: 
        light_state = 2 if east_west_light_state == 0 else 0
    else: 
        light_state = 1
    
    if east_west_light_state == 1: 
        east_west_light_state = 0
    elif east_west_light_state == 0: 
        east_west_light_state = 2 if light_state == 0 else 0
    else: 
        east_west_light_state = 1

    update_pedestrian_lights()

def change_lights():
    global light_state, east_west_light_state
    
    if light_state == 1: 
        light_state = 0
    elif light_state == 0: 
        light_state = 2 if east_west_light_state == 0 else 0
    else: 
        light_state = 1
    
    if east_west_light_state == 1: 
        east_west_light_state = 0
    elif east_west_light_state == 0: 
        east_west_light_state = 2 if light_state == 0 else 0
    else: 
        east_west_light_state = 1

    update_lights()

root = tk.Tk()
root.title("Traffic Light Simulation")
canvas = tk.Canvas(root, width=512, height=512, bg="white")
canvas.pack()

def draw_light(x, y):
    return canvas.create_oval(x, y, x+30, y + 30, fill="gray")

light_positions = [(156, 256), (356, 256), (256, 156), (256, 356)]
left_turn_light_positions = [(206, 206), (306, 206), (206, 306), (306, 306)]
canvas.create_rectangle(250, 0, 300, 1000, fill="gray", outline="gray") # N-S road
canvas.create_rectangle(0, 250, 1000, 300, fill="gray", outline="gray") # E-W road

# Draw crosswalks


north_light = draw_light(*light_positions[0])
south_light = draw_light(*light_positions[1])
east_light = draw_light(*light_positions[2])
west_light = draw_light(*light_positions[3])

west_pedestrian_light = draw_light(*left_turn_light_positions[0])
south_pedestrian_light = draw_light(*left_turn_light_positions[1])
east_pedestrian_light = draw_light(*left_turn_light_positions[2])
north_pedestrian_light = draw_light(*left_turn_light_positions[3])

left_turn_light = canvas.create_oval(256, 256, 286, 286, fill="gray")
text = canvas.create_text(266, 266, text="←", font=("Arial", 10))

light_state = 0  
east_west_light_state = 2  

change_lights() 
update_pedestrian_lights()

root.mainloop()

