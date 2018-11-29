import pygame
import time
import random
from pygame.locals import*
###########
def upd(S,sc):
    S.fill((0,0,0))
    if sc==0:
        color=(255,0,0)
    else:
        color=(0,255,0)
    rendered=font.render("your score is {}".format(sc),0,color)
    S.blit(rendered,(125,200))
    pygame.display.update()
##########
pygame.init()
pygame.display.set_caption('snake game')
Surface=pygame.display.set_mode((500,500))
Surface.fill((0,0,0))
pygame.draw.rect(Surface,(255,255,255),[100,75,300,75],0)
pygame.draw.rect(Surface,(255,255,255),[100,175,300,75],0)
font = pygame.font.SysFont(None,40)
rendered=font.render("NEW GAME",0,(0,0,0))
Surface.blit(rendered,(200,100))
rendered=font.render("LOAD GAME",0,(0,0,0))
Surface.blit(rendered,(200,200))
pygame.display.update()
exit=True
run=True
b=True
f=True
l=[[250,260],[250,250]]
x0=10
y0=0
score=0
####first window  
#####################
while exit:
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN:
            (mx,my)=pygame.mouse.get_pos()
            ####### NEW GAME
            if (mx>=100 and mx<=400 and my>=75 and my<=150):       
               exit=False
               run=True
               saving=True
               pygame.draw.rect(Surface,(100,100,100),[100,75,300,75],0)
               rendered=font.render("NEW GAME",0,(0,0,0))
               Surface.blit(rendered,(200,100))
               pygame.display.update()
               time.sleep(0.1)
        ######LOAD GAME
            else:
                if  (mx>=100 and mx<=400 and my>=175 and my<=250):
                    exit=False
                    run=True
                    saving=False
                    pygame.draw.rect(Surface,(100,100,100),[100,175,300,75],0)
                    rendered=font.render("LOAD GAME",0,(0,0,0))
                    Surface.blit(rendered,(200,200))
                    pygame.display.update()
        if e.type==pygame.QUIT:
            exit=False
            run=False
            f=False
        
######################
######## loading the variables
if not saving:
    l=[[],[]]
    ch=""
    file=open("logs.txt","r")
    for e in file:
        ch+=e
    file.close()
    i=0
    a=0
    s=""
    while ch[i]!="*":
        if ch[i]!="/" and ch[i]!="." and ch[i]!=";" and ch[i]!="," and ch[i]!="G" and ch[i]!="n" and ch[i]!="w" and ch[i]!="|":
            s=s+ch[i]
        if ch[i]=="/":
            score=int(s)
            s=""
        if ch[i]==".":
            l[a].append(int(s))
            s=""
        if ch[i]=="G":
            l[a].append(int(s))
            s=""
            a+=1
        i+=1
        if ch[i]==";":
            l[a].append(int(s))
            s=""
        if ch[i]==",":
            x0=int(s)
            s=""
        if ch[i]=="n":
            y0=int(s)
            s=""
        if ch[i]=="w":
            xp=int(s)
            s=""
        if ch[i]=="*":
            yp=int(s)
else:
    xp=random.randint(0,490)
    yp=random.randint(0,490)
    xp=xp-xp%10
    yp=yp-yp%10
Surface.fill((0,0,0))
back=(255,255,255)
pygame.init()
Surface=pygame.display.set_mode((500,500))
Surface.fill(back)
yellow=(100,10,10)
#################
for i in range(len(l[0])):
    pygame.draw.rect(Surface,(0,200,0),[l[0][i],l[1][i],10,10],0)
######second window
################
while run:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            run=False
            b=False
    keys=pygame.key.get_pressed() 
    pygame.draw.rect(Surface,(255,0,0),[xp,yp,10,10],0)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP] and y0!=10:
        y0 = -10
        x0 = 0
    if keys[pygame.K_DOWN] and y0!=-10:
        y0 = 10
        x0 = 0
    if keys[pygame.K_LEFT] and x0!= 10:
        x0 = -10
        y0 = 0
    if keys[pygame.K_RIGHT] and x0!=-10:
        x0 = 10
        y0 = 0       
    for i in range(len(l[0])):
        pygame.draw.rect(Surface,back,[l[0][i],l[1][i],10,10],0)
    for i in range(len(l[0])-1):
        l[0][len(l[0])-i-1]=l[0][len(l[0])-i-2]
        l[1][len(l[0])-i-1]=l[1][len(l[0])-i-2]
    l[0][0]+=x0             
    l[1][0]+=y0

    if l[0][0]>=490 or l[0][0]<=0 or l[1][0]<=0 or l[1][0]>=490:
        pygame.draw.circle(Surface,yellow,(l[0][0]-5,l[1][0]-5),4,0)
        pygame.draw.circle(Surface,yellow,(l[0][0]-5,l[1][0]+15),4,0)
        pygame.draw.circle(Surface,yellow,(l[0][0]+15,l[1][0]-5),4,0)
        pygame.draw.circle(Surface,yellow,(l[0][0]+15,l[1][0]+15),4,0)
        pygame.draw.circle(Surface,yellow,(l[0][0]+5,l[1][0]-5),3,0)
        pygame.draw.circle(Surface,yellow,(l[0][0]+5,l[1][0]+15),3,0)
        pygame.draw.circle(Surface,yellow,(l[0][0]+15,l[1][0]+5),3,0)
        pygame.draw.circle(Surface,yellow,(l[0][0]-5,l[1][0]+15),3,0)
        run = False
    time.sleep(0.155)
    for i in range(1,len(l[0])):
        pygame.draw.rect(Surface,(0,200,0),[l[0][i],l[1][i],10,10],0)
    pygame.draw.rect(Surface,(0,50,0),[l[0][0],l[1][0],10,10],0)
    if l[0][0]==xp and l[1][0]==yp:
        xp=random.randint(0,490)
        yp=random.randint(0,490)
        xp-=xp%10
        yp-=yp%10
        l[0].append(l[0][len(l[0])-1]-x0)
        l[1].append(l[1][len(l[1])-1]-y0)
        score+=2
    for i in range(4,len(l[0])):
        if l[0][0]==l[0][i-1] and l[1][0]==l[1][i-1]:
            pygame.draw.circle(Surface,(255,0,0),(l[0][0]+5,l[1][0]+5),6,0)
            run=False
    pygame.display.update()
time.sleep(1)
##########################
########third window 
if run==False and b==True and f==True :
    f=True
    while f:
        for ev in pygame.event.get():
            if ev.type==pygame.QUIT:
                f=False
        upd(Surface,score) 
ch="{}/".format(score)
########## overwriting the file logs.txt
if run==False and b==False:
    for i in range(len(l[0])):
         ch+="{}.".format(l[0][i])
    n=list(ch)
    del n[len(n)-1]
    ch="".join(n)
    ch+="G"
    for i in range(len(l[1])):
         ch+="{}.".format(l[1][i])
    n=list(ch)
    del n[len(n)-1]
    ch="".join(n)
    ch+=";{},{}n{}w{}*".format(x0,y0,xp,yp)
    ch+="".format()
    file=open("logs.txt","w")
    file.write(ch)
    file.close()


##               ___     
##|\   /\ |\   ||      |\  |\
##| \ /  \| \  ||___   | ) | )
##| / \  /|  \ ||      |(  |(
##|/   \/ |   \||___   | ) | )
##                     |/  |/