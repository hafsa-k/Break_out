import pgzrun
from pgzhelper import *

WIDTH = 800
HEIGHT = 600

#point
calmness_point = 0

#song
music.play('music_background')

def on_music_end():
    music.play('end_game')

#end game 

end_game = False

all_bricks = []

temps = 100

#creation de line au fur et à mesure
def creation_lines(): 
    for x in range(8):
        brick = Actor("brick_2", anchor=["left", "top"])
        brick.pos = [x * 100, 0]
        all_bricks.append(brick)
    

#background moving
# background = Actor("background1")
# bg_images = ["background1", "background0"]
# background.images = bg_images          


#background pastel
background = Actor("background_pastel")     


player = Actor("player")
player.pos = [WIDTH/2, 550]


ball = Actor("ball")
ball.pos = [WIDTH/2, 500]
ball_speed = [3, -3]



def on_mouse_move(pos):
    # player.x = pos[0]
    player.pos = [pos[0], player.pos[1]]


def invert_horizontal_speed():
    ball_speed[0] = ball_speed[0] * -1

def invert_vertical_speed():
    ball_speed[1] = ball_speed[1] * -1

#ball respawn
def ball_spawn():
    
    global ball_speed 
    ball.pos = [player.x, 500]
    ball_speed = [3, -3]

    

def update():



#background image
    # background.next_image()

#creation de line au fur et à mesure
    global temps
    if temps > 0 : 
        temps = temps - 1
        if temps == 0 :
            for brick in all_bricks:
                brick.y = brick.y + 30
                #end game & ball disable
                global end_game
                if brick.y == 600:
                    end_game = True
                    ball.pos =[-100, -100]
                    return
            creation_lines()
            temps = 600


    new_x = ball.pos[0] + ball_speed[0]
    new_y = ball.pos[1] + ball_speed[1]
    ball.pos = [new_x, new_y]

    if ball.right > WIDTH or ball.left < 0:
        invert_horizontal_speed()
    
    if ball.top < 0:
        invert_vertical_speed()

    if ball.colliderect(player):
        invert_vertical_speed()

    #ball respawn
    if ball.y > HEIGHT: 
        ball_spawn()

   
        
    

    for brick in all_bricks:
        global calmness_point
        if ball.colliderect(brick):
            sounds.hit.play()
            all_bricks.remove(brick)
            calmness_point += 1

            invert_vertical_speed()

            


    



def draw():
 
    
    
    #background
    background.draw()
    player.draw()
    ball.draw()
    screen.draw.text("Point of calmness : "  + str(calmness_point), center=(100, 580), color=(128,101,166), fontsize=20)       
    

    for brick in all_bricks:
        brick.draw()

#end game
    if end_game:
        screen.clear()
        on_music_end()   
        background.draw()
        screen.draw.text("Hope you did enjoy the game, \n you have gain "  + str(calmness_point) + " points of calmness ", center=(WIDTH/2, HEIGHT/2), color=(242,229,213), fontsize=60)       
    


    
    
    
# DERNIERE LIGNE ONLY
pgzrun.go()
