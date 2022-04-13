import json


def initPoints():
    # try to read from file, otherwise return []
    try:
        file = open("points.txt", "r")
        json_points = file.read()
        file.close()
        return json.loads(json_points)
    except:
        return []


def savePoints(points):
    # Convert points to JSON
    json_points = json.dumps(points)

    file = open("points.txt", "w")
    file.write(json_points)
    file.close()


def addPoint(points):
    label = input("Point Label: ")
    x = int(input("x-coordinate: "))
    y = int(input("y-coordinate: "))
    points.append(newPoint(label, x, y))


def newPoint(label, x, y):
    return {
        "label": label,
        "x": x,
        "y": y
    }


def removePoint(points):
    label = input("Enter label of point to remove: ")
    for i in range(len(points)):
        if points[i]["label"] == label:
            points.pop(i)
            break


def printPoints(points):
    for point in points:
        print(f"{point['label']}({point['x']},{point['y']})")
