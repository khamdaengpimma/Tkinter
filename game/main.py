import tkinter as tk

class Ball:
    def __init__(self, canvas, x, y, dx, dy, radius, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color
        self.ball = self.canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius, fill=color
        )

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Check collision with canvas boundaries
        if self.x - self.radius <= 0 or self.x + self.radius >= self.canvas.winfo_width():
            self.dx = -self.dx
        if self.y - self.radius <= 0 or self.y + self.radius >= self.canvas.winfo_height():
            self.dy = -self.dy

        # Move the ball
        self.canvas.move(self.ball, self.dx, self.dy)

def update_animation():
    ball1.move()
    ball2.move()
    
    # Check for collision between balls
    distance = ((ball2.x - ball1.x) ** 2 + (ball2.y - ball1.y) ** 2) ** 0.5
    if distance <= ball1.radius + ball2.radius:
        # Swap velocities for reflection effect
        ball1.dx, ball2.dx = ball2.dx, ball1.dx
        ball1.dy, ball2.dy = ball2.dy, ball1.dy

    root.after(5, update_animation)

def control_ball1(event):
    print(event)
    if event.keysym == 'Up':
        ball1.dy = -2
    elif event.keysym == 'Down':
        ball1.dy = 2
    elif event.keysym == 'Left':
        ball1.dx = -2
    elif event.keysym == 'Right':
        ball1.dx = 2

def control_ball2(event):
    print(event)
    if event.keysym == 'w':
        ball2.dy = -2
    elif event.keysym == 's':
        ball2.dy = 2
    elif event.keysym == 'a':
        ball2.dx = -2
    elif event.keysym == 'd':
        ball2.dx = 2

root = tk.Tk()
root.title("Bouncing Balls")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

ball1 = Ball(canvas, 50, 100, 3, 2, 20, "red")
ball2 = Ball(canvas, 150, 150, -2, -3, 20, "blue")

update_animation()

# Bind arrow keys to control ball 1
root.bind('<Up>', control_ball1)
root.bind('<Down>', control_ball1)
root.bind('<Left>', control_ball1)
root.bind('<Right>', control_ball1)

# Bind WASD keys to control ball 2
root.bind('w', control_ball2)
root.bind('s', control_ball2)
root.bind('a', control_ball2)
root.bind('d', control_ball2)

root.mainloop()
