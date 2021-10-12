import pygame
import math

RED = [255, 50, 20]
GREEN = [40, 255, 60]
BLUE = pygame.Color('blue')
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

dead_zone = 10

class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def indentY(self):
        self.y += 10

    def unindent(self):
        self.x -= 10

pygame.init()
pygame.joystick.init()

textPrint = TextPrint()

screen = pygame.display.set_mode([420, 200])

print(pygame.joystick.get_count(), "controler connected")

joystick = pygame.joystick.Joystick(0)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    axisX1 = joystick.get_axis(0)
    axisY1 = joystick.get_axis(1)
    axisX1 = axisX1 * 25
    axisY1 = axisY1 * 25

    axisX2 = joystick.get_axis(2)
    axisY2 = joystick.get_axis(3)
    axisX2 = axisX2 * 25
    axisY2 = axisY2 * 25

    axisT1 = joystick.get_axis(4)
    axisT2 = joystick.get_axis(5)
    axisT1 = axisT1 * 100
    axisT2 = axisT2 * 100

    dist1 = math.sqrt((axisX1 * axisX1) + (axisY1 * axisY1))
    dist2 = math.sqrt((axisX2 * axisX2) + (axisY2 * axisY2))

    button1 = joystick.get_button(7)
    button2 = joystick.get_button(8)

    if (button1 == True):
        color1 = BLUE     
    elif (dist1 < dead_zone):
        color1 = RED
    else:
        color1 = GREEN

    if (button2 == True):
        color2 = BLUE     
    elif (dist2 < dead_zone):
        color2 = RED
    else:
        color2 = GREEN
        
    screen.fill([255, 255, 255])

    pygame.draw.circle(screen, [160, 160, 160], [170, 40], dead_zone)
    pygame.draw.circle(screen, color1, [axisX1 + 170, axisY1 + 40], 5)
    pygame.draw.rect(screen , BLACK, (140, 10, 60, 60), width = 2)

    pygame.draw.circle(screen, [160, 160, 160], [380, 40], dead_zone)
    pygame.draw.circle(screen, color2, [axisX2 + 380, axisY2 + 40], 5)
    pygame.draw.rect(screen , BLACK, (350, 10, 60, 60), width = 2)

    pygame.draw.rect(screen , RED, (30, 100, axisT1, 20))
    pygame.draw.rect(screen , BLACK, (30, 100, 100, 20), width = 2)

    pygame.draw.rect(screen , RED, (30, 140, axisT2, 20))
    pygame.draw.rect(screen , BLACK, (30, 140, 100, 20), width = 2)

    textPrint.reset()
    textPrint.tprint(screen, "Axis x value: {:>6.3f}".format(axisX1 / 25))
    textPrint.tprint(screen, "Axis y value: {:>6.3f}".format(axisY1 / 25))
    textPrint.tprint(screen, "L. Stick In value: {}".format(button1))
    textPrint.tprint(screen, "Dead zone size: {}".format(dead_zone))
    textPrint.reset()
    textPrint.tprint(screen, "                                                     Axis x value: {:>6.3f}".format(axisX2 / 25))
    textPrint.tprint(screen, "                                                     Axis y value: {:>6.3f}".format(axisY2 / 25))
    textPrint.tprint(screen, "                                                     R. Stick In value: {}".format(button2))
    textPrint.tprint(screen, "                                                     Dead zone size: {}".format(dead_zone))
    textPrint.indentY()
    textPrint.tprint(screen, "Axis LT value: {:>6.3f}".format(axisT1 / 100))
    textPrint.indentY()
    textPrint.indentY()
    textPrint.indentY()
    textPrint.tprint(screen, "Axis RT value: {:>6.3f}".format(axisT2 / 100))

    pygame.display.flip()

pygame.joystick.quit()
pygame.quit()