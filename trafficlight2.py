import tkinter as tk
from tkinter import Canvas
import time

class TrafficLight(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Traffic Light Simulation")
        self.geometry("700x700")
        
        self.canvas = Canvas(self, width=700, height=700, bg="grey")
        self.canvas.pack()

        # [x0, y0, x1, y1] coordinates for the lights with adapted size
        self.lights = {'N': [280, 100, 420, 240],
                       'S': [280, 460, 420, 600],
                       'E': [460, 280, 600, 420],
                       'W': [100, 280, 240, 420],
                       'P': [280, 280, 420, 420]}

        # initial state
        self.state = {'N': 'red', 'S': 'red', 'E': 'red', 'W': 'red', 'P': 'green'}

        # duration of each light state in seconds
        self.durations = {'green': 5, 'yellow': 2, 'red': 5, 'walk': 5, 'do_not_walk': 2}

        self.update_lights()

    def update_lights(self):
        self.draw_roads()  # Draw roads first
        for light, coords in self.lights.items():
            self.canvas.create_oval(coords[0], coords[1], coords[2], coords[3], fill=self.state[light])
        
        self.after(1000, self.change_lights)
        
    def draw_roads(self):
        # Draw horizontal road
        self.canvas.create_rectangle(0, 280, 700, 420, fill='black', outline='black')
        
        # Draw vertical road
        self.canvas.create_rectangle(280, 0, 420, 700, fill='black', outline='black')
        
        # Draw dashed lines for pedestrian paths
        for i in range(7):
            self.canvas.create_rectangle(280, 280 + i*40, 420, 300 + i*40, fill='white', outline='white')
            self.canvas.create_rectangle(280 + i*40, 280, 300 + i*40, 420, fill='white', outline='white')
        
    def change_lights(self):
        # Basic logic for changing lights
        # More comprehensive logic will be required for a real-world application
        if self.state['N'] == self.state['S'] == 'red' and self.state['E'] == self.state['W'] == 'green':
            self.state['E'] = self.state['W'] = 'yellow'
            self.durations['yellow'] -= 1
            if self.durations['yellow'] == 0:
                self.state['E'] = self.state['W'] = 'red'
                self.state['P'] = 'green'
                self.durations['yellow'] = 2  # reset duration
        elif self.state['E'] == self.state['W'] == 'red' and self.state['N'] == self.state['S'] == 'green':
            self.state['N'] = self.state['S'] = 'yellow'
            self.durations['yellow'] -= 1
            if self.durations['yellow'] == 0:
                self.state['N'] = self.state['S'] = 'red'
                self.state['P'] = 'green'
                self.durations['yellow'] = 2  # reset duration
        elif self.state['P'] == 'green':
            self.durations['walk'] -= 1
            if self.durations['walk'] == 0:
                self.state['P'] = 'red'
                if self.state['N'] == 'red':
                    self.state['E'] = self.state['W'] = 'green'
                else:
                    self.state['N'] = self.state['S'] = 'green'
                self.durations['walk'] = 5  # reset duration
        
        self.canvas.delete("all")
        self.update_lights()


app = TrafficLight()
app.mainloop()
