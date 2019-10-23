# Goal: Dsconnect infected computers from uninfected computers with 1 cable cut
# A: List of computers connected to B, B: List of computers connected to A, where A[i] is connected to B[i]
# C: Index of computers infected

def stop_computer_infection(A, B, C):
    # Index of infected computers
    C_index = [i for i, x in enumerate(C) if x]  

    # List of index of uninfected computers linked to infected computers in list A and list B
    linked_computer = []  
    for i in range(len(A)):     
        # A is not infected and B is infected
        if (A[i] not in C_index) and (B[i] in C_index):            
            linked_computer.append(i)
        # A is infected and B is not infected
        if (A[i] in C_index) and (B[i] not in C_index):            
            linked_computer.append(i)

    # If there are more than 1 uninfected computer linked to infected computers, there is no way to break the link with one cut       
    if len(linked_computer) == 1:        
        print("Remove cable {} to separate infected from uninfected computers.".format(linked_computer[0]))
    else:        
        print("Remove cables {}. Unable to cut only one cable to separate infected from uninfected computers.".format(linked_computer))

# Computer 1 infected, linked to two computers 0,2
stop_computer_infection([0,1],[1,2],[False,True,False])

# Computer 1,5 infected, Computer 1,5 linked, Computer 1,3 linked (remove cable 1)
stop_computer_infection([0,1,2,3,5],[4,3,0,0,1],[False,True,False,False,False,True])

# Computer 1,5,6 infected, Computer 1,5 linked, Computer 5,6 linked, Computer 1,3 linked (remove cable 2)
stop_computer_infection([4,0,1,2,3,5,6],[7,4,3,0,0,1,5],[False,True,False,False,False,True,True,False])

# Computer 1,5,6 infected, Computer 1,5 linked, Computer 5,6 linked, Computer 1,3 linked (remove cable 1)
stop_computer_infection([0,1,2,3,5,6],[4,3,0,0,1,5],[False,True,False,False,False,True,True])

# Computer 1,5,6,7 infected, Computer 1,5 linked, Computer 5,6 linked, Computer 1,3 linked, Computer 4,7 linked
stop_computer_infection([4,0,1,2,3,5,6],[7,4,3,0,0,1,5],[False,True,False,False,False,True,True,True])