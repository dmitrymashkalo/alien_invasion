import pygame.font


class Button:
    """ Implement a button """

    def __init__(self, ai_game, msg):
        """ Init the attributes of the button """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Button sizes and properties
        self.width, self.heigth = 250, 80
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Align the button in the center of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.heigth)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """ Converts message to an image """
        # Render into an image
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # Align the image in the center of the screen
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """ Draw button and text """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
