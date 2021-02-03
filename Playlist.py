from Song import Song

class Playlist:
  def __init__(self):
    #our head
    self.__first_song = None

  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)
    #next song is current first song
    new_song.next = self.__first_song
    #now that we have a new song, our head becomes the new_song
    self.__first_song = new_song


  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    current_song = self.__first_song
    found = False
    counter = 0

    while current_song != None and not found:
      #Checking to see if our current song is the title we are looking for
      if current_song.get_title() == title:
        found = True
      #if its not, then it will go to the next song and add 1 to the counter to help find its index
      else:
        current_song = current_song.next()
        counter += 1

    if found:
      return found
    else:
      return -1


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    current_node = self.__first_song

    previous = None
    found = False

    #What this method is doing, is looking for the song we want. If we cant find it then we will cycle through until its found
    while not found:
      if current_node.get_title() == title:
        found = True
      else:
        current = current_node.get_next_song()
        previous = current
    #once we find it it wil change our song to the next song remove it from the list
    if previous == None:
      self.__first_song = current_node.get_next_song()
    else: 
      previous.set_next_song(current_node.get_next_song())


  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    counter = 0
    current_node = self.__first_song

    while current_node != None:
      counter += 1
      current_node = current_node.next
    return counter


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current_node = self.__first_song

    if current_node == None:
      print(f'This playlist has no songs! Add some songs!')

  