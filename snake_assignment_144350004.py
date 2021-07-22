import pygame
import sys, time, random

#initial game variables

# Window size
frame_size_x = 720
frame_size_y = 480

#Parameters for Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = 'RIGHT'
change_to = direction

#Parameters for food
food_pos = [0,0]
food_spawn = False

score = 0


# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()






def check_for_events():
    """
     This should contain the main for loop (listening for events). You should close the program when
     someone closes the window, update the direction attribute after input from users. You will have to make sure
     snake cannot reverse the direction i.e. if it turned left it cannot move right next.
     """
    global change_to
    global direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT' 

    # if pygame.key.get_pressed()[pygame.K_UP] and direction!='DOWN':
    #     direction = 'UP'
    # if pygame.key.get_pressed()[pygame.K_DOWN] and direction!='UP':
    #     direction = 'DOWN'
    # if pygame.key.get_pressed()[pygame.K_LEFT] and direction !='RIGHT':
    #     direction = 'LEFT'
    # if pygame.key.get_pressed()[pygame.K_RIGHT] and direction!='LEFT':
    #     direction =  'RIGHT'
    
    if change_to == 'UP' and direction !='DOWN':
        direction = 'UP'  
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'                   
   
def update_snake():
    """
    This should contain the code for snake to move, grow, detect walls etc.
    """
    # Code for making the snake move in the expected direction
    # global score
    # global food_pos
    # global snake_pos
    # global snake_body

    if direction =='RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    
    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions 
    # since we have not made snake and food as a specific sprite or surface.
    
    snake_body.append(list(snake_pos)) 

    # End the game if the snake collides with the wall or with itself. 
    if snake_pos[0]+0 <=0 or snake_pos[0] >= frame_size_x:
        game_over()
    if snake_pos[1]+0 <= 0 or snake_pos[1] >= frame_size_y:
        game_over()

    for square in snake_body[:-1]:
        if pygame.Rect(square[0],square[1],10,10).colliderect(pygame.Rect(snake_pos[0],snake_pos[1],10,10)):
            sys.exit()

def create_food():
    """ 
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
    global food_spawn
    global food_pos
    if food_spawn == False:
        food_pos = [random.randrange(40,frame_size_x-40),random.randrange(40,frame_size_y-40)]    
        food_spawn = True
    pygame.draw.rect(game_window, (200,200,200), (food_pos[0],food_pos[1],10,10))



def show_score(pos, color, font, size):
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
    
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render('Score:' +str(score),True, color)
    font_pos = score_surface.get_rect(center = pos)
    game_window.blit(score_surface,font_pos)


def update_screen():
    """
    Draw the snake, food, background, score on the screen
    """
    show_score((40,30),(150,150,150),'timesnewroman',15)    
    pygame.display.update()

   


def game_over():
    """ 
    Write the function to call in the end. 
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    message_font = pygame.font.SysFont('timesnewroman',40)
    game_message_surface = message_font.render('Total Score:' +str(score),True,(0,0,150))
    game_message_rect = game_message_surface.get_rect()

    game_message_rect.midtop = (frame_size_x/2,frame_size_y/2)

    game_window.blit(game_message_surface,game_message_rect)
    pygame.display.flip()

    time.sleep(3)
    pygame.quit()
    sys.exit()



# Main loop
while True:

    # Make appropriate calls to the above functions so that the game could finally run
    check_for_events()
    
    game_window.fill((0,0,0))
    for square in snake_body:
        pygame.draw.rect(game_window,(0,200,0),(square[0],square[1],10,10))
    
    update_snake()
       
    create_food()
    if pygame.Rect(snake_pos[0],snake_pos[1],10,10).colliderect(pygame.Rect(food_pos[0],food_pos[1],10,10)):
        food_spawn = False
        score +=1        
    else:
        snake_body.pop(0)
   
    update_screen()
    

    
    # To set the speed of the screen
    fps_controller.tick(15)