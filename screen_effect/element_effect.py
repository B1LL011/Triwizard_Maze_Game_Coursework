import pygame
import sys
import random
import time
import os
current_file = os.path.abspath(__file__)
p_dir = os.path.dirname(current_file)
gp_dir = os.path.dirname(p_dir)
dice_path = os.path.join(gp_dir,"all_image")
""""
# initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
#pygame.display.set_caption("rotating dice")
"""
def pop_Die(screen, target_result):
    # Color definition
    WHITE = (255, 255, 255)

    # Load 6 dice images and scale them to fit the screen
    dice_images = [pygame.image.load(f"{dice_path}/dice{i}.png") for i in range(1, 7)]
    dice_images = [pygame.transform.scale(img, (70, 70)) for img in dice_images]

    # Create a clock to control the frame rate
    clock = pygame.time.Clock()

    # Function to display a dice with a rotation angle at the center of the screen
    def show_dice(index, angle=0):
        dice = dice_images[index - 1]  # Select the dice image based on the index
        if angle != 0:
            dice = pygame.transform.rotate(dice, angle)  # Rotate the dice if an angle is provided
        rect = dice.get_rect(center=(638, 352))  # Get the rectangle and position the dice in the center
        screen.blit(dice, rect)  # Draw the dice on the screen
        return rect  # Return the rectangle to know the updated area for display update

    # Rotate the dice for 1 second
    start_time = time.time()
    while time.time() - start_time < 1.0:
        angle = ((time.time() - start_time) * 1000) % 360  # Calculate the rotation angle
        random_index = random.randint(1, 6)  # Randomly select a dice image
        dice_rect = show_dice(random_index, angle)  # Display the rotated dice and get its rectangle
        pygame.display.update(dice_rect)  # Update only the area covered by the dice
        clock.tick(60)  # Limit the frame rate to 60 FPS

    # Show the target dice result without rotation
    dice_rect = show_dice(target_result)  # Display the final result
    pygame.display.update(dice_rect)  # Update only the area covered by the dice

    # Pause for 1 second to show the final result
    time.sleep(1)

"""
#test code:


pygame.init()
screen = pygame.display.set_mode((400, 400))
pop_Die(screen,5)
"""

def prompt_and_show_p_num(screen):
    pygame.font.init()
    font = pygame.font.SysFont("comic sans ms", 20)
    big_font = pygame.font.SysFont("comic sans ms", 30)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    input_number = None
    clock = pygame.time.Clock()

    while input_number is None:
        #screen.fill(WHITE)

        # display prompt

        prompt_text = font.render("Press a number (1-4)", True, WHITE)
        center_pos = prompt_text.get_rect(center=(123, 360))
        screen.blit(prompt_text, center_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    input_number = int(event.unicode)

        pygame.display.update()
        clock.tick(30)


    # clear and display input
    #screen.fill(WHITE)

    number_surface = big_font.render("pawn "+str(input_number), True, WHITE)
    number_rect = number_surface.get_rect(center=(123, 390))
    screen.blit(number_surface, number_rect)
    pygame.display.update()

    # wait 1 sec
    pygame.time.wait(1000)

    return input_number




def draw_text(screen, text, pos, font_size=16, color=(255, 255, 255)):
    """
    Draws text on the screen at the given position.

    :param screen: The Pygame screen surface
    :param text: The string to render
    :param pos: (x, y) position to place the text
    :param font_size: Font size
    :param color: Font color (default white)
    :return: The rect of the rendered text (used for clearing later)
    """
    font = pygame.font.SysFont("comic sans ms", font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=pos)
    screen.blit(text_surface, text_rect)
    pygame.display.update(text_rect)
    return text_rect  # return rect for clearing later


def clear_text(screen, text_rect, bg_surface):
    """
    Clears previously drawn text by covering it with background.

    :param screen: The Pygame screen surface
    :param text_rect: The rect returned by draw_text
    :param bg_surface: Background surface (e.g., your background image)
    """
    screen.blit(bg_surface, text_rect, text_rect)
    pygame.display.update(text_rect)




def countdown_timer(screen, duration, bg_img = None,position=(633,345), font_size=500, font_color=(255,0,0), bg_color=(255, 255, 255)):
    """
    Display a countdown timer on the Pygame screen.

    Parameters:
        screen: The Pygame display surface.
        duration: Countdown duration in seconds.
        position: (x, y) coordinates to display the timer.
        font_size: Size of the font used.
        font_color: Color of the text (RGB).
        bg_color: Background color (RGB).
    """
    font = pygame.font.SysFont(None, font_size)
    start_time = time.time()
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.blit(bg_img,(0,0))

        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Calculate remaining time
        elapsed = time.time() - start_time
        remaining = max(0, int(duration - elapsed))

        # Render and display the remaining time
        text = font.render(str(remaining), True, font_color)
        text_rect = text.get_rect(center=position)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

        # Stop the loop when the countdown reaches 0
        if remaining == 0:
            running = False
            pygame.time.delay(1000)  # Optional: pause for 1 second to show "0"




def load_and_play_music(music_path, volume=0.5, loops=-1, start=0.0):
    """
    Load and play background music using pygame.

    Parameters:
        music_path (str): Path to the music file (e.g., "bgm.mp3", "sound.ogg").
        volume (float): Volume level from 0.0 to 1.0.
        loops (int): Number of times to loop the music. -1 means infinite loop.
        start (float): Start position in seconds.
    """
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loops=loops, start=start)
        print(f"Playing music: {music_path}")
    except pygame.error as e:
        print(f"Failed to play music: {e}")
