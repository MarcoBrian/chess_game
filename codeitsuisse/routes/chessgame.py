import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/chessgame', methods=['POST'])
def evaluate():
    data = request.get_json();
    print(data)
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input");
    result = chess(inputValue)
    logging.info("My result :{}".format(result))
    return json.dumps(result);




def chess(board):
    num_of_squares = 0
    #find queen position 
    position = [0,0]
    for row in range(len(board)):
        for item in range(len(board)):
            if board[row][item] == "K":
                position[0], position[1] = row,item 
    print(position)
    
    #check horizontally left
    horizontal_pointer_left = position[1] - 1
    row_pointer = position[0]
    while horizontal_pointer_left >= 0:
        if board[row_pointer][horizontal_pointer_left] == "":
            num_of_squares += 1
            horizontal_pointer_left -= 1
        elif board[row_pointer][horizontal_pointer_left] == "X":
            break 
   
    #check horizontally right
    horizontal_pointer_right = position[1] + 1
    while horizontal_pointer_right < len(board):
        if board[row_pointer][horizontal_pointer_right] == "":
            num_of_squares += 1
            horizontal_pointer_right += 1
        elif board[row_pointer][horizontal_pointer_right] == "X":
            break
        
    #check vertically up
    vertical_pointer_up = position[0] - 1 
    column_pointer = position[1]
    while vertical_pointer_up >= 0: 
        if board[vertical_pointer_up][column_pointer] == "":
            num_of_squares+=1
            vertical_pointer_up -= 1 
        elif board[vertical_pointer_up][column_pointer] == "X":
            break
    
    #check verticall down
    vertical_pointer_down = position[0] + 1 
    column_pointer = position[1]
    while vertical_pointer_down < len(board): 
        if board[vertical_pointer_down][column_pointer] == "":
            num_of_squares+=1
            vertical_pointer_down += 1 
        elif board[vertical_pointer_down][column_pointer] == "X":
            break
    
    #check dioganally upper-right
    vertical_pointer_up = position[0] - 1 
    horizontal_pointer_right = position[1] + 1
    while vertical_pointer_up >= 0 and horizontal_pointer_right < len(board):
        if board[vertical_pointer_up][horizontal_pointer_right] == "":
            num_of_squares += 1
            vertical_pointer_up -= 1 
            horizontal_pointer_right +=1
        elif board[vertical_pointer_up][horizontal_pointer_right] == "X":
            break
    
    
    
    #check dioganally upper-left
    vertical_pointer_up = position[0] - 1 
    horizontal_pointer_left = position[1] -1 
    while vertical_pointer_up >= 0 and horizontal_pointer_left >= 0:
        if board[vertical_pointer_up][horizontal_pointer_left] == "":
            num_of_squares += 1
            vertical_pointer_up -= 1 
            horizontal_pointer_left -= 1
        elif board[vertical_pointer_up][horizontal_pointer_left] == "X":
            break
    
    #check dioganally down-right
    vertical_pointer_down = position[0] + 1 
    horizontal_pointer_right = position[1] + 1
    while vertical_pointer_down < len(board) and horizontal_pointer_right < len(board):
        if board[vertical_pointer_down][horizontal_pointer_right] == "": 
            num_of_squares += 1 
            vertical_pointer_down += 1
            horizontal_pointer_right +=1
        elif board[vertical_pointer_down][horizontal_pointer_right] == "X":
            break
    
    #check dioganally down-left
    vertical_pointer_down = position[0] + 1 
    horizontal_pointer_left = position[1] - 1
    while vertical_pointer_down < len(board) and horizontal_pointer_left >= 0 : 
        if board[vertical_pointer_down][horizontal_pointer_left] == "":
            num_of_squares +=1
            vertical_pointer_down +=1
            horizontal_pointer_left -= 1
        elif board[vertical_pointer_down][horizontal_pointer_left] == "X":
            break
    
    return num_of_squares