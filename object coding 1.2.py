#james ellis + alan arvizu

bball_weight = 5.25
ball_circumference = 9.20
ball_color= "white"
stitching_color= "red"
ball_shape= "sphere"
in_hand= True
ball_thrown = True

def throw_ball():
    if in_hand:
        print("you can throow ball")
    else:
        print("you can't throw ball")


def catch_ball():
    if ball_thrown:
        print ("the balll has been thrown , catch it if you can")
    else:
        print("you cant catch a ball that has not been thrown")

