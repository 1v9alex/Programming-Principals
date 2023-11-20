#Create and implmenet a playlist class composed of multiple song objects
# make sure to use composite and component classes

class Song:
    def __init__(self, name, artist, album):
        self.name = name
        self.artist = artist
        self.album = album

    def getName(self):
        return self.name

    def getArtist(self):
        return self.artist

    def getAlbum(self):
        return self.album

    def __str__(self):
        return f"'{self.name}' by {self.artist} from '{self.album}'"

class Playlist:
    def __init__(self, name):
        self.name = name
        self.playlist = []

    def addSong(self, song):
        self.playlist.append(song)

    def removeSong(self, song):
        self.playlist.remove(song)

    def getPlaylist(self):
        return self.playlist
    
    def __str__(self):
        playlist_str = '\n'.join(str(song) for song in self.playlist)
        return f"{self.name} playlist:\n{playlist_str}"
    
    def searchSong(self):
        song_name = input("Enter the name of the song you're looking for: ")
        for song in self.playlist:
            if song.getName().lower() == song_name.lower():
                print(f"Found song: {song}")
                view = input("Would you like to view its details? (yes/no): ")
                if view.lower() == 'yes':
                    print(song)
                return
        print("Song not found in this playlist.")

def searchPlaylist(musicLibrary):
    playlist_name = input("Enter the name of the playlist you're looking for: ")
    for playlist in musicLibrary:
        if playlist.name.lower() == playlist_name.lower():
            print(f"Found playlist: {playlist.name}")
            view = input("Would you like to view its contents? (yes/no): ")
            if view.lower() == 'yes':
                print(playlist)
            return
    print("Playlist not found in the music library.")



song1 = Song("Song1", "Artist1", "Album1")
song2 = Song("Song2", "Artist2", "Album2")
song3 = Song("Song3", "Artist3", "Album3")
song4 = Song("Song4", "Artist4", "Album4")
song5 = Song("Song5", "Artist5", "Album5")
song6 = Song("Song6", "Artist6", "Album6")
song7 = Song("Song7", "Artist7", "Album7")
song8 = Song("Song8", "Artist8", "Album8")
song9 = Song("Song9", "Artist9", "Album9")
song10 = Song("Song10", "Artist10", "Album10")

playlist1 = Playlist("Playlist1")
playlist1.addSong(song1)
playlist1.addSong(song2)
playlist1.addSong(song3)
playlist1.addSong(song4)
playlist1.addSong(song5)
playlist1.addSong(song6)
playlist1.addSong(song7)
playlist1.addSong(song8)
playlist1.addSong(song9)
playlist1.addSong(song10)

print(playlist1)

single1 = Song("Single1", "Artist1", "Album1")
single2 = Song("Single2", "Artist2", "Album2")
single3 = Song("Singl3", "Artist3", "Album3")

playlist2 = Playlist("Playlist2")
playlist2.addSong(single1)
playlist2.addSong(single2)
playlist2.addSong(single3)

favsong1 = Song("FavSong1", "Artist1", "Album1")
favsong2 = Song("FavSong2", "Artist2", "Album2")
favsong3 = Song("FavSong3", "Artist3", "Album3")
favsong4 = Song("FavSong4", "Artist4", "Album4")
favsong5 = Song("FavSong5", "Artist5", "Album5")

favouriteSongs = Playlist("Favourite Songs")
favouriteSongs.addSong(favsong1)
favouriteSongs.addSong(favsong2)
favouriteSongs.addSong(favsong3)
favouriteSongs.addSong(favsong4)
favouriteSongs.addSong(favsong5)

#create a music library by putting aol the playlists together in a list and iterating over them
musicLibrary = [playlist1, playlist2, favouriteSongs]

for playlist in musicLibrary:
    print(playlist)
    print()

# Search for a playlist in the music library
searchPlaylist(musicLibrary)

# Search for a song in a playlist
playlist = musicLibrary[0]  # replace 0 with the index of the playlist you want to search in
playlist.searchSong()