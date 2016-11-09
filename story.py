#choices = ["A" or "B"]
import time
print("~~~~~~~~~~~~~~~~~~~~~")
print("This is a story")
print("~~~~~~~~~~~~~~~~~~~~~")
name = input("What is your name?: ")
print("Hi", name, "!", "This is your story.")
time.sleep(2)
print("You wake up in a cold, dark room with only one small window.")
time.sleep(2)
print("Do you: ")
print("A: Try to squeeze through the small window? ")
time.sleep(1)
print("or")
time.sleep(1)
print("B: Go back to sleep on the cold, dirty floor? ")
choice1 = input("Type A or B: ")
if choice1 == "a" or choice1 == "A":
    time.sleep(2)
    print("You managed to squeeze through the small window only to end up in an even darker cemetery...")
    time.sleep(2)
    print("You can see a dim light in the distance.")
    time.sleep(2)
    print("Do you: ")
    print("A: Go towards the dim light? ")
    time.sleep(1)
    print("or")
    time.sleep(1)
    print("B: Stay and wait? ")
    choice2a = input("Type A or B: ")
    if choice2a == "A" or choice2a == "a":
        print("You made it out alive somehow...")
















if choice1 == "b" or choice1 == "B":
    print("You lay yourself down on the cold floor again only to later die of starvation & dehydration. RIP.")



else:
    print("You became confused and died. RIP.")

