#input 3 signal values  (red,green,yellow) and then disply the appropriate message for the traffic
# also check for pedestrians
# red message = stop
# green message = go
# yellow message = prepare to stop
# if pedestrian is present, display "wait for pedestrian"
# also have advanced green signal for left turn


redMessage = "Stop"
greenMessage = "Go"
yellowMessage = "Prepare to stop"
pedestrianMessage = "Wait for pedestrian"
leftTurnMessage = "Advanced green for left turn"

red = False
green = True
yellow = False
pedestrian = False
leftTurn = True

if red:
    print(redMessage)
    if pedestrian:
        print(pedestrianMessage)
    if red and leftTurn:
        print(leftTurnMessage)
elif green:
    print(greenMessage)
    if leftTurn:
        print(leftTurnMessage)
elif yellow:
    print(yellowMessage)
    if pedestrian:
        print(pedestrianMessage)
else:
    print("Invalid signal")