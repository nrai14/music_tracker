1. Describe the Problem

> As a user <br>
> So that I can keep track of my music listening <br>
> I want to add tracks I've listened to and see a list of them.

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE
```python
class MusicTracker:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   playList: empty list containing dictionaries
        # playList = 
        # [
        #     { 'song': "Drop it like its hot", 'artist' : "Snoop Dogg" }
        # ]

        # playList[0]['artist']
        # playList[0]['song']

        # playList =  
        # {
        #     'Drop it like its hot' : { 'artist' : "Snoop Dogg" }
        # }

        # playList['Drop it like its hot']['artist']

        # Side effects:
        #   Sets the playList property of the self object 
        pass

    def add_track(self, track, artist):
        # Parameters:
        #   track: string representing a single track
        #   artist: string reprsenting the artist of that track 
        # Returns:
        #   Verification of song and its artist being added
        # 
        # Side-effects
        #   Saves the song to the self object
        pass 

    
    def display_tracks(self):
        # Parameters:
        #   none
        # Returns:
        #   updated playList dictionary
```

3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# EXAMPLE

```python
"""
User added a new Track to the list
#Adds a new Track to the list
"""
result = MusicTracker()
result.add_track("Drop it like it's hot", "Snoop Dogg") # => "Track has been added."

"""
User added a new Track to the list
#Displays the new Track in the list
"""
result = MusicTracker()
result.add_track("Drop it like it's hot", "Snoop Dogg") # => "Track has been added."
result.display_tracks() # => ["Drop it like it's hot by Snoop Dogg"]


"""
User added multiple new Tracks to the list
#Displays the Tracks in the list
"""
result = MusicTracker()
result.add_track("Drop it like it's hot", "Snoop Dogg") # => "Track has been added."
result.display_tracks() # => ["Drop it like it's hot by Snoop Dogg"]


"""
Given an empty string to add into list
#add_track raises an exception
"""
result = MusicTracker()
result.add_track("", "") # raises an error with the message "Please enter a track along with artist name."

"""
Given an integer to add into list
#add_track raises an exception
"""
result = MusicTracker()
result.add_track(5, 5) # raises an error with the message "Please enter text. Track name and artist name."

```