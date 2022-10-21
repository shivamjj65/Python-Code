from turtle import *
# turtle is 2d graphic module in python allows to make simple art/designs to visualize things

'''shape("turtle") #shape of cursor
#moving cursor head
forward(120)
left(75) #turn at angle
forward(100)
right(50)
backward(200)
'''
shape("turtle")
#creating tree
def tree(size,levels,angle):
    # size is length of branch, level is levels of tree, angle is angle between branches
    if levels==0:
        color("green")
        dot(size)
        color("black")
        return

    forward(size)

    right(angle)
    tree(size*0.8,levels-1,angle) # recursion

    left(angle*2)
    tree(size * 0.8, levels - 1, angle)  # recursion

    right(angle)
    backward(size)
left(90)
tree(70,7,30)
mainloop() # keep screen open