import MineStats.HypixelStats as hypixel
import MineStats.YoutubeInfo as yt_info
import Colors as color

while True:
    start = input("""Welcome to MineStats
    
    Here you can see all find all your favorite youtube gamers and stats at the same time
    
    Continue (y/n): """)

    if start.lower() == "n":
        print("Now exiting MineStats")
        break