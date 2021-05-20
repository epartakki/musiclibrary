## ------------------------------------------------------
##        A simple music library
## ------------------------------------------------------

print("**********************************")
print("*** THIS IS YOUR MUSIC LIBRARY ***")
print("**********************************")
print("")

    
def playSong():
    import webbrowser #will help us play music on a different page
    selection = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ").upper() #user can input choice
    playlist = [] #creates empty list for the dictonaries to be added to
    print("")
    while (selection != "QUIT"): #creation of loop, continues until user inputs quit

        
        if (selection == "ADD"): #runs if user inputs "add"
            song = {} #creates empty dictonary
            title = input("Song title: ") #user adds info on song
            artist = input("Artist: ")
            album = input("Album: ")
            url = input("Spotify URL: ")
            print("")
            song = {"Song title":title, #creates dictionary
                     "Artist":artist,
                     "Album":album,
                     "Spotify URL":url,
                     }
            playlist.append(song) #adds dictionary to list
        
            selection = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ").upper() #asks for input again

            
        elif (selection == "REMOVE"): #runs if user inputs "remove"
            
            song_removal = eval(input("Enter the number of the song you want to remove: "))
            playlist.remove(playlist[song_removal - 1]) #removes song user requested by its index
            selection = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ").upper()

            
        elif (selection == "PLAY"): #runs if user inputs "play"
            
            song_play = eval(input("Which song would you like to play? Enter a number: "))
            for song in playlist: #loops through each dictionary in list
                if playlist.index(song) == song_play - 1: #if the index matches the number the user asked for, that song is played
                    webbrowser.open(url)
            selection = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ").upper()

            
        elif (selection == "PRINT"): #runs if user inputs "print"
            for song in playlist: #runs though each dictionary in list and prints the info about each song
                count = 1 + playlist.index(song)
                print(count , ".","'", song['Song title'] , "'","by", song['Artist'], "(" , song['Album'] , ")")
            selection = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ").upper()
        else: #if user doesnt input a valid choice, program asks again
            print("Please enter a valid option. ")
            selection = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ").upper()


    
def main(): #holds our function
    playSong()
    print("Thank you for listening to music today")
    
   
if __name__ == "__main__": #executes main
    main()

