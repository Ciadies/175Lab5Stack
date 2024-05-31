import os
from time import sleep
import stack

#----------------------------------------------------
# Lab 5 Problem B: BROWSE-175
# Purpose of program:
#
# Author: Sebastian
# Collaborators/references:
#----------------------------------------------------

os.system("")  # enables ANSI characters in terminal

def print_location(x, y, text):
    '''
    Prints text at the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
        - text (str): text to print
    Returns: N/A
    '''
    print ("\033[{1};{0}H{2}".format(x, y, text))

def clear_screen():
    '''
    Clears the terminal screen for future contents.
    Input: N/A
    Returns: N/A
    '''
    if os.name == "nt":  # windows
        os.system("cls")
    else:
        os.system("clear")  # unix (mac, linux, etc.)
        
def display_error(error):
    '''
    Displays an error message under the current site as specificed by "error".
    Input:
        - error (str): error message to display
    Returns: N/A
    '''
    move_cursor(0, 3)
    print("\033[6;31;40m{:^80}\033[0m".format(error))
    sleep(0.6)
    clear_screen()

def print_header():
    '''
    Prints the BROWSE-175 header.
    Input: N/A
    Returns: N/A 
    '''
    print("\033[0;32;40m{:^80}\033[0m".format("[ BROWSE-175 ]"))

def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: N/A
    '''
    print("\033[{1};{0}H".format(x, y), end='')

def display_current_site(current):
    '''
    Displays the current site underneath the header.
    Input:
        - current (str): current site
    Returns: N/A
    '''
    print("\033[2;32;40m{:^80}\033[0m".format("Currently viewing: " + current))
    print("\033[4;30;40m{:^80}\033[0m".format(""))

def display_hint(message):
    '''
    Displays navigation hint message in the terminal.
    Input:
        - message (str): navigation hint message
    Returns: N/A
    '''
    print("\033[40;30;47m{:^80}\033[0m".format(message))

def display_buttons(back, fwd):
    '''
    Displays the navigational buttons at the top of the terminal.
    "(<) BACK" and "FORWARD (>)" labels should only be displayed
    if there are sites to go back or forward to.
    Input: 
        - back: stack of previous sites
        - fwd: stack of forward sites
    Returns: N/A
    '''
    if not back.isEmpty() and not fwd.isEmpty():
        print("%-40s%40s"%("Back(<)","Forward(>)"))
    elif not back.isEmpty():
        print("%-80s"%("Back(<)"))
    elif not fwd.isEmpty():
        print("%80s"%("Forward(>)"))

    

def goToNewSite(current, back, fwd):
    '''
    updates the stacks so that backwards has the previous current site and forward is emptied
    Inputs: string of site, two stacks for backwards and forwards
    Returns: string of a new site
    '''
    site = input("Please enter the desired url: ")
    back.push(current)
    fwd.clear()
    return site

def goBack(current, bck, fwd):
    '''
    updates the stacks so that forwards has the previous current site and backwards gets pop-ed
    Inputs: string of site, two stacks for backwards and forwards
    Returns: string of a new site
    '''    
    try:
        newCurrent = bck.pop()
        fwd.push(current)
    except Exception:
        display_error("Cannot go Back")
        newCurrent = current
    finally:
        return(newCurrent)

def goForward(current, bck, fwd):
    '''
    updates the stacks so that backwards has the previous current site and forward gets pop-ed
    Inputs: string of site, two stacks for backwards and forwards
    Returns: string of a new site
    '''    
    try:
        newCurrent = fwd.pop()
        bck.push(current)
    except Exception:
        display_error("Cannot go Forward")
        newCurrent = current
    finally:
        return(newCurrent)

def main():
    HOME = 'www.cs.ualberta.ca'
    back = stack.Stack()
    fwd = stack.Stack()
    current = HOME
    quit = False
    
    while not quit:
        clear_screen()
        print_header()
        display_current_site(current)

        # TODO: call display_buttons to show navigational buttons
        display_buttons(back, fwd)

        move_cursor(0, 20)
        display_hint("Use <, > to navigate, = to enter a URL, q to quit")
        print_location(5, 5, "Action: ")
        move_cursor(13, 5)
        action = input()
        if action == '=':
            current = goToNewSite(current, back, fwd)
        elif action == '<':
            current = goBack(current, back, fwd)
        elif action == '>':
            current = goForward(current, back, fwd)
        elif action == 'q':
            clear_screen()
            quit = True
        else:
            display_error('Invalid action!')
  

if __name__ == "__main__":
    main()