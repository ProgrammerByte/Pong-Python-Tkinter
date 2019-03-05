from tkinter import *
from random import randint

class gamewindow():
    def __init__(s):
        s.root = Tk()
        s.root.title("Pong")
        
        s.root.bind("<KeyPress>", lambda event="<KeyPress>": gamewindow.keypress(event, s))
        s.root.bind("<KeyRelease>", lambda event="<KeyRelease>": gamewindow.keyrelease(event, s))
        
        s.root.grid()

        s.canvas = Canvas(bg = "Black", height = 500, width = 500)
        s.canvas.grid()
        
        s.player1 = s.canvas.create_rectangle(10, 10, 35, 100, fill = "White")
        s.velocity1 = 0

        s.player2 = s.canvas.create_rectangle(490, 10, 465, 100, fill = "White")
        s.velocity2 = 0

        s.player1score = 0
        s.player1text = s.canvas.create_text(100, 50, fill = "White", font = "Calibri 20 bold", text = s.player1score)

        s.player2score = 0
        s.player2text = s.canvas.create_text(400, 50, fill = "White", font = "Calibri 20 bold", text = s.player2score)

        lineamount = 10
        lineheight = int(500 / lineamount)
        gap = 10
        thickness = 5
        x1 = 250 - thickness
        x2 = 250 + thickness
        for lines in range(lineamount):
            y1 = 500 - (lines * lineheight)
            y2 = (y1 - lineheight) + gap
            s.line = s.canvas.create_rectangle(x1, y1, x2, y2, fill = "White")
                

        s.ball = s.canvas.create_oval(100, 240, 120, 260, fill = "White")
        s.ballvelx = 2
        s.ballvely = randint(-5, 5)

        gamewindow.RefreshScreen(s)
        s.root.mainloop()

    def RefreshScreen(s):
        player1pos = list(s.canvas.bbox(s.player1))
        player2pos = list(s.canvas.bbox(s.player2))
        ballpos = list(s.canvas.bbox(s.ball))
        deleted = "N"

        if s.velocity1 + player1pos[1] > 0 and s.velocity1 + player1pos[3] < 500:
            s.canvas.move(s.player1, 0, s.velocity1)

        if s.velocity2 + player2pos[1] > 0 and s.velocity2 + player2pos[3] < 500:
            s.canvas.move(s.player2, 0, s.velocity2)



        if s.ballvely + ballpos[1] < 0 or s.ballvely + ballpos[3] > 500:
            s.ballvely = -s.ballvely



        if player1pos[0] < s.ballvelx + ballpos[0] < player1pos[2] and (player1pos[1] < s.ballvely + ballpos[3] and s.ballvely + ballpos[1] < player1pos[3]):
            s.ballvelx = -s.ballvelx
            if player1pos[3] - (s.ballvely  + ballpos[3]) <  (s.ballvely + ballpos[1]) - player1pos[1]:
                s.ballvely += 1
            else:
                s.ballvely -= 1

        elif player2pos[0] < s.ballvelx + ballpos[2] < player2pos[2] and (player2pos[1] < s.ballvely + ballpos[3] and s.ballvely + ballpos[1] < player2pos[3]):
            s.ballvelx = -s.ballvelx
            if player2pos[3] - (s.ballvely  + ballpos[3]) <  (s.ballvely + ballpos[1]) - player2pos[1]:
                s.ballvely += 1
            else:
                s.ballvely -= 1


        elif s.ballvelx + ballpos[0] < player1pos[2]:
            deleted = "Y"
            s.player2score += 1
            s.canvas.delete(s.player2text)
            s.player2text = s.canvas.create_text(400, 50, fill = "White", font = "Calibri 20 bold", text = s.player2score)

        elif s.ballvelx + ballpos[2] > player2pos[0]:
            deleted = "Y"
            s.player1score += 1
            s.canvas.delete(s.player1text)
            s.player1text = s.canvas.create_text(100, 50, fill = "White", font = "Calibri 20 bold", text = s.player1score)


        if deleted == "Y":
            s.canvas.delete(s.ball)
            s.ball = s.canvas.create_oval(100, 240, 120, 260, fill = "White")
            s.ballvelx = 2
            s.ballvely = randint(-5, 5)

        
        s.canvas.move(s.ball, s.ballvelx, s.ballvely)

        s.root.after(10, gamewindow.RefreshScreen, s)
        
    
    def keypress(event, s):
        direction = event.keysym
        if direction == "s":
            s.velocity1 = 5
        elif direction == "w":
            s.velocity1 = -5

        elif direction == "Up":
            s.velocity2 = -5
        elif direction == "Down":
            s.velocity2 = 5

    def keyrelease(event, s):
        direction = event.keysym
        if direction == "w" or direction == "s":
            s.velocity1 = 0

        elif direction == "Up" or direction == "Down":
            s.velocity2 = 0

if __name__ == "__main__":
    game = gamewindow()
