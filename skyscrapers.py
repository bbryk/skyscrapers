"""
module
>>> read_input("check.txt")
['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']

>>> left_to_right_check("412453*", 4)
True
>>> left_to_right_check("452453*", 5)
False

>>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', \
'*?????*', '*?????*', '*2*1***'])
False
>>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
True
>>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', \
'*35214*', '*41532*', '*2*1***'])
False

>>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
True
>>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
False
>>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', \
'*35214*', '*41532*', '*2*1***'])
False

>>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
True
>>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
False
>>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
False

>>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
True
>>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
False
>>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
False
"""


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    with open(path, 'r', encoding='UTF-8') as file_to_read:
        lines = file_to_read.readlines()
        new_lines = []
        for line in lines:
            line = line.strip()
            new_lines.append(line)
    return new_lines


def reverse_str(string: str) -> str:
    '''
    reverses the line and returns it
    '''
    lst = list(string)
    lst.reverse()
    string = "".join(lst)
    return string


def left_to_right_check(input_line: str, pivot: int) -> bool:
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    # check_first_num = input_line[0]
    # check_last_nime = input_line[-1]

    input_line = input_line[1:-1]

    # 12453
    visible_counter = 1
    for i in range(1, len(input_line)):
        isHigher = True
        for j in range(i):
            if input_line[i] > input_line[j]:
                continue
            else:
                isHigher = False
        if isHigher:
            visible_counter += 1

    if visible_counter == pivot:
        return True

    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', \
    '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', \
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', \
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board:
        if '?' in row:
            return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', \
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', \
    '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', \
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board[1:-1]:
        row = row[1:-1]
        # print(row)
        for pivot in row:
            #print('pivot is '+pivot)
            for i in range(row.find(pivot)+1, len(row)):
                #print('the num is'+row[i])
                if pivot == row[i]:
                    return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', \
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', \
    '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', \
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:-1]
    for row in board:
        first_hint = row[0]
        last_hint = row[-1]
        if first_hint != '*' and not left_to_right_check(row, int(first_hint)):
            return False
        if last_hint != "*":
            row = reverse_str(row)
            if not left_to_right_check(row, int(last_hint)):
                return False
    return True


def side_switch(board: list):
    '''
    rotate matrix by 90 degrees
    '''
    new_board = []

    for row in board:
        new_board.append(list(row))
    # print(new_board)
    b = [[0]*len(board)]*len(board)
    b1 = []

    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            b[i][j] = new_board[j][len(new_board)-i-1]
        b1.append(list(b[0]))
        b2 = []
    for lst in b1:
        strring = "".join(lst)
        b2.append(strring)
    return b2


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness \
    (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = side_switch(board)
    if check_horizontal_visibility(board) and check_uniqueness_in_rows(board):
        return True
    return False


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)
    if check_columns(board) and check_horizontal_visibility(board) and check_uniqueness_in_rows(board) and check_not_finished_board(board):
        return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
