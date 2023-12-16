import tkinter as tk
import time

class Maze(tk.Tk):
    def __init__(self, width: int, height: int, scale: int, goal: tuple, hells: list):
        super(Maze, self).__init__()
        self.actor_ref = None
        self.title('Maze')
        self.geometry(f'{width * scale}x{height * scale}')
        self._build_maze()

        self.height = height * scale
        self.width = width * scale
        self.maze_height = height
        self.maze_width = width
        self.scale = scale
        self.goal = goal
        self.hells = hells

    def _build_maze(self) -> None:    
        self.canvas = tk.Canvas(self, bg="white", height=self.height, width=self.width)
        # Make grid
        for r in range(0, self.maze_width * self.scale, self.scale):
            x0, y0, x1, y1 = 0, r, self.maze_height * self.scale, r
            self.canvas.create_line(x0, y0, x1, y1)
        for c in range(0, self.maze_height * self.scale, self.scale):
            x0, y0, x1, y1 = c, 0, c, self.maze_width * self.scale
            self.canvas.create_line(x0, y0, x1, y1)

        # Hells
        for h in self.hells:
            self.canvas.create_rectangle(
                h[0] * self.scale, h[1] * self.scale,
                h[0] * self.scale + self.scale, h[1] * self.scale + self.scale,
                fill='black')

        # Goal
        self.canvas.create_oval(
            self.goal[0] * self.scale, self.goal[1] * self.scale,
            self.goal[0] * self.scale + self.scale, self.goal[1] * self.scale + self.scale,
            fill='yellow')

        # Actor
        self.actor_ref = self.canvas.create_rectangle(
            0, 0,
            self.scale, self.scale,
            fill='green')

        self.canvas.pack()

    def update_canvas(self, actor):
        time.sleep(0.2)
        self.canvas.delete(self.actor_ref)
        self.actor_ref = self.canvas.create_rectangle(
            actor[0] * self.scale, actor[1] * self.scale,
            actor[0] * self.scale + self.scale, actor[1] * self.scale + self.scale,
            fill='green')
        self.update()

