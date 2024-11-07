# Simple pygame program

# Import and initialize the pygame library
import pygame

#initializes the pygame 
pygame.init()



# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Setting the title
pygame.display.set_caption('Space Game')


while True:

    # Going through all the events that can happen in pygame using a forloop
    # and looking in one of those event is pygame.QUIT(when user exit the window)
    #then the close the pygame program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    #draw.circle(surface=the screen you want it to appear, color= in rgb, (x,y)coordinates, radius)
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Show the updates happening in the screen
    pygame.display.update()
