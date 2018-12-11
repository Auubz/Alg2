def make_album(artist_name,song_title, track_number =0):
    album = ("Artist's name: " + artist_name + "   |" + " Song title: " + song_title + " Track Number:   " + str(track_number))
    return (album)


music  = make_album("Purple rain", "Jimmy Hendrix")
music2 = make_album("Smoke on The Water", "Deep Purple")
music3 = make_album("Hey Ya", "Outkast")
music4 = make_album("Gangam Style","Psy",2)

print(music)
print(music2)
print(music3)
print(music4)

while True:
    print("\nPlease give me an Artist + Song")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")

    if artist == 'q':
        break
    song = input("Song: ")
    if song == 'q':
        break

    musica = make_album(artist,song)
    print(musica)

a = 0
