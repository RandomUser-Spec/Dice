from tkinter import *
import random
from PIL import ImageTk, Image
root = Tk()

root.title("Endless Dice Game")
root.geometry("600x400")

root.configure(background = "yellow2")

img1 = ImageTk.PhotoImage(Image.open ("one.png"))
img2 = ImageTk.PhotoImage(Image.open ("two.png"))
img3 = ImageTk.PhotoImage(Image.open ("three.png"))
img4 = ImageTk.PhotoImage(Image.open ("four.png"))
img5 = ImageTk.PhotoImage(Image.open ("five.png"))
img6 = ImageTk.PhotoImage(Image.open ("six.png"))
player1score = 0;
player2score = 0;
dice = [img1,img2,img3,img4,img5,img6]
dice_number= [1,2,3,4,5,6]

def player1roll():
    global player1score
    r1 = random.randint(0,5)
    print(r1)
    p1 = dice[r1]
    player1_btn.config(image = p1)
    print(dice_number[r1])
    random_dice_label["text"] = "Player 1 Dice Random Number is : " + str(dice_number[r1])
    player1_dice = player1score + dice_number[r1]
    print(player1_dice)
    player_1_score["text"] = str(player1_dice)

player1 = Label(root, text = 'Player 1', bg = "royal blue", fg = 'white')
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

def player2roll():
    global player2score
    r2 = random.randint(0,5)
    print(r2)
    p2 = dice[r2]
    player2_btn.config(image = p2)

place2 = Label(root, text = 'Player 2', bg = 'royal blue', fg = 'white')
place2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score =  Label(root, bg = 'royal blue', fg = 'white')
player_1_score.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score = Label(root, bg = 'royal blue', fg = 'white')
player_2_score.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_dice_label = Label(root, bg = 'chocolate1', fg = 'white')
random_dice_label.place(relx = 0.4, rely = 0.5)

player1_btn = Button(root, image = img1, command = player1roll)
player1_btn.place(relx = 0.1, rely = 0.5, anchor = CENTER)

player2_btn = Button(root, image = img1, command = player2roll)
player2_btn.place(relx = 0.9, rely = 0.5, anchor = CENTER)

root.mainloop()