
class Track:
    def __init__(self, name, id, artist, album):
        self.name = name
        self.id = id
        self.artist = artist
        self.album = album
    
    def __str__(self):
        return self.name + " " + self.id + " " + self.artist + " " + self.album
    
    def nameIsSimilar(self, track):
        if Track.isSimilar(self.name, track.name) and Track.isSimilar(track.name, self.name) and self.artistIsSimilar(track):
            return True
        return False

    def artistIsSimilar(self, track):
        return Track.isSimilar(self.artist, track.artist)
        
    def isSimilar(string1, string2):
        count = 0
        words = string1.split()
        targetWords = string2.split()
        totalCount = len(targetWords)
        for word in words:
            if word in targetWords:
                count += 1
        if(totalCount == 0):
            return False
        return count/totalCount > 0.5

    

    


    