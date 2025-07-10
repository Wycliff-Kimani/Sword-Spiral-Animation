import turtle
import time

def draw_sword():
    
    try:
        screen = turtle.Screen()
        screen.bgcolor("black")
        screen.title("Sword Annimation")
        
        
        t = turtle.Turtle()
        t.color("gold")
        t.pensize(1)
        
        
        t.speed(10)
        time.sleep(3)
        v = 200
        while v > 0:
            t.left(v)
            t.forward(v * 2)
            v = v - 1
        
        t.hideturtle()
        screen.mainloop()
    except turtle.Terminator:
        print("Drawing terminated by User - You")

if __name__ == "__main__":
    draw_sword()