quit == ""
while quit != "no":
    print("Welcome!")
    print("\n")
    print("----------------------")
    print("\n")
    print("You find yourself in an open field. In front of you is a forest. To your left is a cave, and to the right is more of the field.")
    print("Go left")
    print("Go right")
    print("Go forward")
    print("Go backwards")
    ans = input ("What will you do? ")
    ans = ans.lower()
    while ans != "go left" and ans != "go right" and ans !="go forward" and ans !="go backwards":
        print("That is not a valid answer")
        ans = input ("What will you do? ")
        ans = ans.lower()
    if ans == "go left":
        print("After going left, you find a small cave.")
        print("Enter the cave")
        print("Go back")
        ans = input("What are you going to do? ")
        ans = ans.lower()
        while ans != "enter the cave" and ans != "go back" and ans != "back":
            print("That is not a valid answer")
            ans = input ("What will you do? ")
            ans = ans.lower()
        if ans == "enter the cave":
            print("You decide to forage ahead, through the cave. As you continue forwards, the light of the sun slowly disappears, leaving you in complete darkness. Realizing your mistake, you attempt to turn back and leave the cave. However, as you continue on the way you had believed was the one you had travelled previously, you realize you have not turned back, but have instead gone down a separate path.")
            print("Continue on")
            print("wait")
            ans = input("Will you continue walking or stay and wait? ")
            ans = ans.lower()
            while ans != "continue on" and ans != "wait":
                print("That is not a vaild answer")
                ans = input ("What will you do? ")
                ans = ans.lower()
            if ans == "continue on":
                print("You continue walking on. The cave slowly angles downwards, and you eventually spot a light. You are too excited to leave the cave to think about why the cave would be angling downwards, and move towards the light, with newfound strength. Next thing you know, you are face to face with a large body of lava. Realizing your mistake, you try to run away, but the lava is too fast.")
            elif ans == "wait":
                print("You decide to wait in the cave. You sit, and sit, and sit, and nothing happens. You find this quite disappointing.")
        elif ans == "go back":
            print("You turn back, to the field you started out at and stand in the exact place you were before. You sit down and decide to wait, in hopes that someone will find you and bring you back to civilization with them. You have been sitting there for a while when you look down, and notice something shining on the ground. Picking it up, you realize it is a locket. You spend some time inspecting it, as you do not remember ever owning a locket, in hopes of finding something that can help you out of your predicament. After you are done inspecting it, you realize that it is nothing but a locket, and in the end the hope of finding something on the ground that would help you out of your current predicament is worthless.")
    elif ans == "go right":
        print("You turn to the right, and see that is more of the same, a field decorated with small flowers or various colors. You decide that this is your best option, and start walking. You continue walking, the flowers slowly losing their initial cheery charm. As time go on, you realize that the field doesn't seem to end, continuing off in the distance. You realize that you will likely not escape this field, and your thoughts begin wandering. Why are you alone in a field in the first place? How likely is it for an open field to be next to a forest, cave and cliff anyway? You ponder these thoughts for far too long, and the sun sets. You'll never get back to civilization now.")
    elif ans == "go forward":
        print("You decide to forge ahead, and enter the woods. The temperature drops as you continue on, causing you to shiver. You continue walking through the forest when you come a across a fork in the road.")
        print("Go left")
        print("Go right")
        ans = input("What do you do? ")
        ans = ans.lower()
        while ans != "go left" and ans != "go right":
            print("That is not a valid answer")
            ans = input ("What will you do? ")
            ans = ans.lower()
        if ans == "go left":
            print("You take the left branch of the fork, and continue on, moving through the forest. Eventually, you come across what seems to be an old shrine to a lost god. Suddenly, you hear a rustling behind you, and something hits you on the head, knocking you unconscious...")
        elif ans == "go right":
            print("You decide to take the right branch, and spend a long time walking along the path. After some time, you can see what looks like a light far off in the distance. You continue walking for what seems like forever, the hope of something more important than your lack of food or energy. You eventually make your way to the end of the path, and can once again feel the heat of the sun. In front of you is a small town. You quickly make your way over to the town, searching for someone who could help you. You find a nice old lady who says she will let you stay with her for a while. Your adventure is over... or is it?")
    elif ans == "go backwards":
        print("You decide to try adventuring behind you. You turn and find a cliff. Before you can do anything, the chunk of earth you are standing on suddenly gives way, and you fall. As you fall, you contemplate why you decided to go towards something without any idea what that thing was, and how long it'd been since you actually had anything that resembled self-preservation.")
    quit = input("Do you want to play again? (type no to exit) ")
