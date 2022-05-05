import csv
from track import Track
class File:
    def __init__(self, fileName):
        self.fileName = fileName
        self.fileContent = None

    def read(self):
        with open(self.fileName, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            tracks = []
            for row in reader:
                if(row != []):
                    track = Track(row[0], row[1], row[2], row[3])
                    tracks.append(track)
            self.fileContent = tracks
        return tracks
        
    def write(self, data):
        with open(self.fileName, 'w',   encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for track in data:
                writer.writerow([track.name, track.id, track.artist, track.album])


