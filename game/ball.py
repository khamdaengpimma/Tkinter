from tkinter import *

class Ball:
    def __init__(self, canvas, name, **kw):
        self.canvas = canvas
        self.radius = kw.get('radius', 50)
        self.pos_x = kw.get('pos_x', 0)
        self.pos_y = kw.get('pos_y', 0)
        self.color = kw.get('color', 'red')
        self.name = name
        self.create()

    def calculate_ball_pos(self):
        x1 = self.pos_x
        x2 = self.pos_x + self.radius
        y1 = self.pos_y
        y2 = self.pos_y + self.radius
        return x1, y1, x2, y2

    def create(self):
        coords = self.calculate_ball_pos()
        self.ball = self.canvas.create_oval(coords[0], coords[1], coords[2], coords[3])
        self.canvas.itemconfig(self.ball, fill=self.color)

        label_x = (coords[0] + coords[2]) / 2 
        label_y = (coords[1] + coords[3]) / 2
        self.label = self.canvas.create_text(label_x, label_y, text=self.name)

    def move(self, x=0, y=0):
        self.pos_x += x
        self.pos_y += y

        if self.pos_x < 0:
            self.pos_x = 0
        elif self.pos_x + self.radius > self.canvas.winfo_width():
            self.pos_x = self.canvas.winfo_width() - self.radius

        if self.pos_y < 0:
            self.pos_y = 0
        elif self.pos_y + self.radius > self.canvas.winfo_height():
            self.pos_y = self.canvas.winfo_height() - self.radius

        coords = self.calculate_ball_pos()
        self.canvas.coords(self.ball, coords[0], coords[1], coords[2], coords[3])

        label_x = (coords[0] + coords[2]) / 2
        label_y = (coords[1] + coords[3]) / 2
        self.canvas.coords(self.label, label_x, label_y)

def check_collision(ball1, ball2):
    x1, y1, r1 = ball1.pos_x, ball1.pos_y, ball1.radius
    x2, y2, r2 = ball2.pos_x, ball2.pos_y, ball2.radius
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) **.6
    return distance < r1 + r2

ball1_di=''
ball2_di=''

def key(event):
    """Receive a keypress and move the ball by a specified amount"""
    global ball1, ball2, ball1_di, ball2_di
    move_speed=20
    if event.char == 'w':
        ball2.move(0, -move_speed)
        ball2_di = "up"
    elif event.char == 's':
        ball2.move(0, move_speed)
        ball2_di = "right"
    elif event.char == 'a':
        ball2.move(-move_speed, 0)
        ball2_di ="left"
    elif event.char == 'd':
        ball2.move(move_speed, 0)
        ball2_di = "down"
    elif event.keysym == 'Up':
        ball1.move(0, -move_speed)
        ball1_di = "up"
    elif event.keysym == 'Down':
        ball1.move(0, move_speed)
        ball1_di = "down"
    elif event.keysym == 'Left':
        ball1.move(-move_speed, 0)
        ball1_di ="left"
    elif event.keysym == 'Right':
        ball1.move(move_speed, 0)
        ball1_di = "right"

    move_speed += move_speed


    if check_collision(ball1, ball2):
        print("true ")
        print("B1",ball1.pos_x,ball1.pos_y)
        print("B2",ball2.pos_x,ball2.pos_y)
        print(ball1_di, " ", ball2_di)
        if ball1_di == "up" and ball2_di == "down":
            print ("b2 up b1 down")
            ball1.move(0,move_speed)  
            ball2.move(0,-move_speed)     
        elif ball1_di == "down"and ball2_di == "up":
            ball1.move(0,-move_speed)
            ball2.move(0,move_speed)
        elif ball1_di == "left" and ball2_di == "right":
            ball1.move(move_speed,0)
            ball2.move(-move_speed,0)
        elif ball1_di == "right"and ball2_di == "left":
            ball1.move(-move_speed,0)
            ball2.move(move_speed,0)

        elif ball1_di == "up":
            print ("b2 up b1 down")
            ball1.move(0,move_speed)  
            ball2.move(0,-move_speed)     
        elif ball1_di == "down":
            ball1.move(0,-move_speed)
            ball2.move(0,move_speed)
        elif ball1_di == "left":
            ball1.move(move_speed,0)
            ball2.move(-move_speed,0)
        elif ball1_di == "right":
            ball1.move(-move_speed,0)
            ball2.move(move_speed,0)
        
        elif ball2_di == "down":
            ball1.move(0,move_speed)
            ball2.move(0,-move_speed)       
        elif ball2_di == "up":
            ball1.move(0,-move_speed)
            ball2.move(0,move_speed)
        elif ball2_di == "right":
            ball1.move(move_speed,0)
            ball2.move(-move_speed,0)
        elif ball2_di == "left":
            ball1.move(-move_speed,0)
            ball2.move(move_speed,0)
    else:
        pass

    # if check_collision(ball1, ball2):
    #     print(" đang chạm nhau!")
    # else:
    #     pass

root = Tk()
root.title('Ball')
mainCanvas = Canvas(root, width=500, height=500)
root.bind('w', key)
root.bind('s', key)
root.bind('a', key)
root.bind('d', key)
root.bind('<Left>', key)
root.bind('<Right>', key)
root.bind('<Up>', key)
root.bind('<Down>', key)
mainCanvas.grid()
ball1 = Ball(mainCanvas, "B1", pos_x=225, pos_y=100)
ball2 = Ball(mainCanvas, "B2", pos_x=225, pos_y=300)
root.mainloop()
