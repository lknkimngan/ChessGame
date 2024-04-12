import pygame  
import os 
import time
pygame.font.init()
from piece import Bishop
from board import Board


board = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), "img", "board_alt.png")), (750,750))

rect = (113,113,525,525)

#Ve man hinh ban co o vi tri 0,0
def redraw_gamewindow(win, bo,p1,p2):
    

    win.blit(board,(0,0))
    
    bo.draw(win)
    formatTime1 = str(p1//60) + ":" + str(p1%60)
    formatTime2 = str(p2//60) + ":" + str(p2%60)
    if p1%60 == 0:
        formatTime1 += "0"
    if p2%60 == 0:
        formatTime2 += "0"

    font = pygame.font.SysFont("comicsans", 30)
                
    txt = font.render("player 2 Time: "+str(formatTime2),1,(255,255,255))
    txt2 = font.render("player 1 Time: "+str(formatTime1),1,(255,255,255))
    win.blit(txt, (450,10))
    win.blit(txt2, (450,700))
    pygame.display.update()

def end_screen(wim, text):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 80)
                
    txt = font.render(text,1,(255,0,0))
    win.blit(txt, (width/2 - txt.get_width()/2, 300))
    pygame.display.update()

    pygame.time.set_timer(pygame.USEREVENT+1, 3000)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                run = False
            elif event.type == pygame.KEYDOWN:
                run = False
            elif event.type == pygame.USEREVENT+1:
                run = False
    

def click(pos):
    
    x = pos[0]
    y = pos[1]
    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[1] + rect[3]:
            divX = x - rect[0]
            divY = y - rect[0]
            i = int(divX / (rect[2]/8))
            j = int(divY / (rect[3]/8))
            return i,j

def main():  
    p1Time = 900
    p2Time = 900
    
    turn = "w"
    bo = Board(8,8)
    bo.update_moves()
    clock = pygame.time.Clock()    
    run = True
    startTime = time.time()
    while run:
        clock.tick(10)
        
       
        if turn == "w":
            
            p1Time -= (time.time() -startTime)
            
        else:
            p2Time -= (time.time() - startTime)
        
        startTime = time.time()
            
        
        
        redraw_gamewindow(win,bo,int(p1Time),int(p2Time))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()

         
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                bo.update_moves()                
                i,j =click(pos)
                change = bo.select(i,j, turn)
                bo.update_moves()
                if change:
                    startTime = time.time()
                    if turn == "w":
                        turn = "b"
                        
                    else:
                        turn = "w"
                
        # if bo.checkMate("w"):
        #     end_screen(win, "Black Wins!!")
        # elif bo.checkMate("b"):
        #     end_screen(win, "White Wins!!")
      

# Thiet lap man hinh
width = 750
height = 750
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Chess Game")
main()