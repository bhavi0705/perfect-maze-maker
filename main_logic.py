import random 

def if_can_move_there(pos,facing,cant_visit):
    x_value,y_value=pos[0],pos[1]
    if facing==1:
        y_value+=1
    elif facing==2:
        x_value-=1
    elif facing==3:
        y_value-=1
    else:
        x_value+=1
    for i in cant_visit:
        if [x_value,y_value]==i:
            return False
    return True

def mainThing(size,visited_given,pos,facing,cant_visit,possible_ends):
    visited=visited_given.copy()
    end=[size-1,size-1]
    
    #facing 1:down 2:left 3:up 4:right 
    possible_moves=[1,2,3]
    
    while visited_given==visited:
        if(len(possible_moves)==0):
            cant_visit.append([pos[0],pos[1]])

            pos=[visited[-1][0],visited[-1][1]]
            visited.pop()
            possible_moves=[1,2,3]
            return [False,pos,visited,facing,cant_visit]

        choice=possible_moves[random.randrange(len(possible_moves))]
        if choice==1:#turned left (from our POV(down -->left-->up-->right-->down))
            if facing ==4:
                facing=1
            else:
                facing+=1
        elif choice==2:#turned right (from our POV(down<--left<--up<--right<--down))
            if facing==1:
                facing=4
            else:
                facing-=1


        if if_can_move_there(pos,facing,cant_visit):
            x_value,y_value=pos[0],pos[1]
            if facing==1:
                y_value+=1
            elif facing==2:
                x_value-=1
            elif facing==3:
                y_value-=1
            else:
                x_value+=1 
            visited.append([pos[0],pos[1]])
            cant_visit.append([pos[0],pos[1]])
            pos=[x_value,y_value]
            possible_moves=[1,2,3]
        else:
            possible_moves.remove(choice)
            if choice==1:
                if facing ==1:
                    facing=4
                else:facing-=1
            elif choice==2:
                if facing ==4:
                    facing =1 
                else:facing+=1
        for i in possible_ends:
            if pos==i:
                visited.append(i)
                return [True,pos,visited,facing,cant_visit]
    return [False,pos,visited,facing,cant_visit]
    
