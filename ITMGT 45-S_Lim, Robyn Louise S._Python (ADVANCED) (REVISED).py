'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.


    if to_member in social_graph.get(from_member, []):
        if from_member in social_graph.get(to_member, []):
            return "friends"
        else:
            return "followed by"
    elif from_member in social_graph.get(to_member, []):
        return "follower"
    else:
        return "no relationship"




def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]
a=int(0)
i=int(0)
h=int(0)
l=int(0)
x=int(0)
ex=int(0)
circle=int(0)
board=(board7)
l=(len(board[0]))
h=(len(board))
while x<h-2 :
    while i<l-2 :
        if board[0+x][0+i] == board[0+x][0+i+1] and board[0+x][0+i] == board[0+x][0+i+2] and board[0+x][0+i]!='':
            a+=1
            i+=1
            
        elif board[0+x][0+i] == board[0+x][0+i+1] and board[0+x][0+i] == board[0+x][0+i+2] and board[0+x][0+i]=='X':
            i+=1
            a+=1
            ex=+1
        elif board[0+x][0+i] == board[0+x][0+i+1] and board[0+x][0+i] == board[0+x][0+i+2] and board[0+x][0+i]=='O':
            i+=1
            a+=1
            circle=+1
        else:
                i+=1
                a=0
    if a >0 and ex==1 :
        print("winner X")
        break
    elif a >0 and circle==1 :
        print("winner O")
        break
    else:
        a=0
        x+=1
    
        i=int(0)
        break


if a==0:
    x=0
    while x<h-2 :
        while i<l-2 :
            if board[0+x][0+i] == board[0+x+1][0+i+1] and board[0+x][0+i] == board[0+x+2][0+i+2] and board[0+x][0+i]!='':
                a+=1
                i+=1
            elif board[0+x][0+i] == board[0+x+1][0+i+1] and board[0+x][0+i] == board[0+x+2][0+i+2] and board[0+x][0+i]=='X':
                i+=1
                a+=1
                ex=+1
            elif board[0+x][0+i] == board[0+x+1][0+i+1] and board[0+x][0+i] == board[0+x+2][0+i+2] and board[0+x][0+i]=='O':
                i+=1
                a+=1
                circle=+1
            else:
                i+=1
                a=0
        if a >0 and ex==1 :
            print("winner X")
            break
        elif a >0 and circle==1 :
            print("winner O")
            break
        else:
            a=0
            x+=1
            i=int(0)
            break

if a==0:
    x=0
    while x<h-2 :
        while i<l-2 :
            if board[0+x][0+i+2] == board[0+x+1][0+i+1] and board[0+x][0+i] == board[0+x+2][0+i] and board[0+x][0+i]!='':
                a+=1
                i+=1
            elif board[0+x][0+i+2] == board[0+x+1][0+i+1] and board[0+x][0+i] == board[0+x+2][0+i] and board[0+x][0+i]=='X':
                i+=1
                a+=1
                ex=+1
            elif board[0+x][0+i+2] == board[0+x+1][0+i+1] and board[0+x][0+i] == board[0+x+2][0+i] and board[0+x][0+i]=='O':
                i+=1
                a+=1
                circle=+1
            else:
                i+=1
                a=0
        if a >0 and ex==1 :
            print("winner X")
            break
        elif a >0 and circle==1 :
            print("winner O")
            break
        else:
            a=0
            x+=1
            i=int(0)
            break
if a==0:
    while x<h-2 :
        while i<l-2 :
            if board[0+x][0+i+2] == board[0+x+1][0+i+1] and board[0+x][0+i+2] == board[0+x+2][0+i] and board[0+x][0+i]!='':
                a+=1
                i+=1
            elif board[0+x][0+i+2] == board[0+x+1][0+i+1] and board[0+x][0+i+2] == board[0+x+2][0+i] and board[0+x][0+i]=='X':
                i+=1
                a+=1
                ex=+1
            elif board[0+x][0+i+2] == board[0+x+1][0+i+1] and board[0+x][0+i+2] == board[0+x+2][0+i] and board[0+x][0+i]=='O':
                i+=1
                a+=1
                circle=+1
            else:
                i+=1
                a=0
        if a >0 and ex==1 :
            print("winner X")
            break
        elif a >0 and circle==1 :
            print("winner O")
            break
        else:
            a=0
            x+=1
            i=int(0)
            break
           


def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if first_stop not in route_map or second_stop not in route_map:
        return None
    
    current_stop = first_stop
    total_time = 0
    
    while current_stop != second_stop:
        if current_stop == route_map[-1]:
            next_stop = route_map[0]
        else:
            next_stop = route_map[route_map.index(current_stop) + 1]
        
        time_to_next_stop = route_map[current_stop][next_stop]
        
        total_time += time_to_next_stop
        current_stop = next_stop
    
    return total_time