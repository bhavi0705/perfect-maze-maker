import os 
import pygame 
import random
from calling_pygame_corner_finder import generate_main_path
def generate_maze():
    pygame.font.init()

    used_font=pygame.font.SysFont("monospace",30)

    #how does one maze

    WHITE=(255,255,255)
    BLACK=(0,0,0)



    FPS1=15 #to take input
    FPS2=30 #to make "maze"
    FPS3=2 #to "solve maze"



    WIN =pygame.display.set_mode((800,800))


    

    clock=pygame.time.Clock()



    progress="user_input"
    user_text=""


    visited,pos=[],[0,0]
    facing=1

    possible_ends=[]

    run = True

    BLOCKIMGRED=pygame.image.load(os.path.join("assets","block_red.png"))
    BLOCKIMG=pygame.image.load(os.path.join("assets","block.png"))


    def draw_path(visited,size):
        THICKNESS=700//size
        block_used=pygame.transform.scale(BLOCKIMG,(THICKNESS-1,THICKNESS-1))
        for i in visited:
            WIN.blit(block_used,(i[0]*THICKNESS+26,i[1]*THICKNESS+26))
        pygame.display.update()
    def draw_path_red(visited,size):
        THICKNESS=700//size
        block_used=pygame.transform.scale(BLOCKIMGRED,(THICKNESS-1,THICKNESS-1))
        for i in visited:
            WIN.blit(block_used,(i[0]*THICKNESS+26,i[1]*THICKNESS+26))
        pygame.display.update()
    
    def draw_maze(size,visited):
                THICKNESS=700//size
                HORIZONTALBAR_WHITE=pygame.transform.scale(pygame.image.load(os.path.join("assets","horizontal_white.png")),(THICKNESS,1))
                VERTICALBAR_WHITE=pygame.transform.scale(pygame.image.load(os.path.join("assets","vertical_white.png")),(1,THICKNESS))

                for i in range(len(visited)-1):

                    if visited[i][0]+1==visited[i+1][0]:
                        WIN.blit(VERTICALBAR_WHITE,((25+((THICKNESS)*(visited[i][0]+1))),25+((THICKNESS)*visited[i][1])))          
                    elif visited[i][0]-1==visited[i+1][0]: 
                        WIN.blit(VERTICALBAR_WHITE,((25+((THICKNESS)*(visited[i][0]))),25+((THICKNESS)*visited[i][1])))
                    elif visited[i][1]+1==visited[i+1][1]:
                        WIN.blit(HORIZONTALBAR_WHITE,((25+((THICKNESS)*(visited[i+1][0]))),25+((THICKNESS)*(visited[i][1]+1))))
                    elif visited[i][1]-1==visited[i+1][1]:
                        WIN.blit(HORIZONTALBAR_WHITE,((25+((THICKNESS)*(visited[i+1][0]))),25+((THICKNESS)*(visited[i][1]))))                
                    pygame.display.update()

    def check_if_move_possible_(facing,pos,maze,traversed):
        if facing==1:
            x_to_be=pos[0]
            y_to_be=pos[1]+1
        elif facing==2:
            x_to_be=pos[0]-1
            y_to_be=pos[1]
        elif facing==3:
            x_to_be=pos[0]-1
            y_to_be=pos[1]
        else:
            x_to_be=pos[0]+1
            y_to_be=pos[1]
        pos_to_be=[x_to_be,y_to_be]
        
        for i in traversed:
            if pos_to_be == i:return False
        #1=down,2=left<-,3=up,4=right->
        if facing==1:
            
            for i in maze[pos[0]][pos[1]+1]:
                if i==1:
                    return True

        elif facing==2:
            for i in maze[pos[0]-1][pos[1]]:
                if i==2:
                    return True
        elif facing==3:
            for i in maze[pos[0]][pos[1]-1]:
                if i==3:
                    return True
        else:
            for i in maze[pos[0]+1][pos[1]]:
                if i==4:
                    return True
        

    def check_if_move_possible(facing,pos,visited,cant_go):
        pos_to_be=pos.copy()
        #1=down,2=left<-,3=up,4=right->
        if facing==1:
            pos_to_be[1]+=1

        elif facing==2:
            pos_to_be[0]-=1
        elif facing==3:
            pos_to_be[1]-=1
        else:
            pos_to_be[0]+=1
        for i in cant_go:
            if i == pos_to_be:
                return False
        for i in range(len(visited)-1):
            if visited[i]==pos:
                if visited[i+1]==pos_to_be:
                    return True
        return False 

    while run:

        if  progress=="user_input":
            tag_text="Enter Size Of Maze : "
            tag=used_font.render(tag_text,1,WHITE)

            for event in pygame.event.get():    
                if event.type==pygame.QUIT:
                    run =False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_BACKSPACE:
                        if len(user_text)!=0:
                            user_text=user_text[:-1]
                    elif event.key==pygame.K_RETURN:
                        size=int(user_text)
                        cant_visit=[]
                        possible_ends.append([size-1,size-1])
                        for i in range(size):
                            cant_visit.append([-1,i])
                            cant_visit.append([size,i])
                            cant_visit.append([i,-1])
                            cant_visit.append([i,size])

                        
                        progress="make maze"

                    elif event.key==pygame.K_0 or event.key==pygame.K_1 or event.key==pygame.K_2 or event.key==pygame.K_3 or event.key==pygame.K_4 or event.key==pygame.K_5 or event.key==pygame.K_6 or event.key==pygame.K_7 or event.key==pygame.K_8 or event.key==pygame.K_9 :
                                user_text+=event.unicode
            user_entry_field=used_font.render(user_text,1,WHITE)
            WIN.fill(BLACK)
            WIN.blit(tag,(75,250))
            WIN.blit(user_entry_field,(75,285))
            pygame.display.update() 
        elif progress=="make maze":
                maze=[]
                for i in range(size+1):
                    temp=[]
                    for j in range(size+1):
                        temp.append([])
                    maze.append(temp)
            
                THICKNESS=700//size
                HORIZONTALBAR=pygame.transform.scale(pygame.image.load(os.path.join("assets","horizontal.png")),(THICKNESS,1))
                VERTICALBAR=pygame.transform.scale(pygame.image.load(os.path.join("assets","vertical.png")),(1,THICKNESS))
                hori_margin=25
                ver_margin=25
                WIN.fill(WHITE)

                for i in range(size+1):
                    for j in range(size+1):

                        if i!=size:
                            WIN.blit(HORIZONTALBAR,(hori_margin,ver_margin))

                        if j!=size:
                            WIN.blit(VERTICALBAR,(hori_margin,ver_margin))

                        ver_margin+=THICKNESS
                    hori_margin+=THICKNESS
                    ver_margin=25
                possible_possible_pos=[]
                for i in range(0,size):
                     for j in range(0,size):
                          possible_possible_pos.append([i,j])

                returned_value=generate_main_path(pos,size,possible_ends)
                visited=returned_value[0]
                cant_go=returned_value[1]
                
                draw_maze(size,visited)
                visited_new=[]
                for i in visited:
                     possible_ends.append(i)
                     try:
                         possible_possible_pos.remove(i)
                     except:pass
                temp=0
                #possible_pos=[]
                #for i in range(2,len(visited)//10):
                #     possible_pos.append(possible_possible_pos[random.randrange(len(possible_possible_pos))])
                #     possible_pos.append([size//i,0])
                #     possible_pos.append([0,size//i])
                #     possible_pos.append([size//i,size-1])
                #     possible_pos.append([size-1,size//i])
                while len(possible_possible_pos)!=0:
                    

                    visited_new=[]

                    temp+=1
                    selecteed_pos=random.randrange(len(possible_possible_pos))
                    pos=possible_possible_pos[selecteed_pos]
                    possible_possible_pos.pop(selecteed_pos)
                    returned_value=generate_main_path(pos,size,possible_ends)
                    visited_new=returned_value[0]
                    for j in visited_new:
                        try:
                            possible_possible_pos.remove(j)
                        except:
                             pass
                        possible_ends.append(j)

                    for j in visited_new:
                        visited.append(j)

                    draw_maze(size,visited_new)


                print("done!")



                progress="preprocessing"
        elif progress=="solve it but cheat":     

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                   run=False  
            pos=[0,0]
            path_solved=[pos]
            end=[size-1,size-1]
            facing=1#1=down,2=left<-,3=up,4=right->
            possible_turns=[1,2,3]
            traversed=[pos]
            for i in range(size):
                traversed.append([-1,i])
                traversed.append([size,i])
                traversed.append([i,-1])
                traversed.append([i,size])

            while pos!=end:
           
                if len(possible_turns)==0:
                    traversed.append(pos)
                    pos=path_solved[-1]
                    possible_turns=[1,2,3]
                    path_solved.pop()
                    #draw_maze(size,path_solved)
                choice=possible_turns[random.randint(0,len(possible_turns)-1)]
                if choice==1:#turned closckwise
                    if facing==4:
                        facing=1
                    else:
                        facing+=1
                elif choice==2:
                     if facing==1:
                          facing=4
                     else:
                          facing-=1                          
                if check_if_move_possible(facing,pos,visited,traversed):
                    if facing==1:
                        pos[1]+=1
                    elif facing==2:
                        pos[0]-=1
                    elif facing==3:
                        pos[1]-=1
                    else:
                        pos[0]+=1
                    path_solved.append(pos)
                    draw_path(path_solved,size)
                    possible_turns=[1,2,3]
                else:
                    if choice==1:
                        if facing==1:
                             facing=4
                        else:
                            facing-=1
                    elif choice==2:
                        if facing==4:
                              facing=1
                        else:
                            facing+=1
                    

                    possible_turns.remove(choice)
            progress="done"
            print("ho gya malik")
        elif progress=="preprocessing":
            for i in range(len(visited)-1):
                
                #[x_value,y_value]
                #this box can be entered by going 1=down,2=left<-,3=up,4=right->
                if visited[i][0]+1==visited[i+1][0]:
                    try :
                        maze[visited[i][0]][visited[i][1]].remove(2)
                        maze[visited[i][0]][visited[i][1]].append(2)
                    except:
                        maze[visited[i][0]][visited[i][1]].append(2)
                    try:
                        maze[visited[i+1][0]][visited[i][1]].remove(4)
                        maze[visited[i+1][0]][visited[i][1]].append(4)
                    except:
                        maze[visited[i+1][0]][visited[i][1]].append(4)
                elif visited[i][0]-1==visited[i+1][0]:
                    try:
                        maze[visited[i][0]][visited[i][1]].remove(4)
                        maze[visited[i][0]][visited[i][1]].append(4)
                    except:
                        maze[visited[i][0]][visited[i][1]].append(4)
                    try:
                        maze[visited[i+1][0]][visited[i][1]].remove(2)
                        maze[visited[i+1][0]][visited[i][1]].append(2)
                    except:
                        maze[visited[i+1][0]][visited[i][1]].append(2)
                elif visited[i][1]+1==visited[i+1][1]:
                    try:
                        maze[visited[i][0]][visited[i][1]].remove(3)
                        maze[visited[i][0]][visited[i][1]].append(3)
                    except:
                        maze[visited[i][0]][visited[i][1]].append(3)
                    try:
                        maze[visited[i][0]][visited[i+1][1]].remove(1)
                        maze[visited[i][0]][visited[i+1][1]].append(1)
                    except:
                        maze[visited[i][0]][visited[i+1][1]].append(1)
                elif visited[i][1]-1==visited[i+1][1]:
                    try:
                        maze[visited[i][0]][visited[i][1]].remove(1)
                        maze[visited[i][0]][visited[i][1]].append(1)
                    except:
                        maze[visited[i][0]][visited[i][1]].append(1)
                    try:
                        maze[visited[i][0]][visited[i+1][1]].remove(3)
                        maze[visited[i][0]][visited[i+1][1]].append(3)
                    except:
                        maze[visited[i][0]][visited[i+1][1]].append(3)
            temp=0
            for i in maze:
                
                temp+=1
            progress="solve i"
            pos=[0,0]
            path_solved=[pos]
            end=[size-1,size-1]
            facing=1#1=down,2=left<-,3=up,4=right->
            possible_turns=[1,2,3]
            traversed=[]
            for i in range(size):
                traversed.append([-1,i])
                traversed.append([size,i])
                traversed.append([i,-1])
                traversed.append([i,size])
            chose_wrong=[]

        elif progress=="solve it":
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                   run=False  
            
            while pos!=end:
                clock.tick(3)
                if len(possible_turns)==0:
                    
                    traversed.append(pos)
                    chose_wrong.append(pos)
                    pos=path_solved[-1]
                    path_solved.pop()
                    possible_turns=[1,2,3]
                    traversed.remove(pos)
                    
                    draw_path_red(chose_wrong,size)
                choice=possible_turns[random.randint(0,len(possible_turns)-1)]
                if choice==1:#turned closckwise
                    if facing==4:
                        facing=1
                    else:
                        facing+=1
                elif choice==2:
                     if facing==1:
                          facing=4
                     else:
                          facing-=1                          
                if check_if_move_possible_(facing,pos,maze,traversed):
                    if facing==1:
                        pos[1]+=1
                    elif facing==2:
                        pos[0]-=1
                    elif facing==3:
                        pos[1]-=1
                    else:
                        pos[0]+=1
                    path_solved.append([pos[0],pos[1]])
                    traversed.append([pos[0],pos[1]])

                    draw_path([pos],size)
                    possible_turns=[1,2,3]
                else:
                    if choice==1:
                        if facing==1:
                             facing=4
                        else:
                            facing-=1
                    elif choice==2:
                        if facing==4:
                              facing=1
                        else:
                            facing+=1
                    

                    possible_turns.remove(choice)
            progress="done"
            print("ho gya malik")
        else:
            pygame.display.update()
            for event in pygame.event.get():
                  if event.type==pygame.QUIT:
                       run=False
    pygame.quit()
    return visited

generate_maze()
print("Progress not solve it")