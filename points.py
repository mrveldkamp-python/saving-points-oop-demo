import json


class Point:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.label}({self.x},{self.y})"

    def as_dictionary(self):
        return {
            "label": self.label,
            "x": self.x,
            "y": self.y
        }


def initPoints():
    # try to read from file, otherwise return []
    try:
        # Load points dictionary from file - parse JSON
        file = open("points.txt", "r")
        json_points = file.read()
        file.close()
        points_dictionary = json.loads(json_points)

        # Convert points_dictionary to array of Point objects
        temp = []
        for point in points_dictionary:
            temp.append(Point(point["label"], point["x"], point["y"]))
        return temp
    except:
        return []


def savePoints(points):
    # Copy points to an array of dictionaries
    points_copy = []
    for i in range(len(points)):
        points_copy.append(points[i].as_dictionary())

    # Convert points copy to JSON
    json_points = json.dumps(points_copy)

    file = open("points.txt", "w")
    file.write(json_points)
    file.close()


def addPoint(points):
    label = input("Point Label: ")
    x = int(input("x-coordinate: "))
    y = int(input("y-coordinate: "))
    points.append(Point(label, x, y))


def removePoint(points):
    label = input("Enter label of point to remove: ")
    for i in range(len(points)):
        if points[i].label == label:
            points.pop(i)
            break


def printPoints(points):
    for point in points:
        print(point)
