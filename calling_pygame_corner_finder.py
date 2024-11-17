from main_logic import mainThing
def generate_main_path(pos,size,possible_ends):        
        visited=[]
        for i in possible_ends:
              if i==pos:
                    return visited
        facing=1
        cant_visit=[]
        for i in range(size):
                cant_visit.append([-1,i])
                cant_visit.append([size,i])
                cant_visit.append([i,-1])
                cant_visit.append([i,size])
        for i in visited:
                cant_visit.append(i)
        while True:
            returnedValue=mainThing(size,visited,pos,facing,cant_visit,possible_ends)
            visited=returnedValue[2]
            pos=returnedValue[1]
            facing=returnedValue[3]
            if returnedValue[0]==True:
                visited=returnedValue[2]
                visited.append(pos)
                return [visited,cant_visit]
                

