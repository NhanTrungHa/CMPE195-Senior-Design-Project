import API
import sys

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def main():
    log("Running...")
    API.setColor(0, 0, "G")
    API.setText(0, 0, "abc")
    while True:
        if API.wallRight() and not API.wallFront():
            API.moveForward()
        if API.wallFront() and not API.wallRight():
            API.turnRight()
            API.moveForward()
        if not API.wallFront() and not API.wallRight():
            API.turnRight()
            API.moveForward()
        if API.wallRight() and API.wallLeft() and API.wallFront():
            API.turnRight()
            API.turnRight()
        if API.wallFront() and API.wallRight():
            API.turnLeft()

if __name__ == "__main__":
    main()