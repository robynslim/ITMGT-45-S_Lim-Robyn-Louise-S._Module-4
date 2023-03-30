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
from_member= str()

to_member= str()

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}
if to_member in(social_graph[from_member]["following"]) and from_member in (social_graph[to_member]["following"]):
        print("freinds")
elif to_member in(social_graph[from_member]["following"]):
    print('follower')
elif from_member in (social_graph[to_member]["following"]):
    print('followedby')
else:
    print('no relationship')



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
board=(board7)
l=(len(board[0]))
h=(len(board))
while x<h-2 :
    while i<l-2 :
        if board[0+x][0+i] == board[0+x][0+i+1] and board[0+x][0+i] == board[0+x][0+i+2] and board[0+x][0+i]!='':
            a+=1
            i+=1
        else:
            i+=1
            a=0
    if a >0:
        print("winner")
        break
    else:
        a=0
        break
    x+=1
    
    i=int(0)

if a==0:
    while x<h-2 :
        while i<l-2 :
            if board[0+x][0+i] == board[0+x+1][0+i+1] and board[0+x][0+i] == board[0+x+2][0+i+2] and board[0+x][0+i]!='':
                a+=1
                i+=1
            else:
                i+=1
                a=0
        if a >0:
            print("winner")
            break
        else:
            a=0
            break
        x+=1
        
        i=int(0)
if a==0:
    while x<h-2 :
        while i<l-2 :
            if board[0+x][0+i+2] == board[0+x+1][0+i+1] and board[0+x][0+i] == board[0+x+2][0+i] and board[0+x][0+i]!='':
                a+=1
                i+=1
            else:
                i+=1
                a=0
        if a >0:
            print("winner")
            break
        else:
            a=0
            break
        x+=1
        
        i=int(0)
if a==0:
    while x<h-2 :
        while i<l-2 :
            if board[0+x][0+i+2] == board[0+x+1][0+i+1] and board[0+x][0+i+2] == board[0+x+2][0+i] and board[0+x][0+i]!='':
                a+=1
                i+=1
            else:
                i+=1
                a=0
        if a >0:
            print("winner")
            break
        else:
            a=0
            print("no winner")
            break
        x+=1
        
        i=int(0)
           


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
legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}
first_stop= str('a1')

second_stop = str('a2')

route_map = dict(legs)

print(legs[first_stop,second_stop]['travel_time_mins'])
