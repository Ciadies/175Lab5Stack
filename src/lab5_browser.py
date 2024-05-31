#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    Asks the user for a character input and returns it 
    Inputs: N/A
    Returns: string of an action character
    '''
    action = input("Please enter; = to go to a new website; < to go back; > to go forward; or q to quit: ")
    if not action in "<>=q":
        raise Exception("Invalid Entry")
    else:
        return action

def goToNewSite(current, bck, fwd):
    '''
    updates the stacks so that backwards has the previous current site and forward is emptied
    Inputs: string of site, two stacks for backwards and forwards
    Returns: string of a new site
    '''   
    site = input("Please enter the desired url: ")
    bck.push(current)
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
        print("Cannot go Back")
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
        print("Cannot go Forward")
        newCurrent = current
    finally:
        return(newCurrent)

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    