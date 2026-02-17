"""
    Alien score keeper
"""

alien_shot = input("What color was the alien? ").lower()

if alien_shot == "green":
    print("You scored 5 points")
elif alien_shot == "yellow":
    print("You socred 10 points")
else:
    print("You scored 15 points")

