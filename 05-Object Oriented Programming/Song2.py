# Compare this file with Song.py
# Here we removed cyclic dependencies.
# Mainly, Album -> Artist removed and Song -> Artist is removed
# The dependency hierarchy now is Artist -> Album -> Songs


class Song(object):
    """
    Class to represent a song

    Attributes:
        title (str): The title of the a song
        duration (int): The duration of the song in seconds. May be zero.
    """

    def __init__(self, title, duration=0):
        self._title = title
        self.duration = duration

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def del_title(self):
        del self._title

    title = property(get_title, set_title, del_title)

    def __eq__(self, other):
        return self.title == other.title and self.duration == other.duration

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f'Song with title "{self.title}"'


class Album:
    """ Class to represent an Album, using it's track list

        Attributes:
            name (str): The name of the album.
            year (int): The year was album was released.
            tracks (List[Song]):  A list of the songs on the album.

        Methods:
            add_song: Used to add a new song to the album's track list. If a song already exists
            in the album, then the song is not added again to the album
    """

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.tracks = []

    def add_song(self, song, artist, position=None):
        """Adds a song to the track list
        if a song already exists in the album, then the song is not added again to the album
        Args:
            song (Song): A song to add
            artist (Artist): the artist of the song
            position (Optional[int]): If specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise, the song will be added to the end of the list.
        """
        # check does the song exist already in the Album
        song_exists_already = False
        for track in self.tracks:
            song_exists_already = track == song  # calls Song.__eq__
            if song_exists_already:
                break

        if song_exists_already:
            print(f'Album.add_song(): Ignoring a duplicate {song} by {artist} in {self}')   # Calls Song.__str__()
        else:
            if position is None:
                self.tracks.append(song)
            else:
                self.tracks.insert(position, song)

    def __str__(self):
        return f'Album "{self.name}" in year {self.year}'

    def __eq__(self, other):
        return self.name == other.name and self.year == other.year

    def __ne__(self, other):
        return not self.__eq__(other)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums.

    Methods:
        get_album: returns an album object (with album_name and album_year and artist (self))
        from self.albums
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.name

    def get_album(self, album_name, album_year):
        """
        If there is an album with album_name, album_year and self (Artist) in self.albums, returns
        that album object. Otherwise, it creates a new album object with album_name, album_year and album_artist
        and appends the album object to the self.albums. The album object is returned as a result

        :param album_name (str)
        :param album_year (int)
        :return (Album): album object which is from self.albums
        """
        result = None
        album_to_search = Album(album_name, album_year)
        for album in self.albums:
            if album == album_to_search:  # the contents match, calls Album.__eq__()
                result = album
                break
        if result is None:
            self.albums.append(album_to_search)
            result = album_to_search
        return result


class ArtistList:
    def __init__(self):
        self.__artist_list = []

    def get_artist(self, artist_name):
        """
        Returns an Artist object from self.__artist_list (with artist_name). If an artist
        object with artist_name is not found in self.__artist_list, an Artist object with
        artist_name is added to it
        :param artist_name : str
        :return: An (added) artist object from self.__artist_list
        """
        result = None
        for artist in self.__artist_list:
            if artist.name == artist_name:
                result = artist
                break
        if result is None:
            result = Artist(artist_name)
            self.__artist_list.append(result)
        return result

    def __len__(self):
        return len(self.__artist_list)

    def write_artist_list_to_file(self, file_name):
        with open(file_name, 'w') as file:
            for artist in self.__artist_list:
                for album in artist.albums:
                    for song in album.tracks:
                        print(f'{artist.name}\t{album.name}\t{album.year}\t{song.title}', file=file)
            file.close()


def populate_artist_list(filename):
    artist_list = ArtistList()
    with open(filename, 'r') as lines:
        for line in lines:
            artist_name, album_name, album_year, song_name = tuple(line.strip('\n').split('\t'))
            # print(f'{artist_name} {album_name} {album_year} {song_name}')
            album_year = int(album_year)
            artist = artist_list.get_artist(artist_name)
            album = artist.get_album(album_name, album_year)
            song = Song(song_name, artist)
            album.add_song(song, artist)
        lines.close()
    return artist_list


if __name__ == '__main__':
    source_file_name = 'albums.txt'
    artist_list = populate_artist_list(source_file_name)
    print(f'There are {len(artist_list)} artists in {source_file_name}')
    destination_file_name = 'albums_by_song_py.txt'
    artist_list.write_artist_list_to_file(destination_file_name)
