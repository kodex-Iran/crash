from numpy import random
class randompy():
    perday = 1
    maxlikes = 680
    maxComment = 170
    maxfallow = 130 
    day = 3600
    hour = 60
    def likerandom():
        maxLikePerMitute = (680 / 1440)
        maxLikePerHour= int(maxLikePerMitute*60)
        print("maxLikePerHour")
        print(maxLikePerHour)
        print("maxLikePerMitute")
        print(maxLikePerMitute)
        cal = int(60/maxLikePerHour)
        export = random.randint(cal)
        return cal

