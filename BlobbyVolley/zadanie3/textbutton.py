import pygame

'''
    Uzupełnij klasę TextButton
    Napis powinien być pozycjonowany na ekranie względem środkowych współrzędnych napisu
    Przydatne funkcje:
        mpx, mpy = pygame.mouse.get_post() # zwraca współrzędne kursora myszy
        text.get_rect() # zwraca prostokąt otaczający wyrenderowany text
'''


def check_text_rect_hover(text_rect):
    mpx, mpy = pygame.mouse.get_pos()
    if text_rect.left < mpx < text_rect.right and text_rect.top < mpy < text_rect.bottom:
        return True
    else:
        return False


class TextButton:
    def __init__(self, center_x, center_y, font_name, font_size, text, color):
        self.center_x = center_x
        self.center_y = center_y
        self.font = pygame.font.SysFont(font_name, font_size)
        self.text = self.font.render(text, True, color)
        self.text_rect = self.text.get_rect()

    def cursor_hover(self):
        return check_text_rect_hover(self.text_rect)

    def update(self, text, color):
        self.text = self.font.render(text, True, color)
        self.text_rect = self.text.get_rect()

    def draw(self,win):
        self.text_rect.center = (self.center_x, self.center_y)
        win.blit(self.text, self.text_rect)
