# Saving Points OOP Demo - FIle IO and JSON

from points import *


def main():
    # Initialize Points List
    points = initPoints()

    # Main Menu Loop
    while True:
        selection = getMenuSelection()

        if selection == "1":
            addPoint(points)
            savePoints(points)
        elif selection == "2":
            removePoint(points)
            savePoints(points)
        elif selection == "3":
            printPoints(points)
        elif selection == "4":
            break


def getMenuSelection():
    print("\nMAIN MENU")
    print("1: Add a Point")
    print("2: Remove a Point")
    print("3: Print Points")
    print("4: Exit")
    return input("Enter menu selection(1-4): ")


# Call main to begin program
main()
