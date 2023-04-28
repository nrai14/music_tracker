class MusicTracker():
    def __init__(self):
        self.playList = {}
    
    def add_track(self, track, artist):
        if isinstance(track, int) and isinstance(artist, int):
        # if track is int and artist is int:
            raise Exception("Please enter text. Track name and artist name.") 

        elif track.strip() == "" or artist.strip() == "":
            raise Exception("Please enter a track along with artist name.")
        
        else:
            self.playList[track] = {'artist' : artist}
            return "Track has been added"
    
    def display_tracks(self):
        answer = []
        for track in self.playList:
            answer.append(f"{track} by {self.playList[track]['artist']}")
            
        return answer
