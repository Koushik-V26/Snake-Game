from tkinter import *
import random
GAME_WIDTH=1200
GAME_HEIGHT=1200
SPACE_SIZE=50
SPEED=1000
SNAKE_COLOUR="#00FF00"
FOOD_COLOUR="#FF0000"
BACKGROUND_COLOUR="#000000"
BODY_PARTS=3
class Snake:
    def __init__(self):
        self.body_size=BODY_PARTS
        self.coordinates=[]
        self.squares=[]

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOUR,tag="Snake")
            self.squares.append(square)

class Food:
    def __init__(self):

        x=random.randint(0,int(GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y=random.randint(0,int(GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE
        self.coordinates=[x,y]
        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOUR,tag="food")


def Next_turn(snake,food):
 x,y=snake.coordinates[0]

 if direction=="up":
    y-=SPACE_SIZE
 elif direction=="down":
     y+=SPACE_SIZE
 elif direction=="right":
     x+=SPACE_SIZE
 elif direction=="left":
     x-=SPACE_SIZE
 snake.coordinates.insert(0,(x,y))
 square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOUR)
 snake.squares.insert(0,square)

 if x==food.coordinates[0] and y==food.coordinates[1]:
     global score
     score+=1
     label.config(text="Score::{}".format(score))
     canvas.delete("food")
     food=Food()
 else:
     del snake.coordinates[-1]
     canvas.delete(snake.squares[-1])
     del snake.squares[-1]

 if Check_collosion(snake):
     Game_over()
 else:
     window.after(SPEED,Next_turn, snake,food)




def Change_direction(new_direction):

    global direction
    if direction=="right":
        if new_direction!="left":
            direction = new_direction
    
    if direction=="left":
        if new_direction!="right":
            direction = new_direction

    if direction=="down":
        if new_direction!="up":
            direction = new_direction
    
    if direction=="up":
        if new_direction!="down":
            direction = new_direction
    


def Check_collosion(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>= GAME_WIDTH:
        return  True
    
    elif y<0  or y>= GAME_HEIGHT:
        return  True
    
    for body_parts in snake.coordinates[1:]:
        if x==body_parts[0] and y==body_parts[1]:
            return True
        
    return False
        

def Game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,
                       font=("consolas",40),text="GAME OVER",fill="red")


window=Tk()
canvas = Canvas(window,width=GAME_WIDTH,height=GAME_HEIGHT,bg=BACKGROUND_COLOUR)
canvas.pack()
score=0
direction='down'
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((screen_width)/2-(window_width)/2)
y=int((screen_height)/2-(window_height)/2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Up>',lambda event :Change_direction('up'))
window.bind('<Right>',lambda event :Change_direction('right'))
window.bind('<Left>',lambda event :Change_direction('left'))
window.bind('<Down>',lambda event :Change_direction('down'))

food=Food()
snake=Snake()
Next_turn(snake,food)
window.mainloop()
