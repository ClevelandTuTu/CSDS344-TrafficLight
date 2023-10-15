import tkinter as tk

def update_lights():
    colors = ["red", "yellow", "green"]
    for i, color in enumerate(colors):
        canvas.itemconfig(north_light[i], fill=color if i == light_state else "gray")
        canvas.itemconfig(south_light[i], fill=color if i == light_state else "gray")
        canvas.itemconfig(east_light[i], fill=color if i == east_west_light_state else "gray")
        canvas.itemconfig(west_light[i], fill=color if i == east_west_light_state else "gray")
    
    if light_state == 0 and east_west_light_state == 0:
        canvas.itemconfig(left_turn_light, fill="green")
    else:
        canvas.itemconfig(left_turn_light, fill="gray")
    
    root.after(2000, change_lights)

def change_lights():
    global light_state, east_west_light_state
    if light_state == 1: 
        light_state = 0
    elif light_state == 0: 
        if east_west_light_state == 0:  
            light_state = 2
    else: 
        light_state = 1
    
    if east_west_light_state == 1: 
        east_west_light_state = 0
    elif east_west_light_state == 0:
        if light_state == 0:
            east_west_light_state = 2
    else:
        east_west_light_state = 1
    
    update_lights()

root = tk.Tk()
root.title("Traffic Light Simulation")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

def draw_light(x, y):
    light = []
    colors = ["red", "yellow", "green"]
    for i, color in enumerate(colors):
        light.append(canvas.create_oval(x, y + i*40, x+30, y + i*40 + 30, fill="gray"))
    return light

light_positions = [(150, 10), (310, 150), (150, 290), (10, 150)]

north_light = draw_light(*light_positions[0])
south_light = draw_light(*light_positions[2])
east_light = draw_light(*light_positions[1])
west_light = draw_light(*light_positions[3])

# Draw a left-turn light
left_turn_light = canvas.create_oval(185, 185, 215, 215, fill="gray")

light_state = 0  # 0: red, 1: yellow, 2: green for N/S
east_west_light_state = 2  # for E/W
update_lights()

root.mainloop()
