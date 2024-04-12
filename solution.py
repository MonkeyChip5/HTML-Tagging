"""
Joseph Wu
CMSC389O section 0301
uid: 118956183
I pledge on my honor that I have not given or received any unauthorized 
assistance on this assignment/examination.

The problem my code solves: 
My code checks to make sure the given list of HTML tags are valid. We have
defined valid tags as tags that start with < or </ and end with >. Tags 
should be closed in the reverse/mirror order they were opened in.

How does my code work?
My code takes in a stack/list and I create a new empty one. When iterating 
through the given input list, I check if the tag is an openning or a closing 
tag. If the tag is an openning one, I add it to the end of the list. If the
tag is a closing tag, I pop the the last element of the list and check if 
that tag was the most recent one that was opened. If the tag is not the 
most recent tag, I return False because it is an invalid list of HTML tags. 
If the tag does not start with a < or </ then it is not a valid tag. 


Time Complexity Analysis:
The time complexity is O(n) because I iterate through the whole list/every 
tag once. The for loop runs for n times. All the if statement checks, 
return statements, variable declaration, poping and appending take a constant
time. 

Auxiliary Space Analysis:
The Aux Space is also O(n) because the stack I use to keep track of the tags 
grows with the number of tags in the input list or n size.
"""



def isValid(tags):
    #empty list/stack to store opening tags
    stack = []

    #iterate through all the tags
    for tag in tags:    

        #checks if tag is a closing tag
        if tag.startswith('</'):
            #checks if stack is empty before call pop to prevent errors
            if not stack:
                return False
            #store tag to look at for later and remove from list/stack
            see_tag = stack.pop() 
            #compares opening and closing tag to make sure they match
            if tag[2:] != see_tag[1:]:
                return False
        
        #checks if tag is an opening tag
        elif tag.startswith('<'):
            stack.append(tag) #add tag to list/stack
            print("running")
        
        #tag is not a opening or a closing tag (invalid tag)
        else:
            return False

    #returns whether list/stack is empty (should be empty if tags were valid)
    return not stack
