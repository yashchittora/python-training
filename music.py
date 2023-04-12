from pygame import mixer

mixer.init()

mixer.music.load("Tum se Hi.mp3")
mixer.music.set_volume(10)

mixer.music.play()

while(True):
    print("P to pause , R to Resume , E to exit")
    c = input("Enter choice : ")
    if c.lower() == 'p':
        mixer.music.pause()
    
    elif c.lower() == 'r':
        mixer.music.unpause()
    
    elif c.lower() == 'e':
        mixer.music.stop()
    



