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
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

def draw_light(x, y):
    return canvas.create_oval(x, y, x+30, y + 30, fill="gray")

light_positions = [(150, 10), (310, 150), (150, 290), (10, 150)]

north_light = draw_light(*light_positions[0])
south_light = draw_light(*light_positions[2])
east_light = draw_light(*light_positions[1])
west_light = draw_light(*light_positions[3])

left_turn_light = canvas.create_oval(185, 185, 215, 215, fill="gray")
text = canvas.create_text(200, 195, text="←", font=("Arial", 20))

light_state = 0  
east_west_light_state = 2  

change_lights()

root.mainloop()

