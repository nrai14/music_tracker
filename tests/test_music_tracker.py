import pytest 
from lib.music_tracker import * 

"""
User added a new Track to the list
#Adds a new Track to the list
"""

def test_add_track_SnoopDogg():
    entry = MusicTracker() 
    assert entry.add_track("Drop it like its hot", "Snoop Dogg") == "Track has been added"
    assert entry.display_tracks() == ["Drop it like its hot by Snoop Dogg"]
    assert entry.add_track("Walk the dog","Michael Bublé") == "Track has been added"
    assert entry.display_tracks() == ["Drop it like its hot by Snoop Dogg", "Walk the dog by Michael Bublé"]


def test_empty_tracks():
    empty = MusicTracker()
    with pytest.raises(Exception) as e:
        empty.add_track("","")
    error_message = str(e.value)
    assert error_message == "Please enter a track along with artist name."
    
    with pytest.raises(Exception) as e:
        empty.add_track("","a")
    error_message = str(e.value)
    assert error_message == "Please enter a track along with artist name."
    
    with pytest.raises(Exception) as e:
        empty.add_track(""," ")
    error_message = str(e.value)
    assert error_message == "Please enter a track along with artist name."

    with pytest.raises(Exception) as e:
        empty.add_track(" a"," ")
    error_message = str(e.value)
    assert error_message == "Please enter a track along with artist name."

def test_integer():
    integer = MusicTracker()
    with pytest.raises(Exception) as e:
        integer.add_track(69, 88)
    error_message = str(e.value)
    assert error_message == "Please enter text. Track name and artist name."


