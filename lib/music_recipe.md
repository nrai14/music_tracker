1. Describe the Problem
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE

class MusicTracker:
    # User-facing properties:
    #   name: string

    def __init__(self, artist, song):
        # Parameters:
        #   todo: string
        #   masterlist: empty list
        # Side effects:
        #   Sets the todo property of the self object
        #   Sets the masterlist property of the self object 
        pass

    def add_track(self, track):
        # Parameters:
        #   task: string representing a single track
        # Returns:
        #   Verification of song being added
        # 
        # Side-effects
        #   Saves the song to the self object
        pass 

    
    def display_tracks(self):
        # Parameters:
        #   none
        # Returns:
        #   updated music tracks dictionary

3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# EXAMPLE

"""
User added a new task to the list
#Adds a new task to the list
"""
result = MusicTracker()
result.add_todo("Walk the dog")
result.add_todo() # => "Task has been added."

"""
Given an empty string to add into list
#add_todo raises an exception
"""
result = TodoList()
result.add_todo("") # raises an error with the message "Please enter a task."

"""
Given an integer to add into list
#add_todo raises an exception
"""
result = TodoList()
result.add_todo(5) # raises an error with the message "Please enter text."

"""
Successfully deleted a task
#Shows the user an updated list 
"""
result = TodoList()
masterlist = ["Walk the dog", "eat", "sleep"]
result.completed_tasks("eat")
result.completed_tasks() # => "Walk the dog", "sleep"