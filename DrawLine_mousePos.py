import pygame


pygame.init()

screen = pygame.display.set_mode((600, 700))

pygame.display.set_caption("Hiirulainen")
screen.fill((255, 255, 255))


def drawLine(x1, y1, x2, y2):
    pygame.draw.line(screen, (0, 255, 0), (x1, y1), (x2, y2))


loop = True

image = pygame.image.load('C:\\Users\\srpropro\\Desktop\\pytis\\maisema.jpg')
screen.blit(image, (100, 100))
pygame.display.update()

while loop:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            # get mouse position, pos[0]=x and pos[1]=y
            pos = pygame.mouse.get_pos()
            print('Mouse pressed at {} {}'.format(pos[0], pos[1]))
            x1 = pos[0]
            y1 = pos[1]
        if event.type == pygame.MOUSEBUTTONUP:
            # get mouse position
            pos = pygame.mouse.get_pos()
            print('Mouse released at {} {}'.format(pos[0], pos[1]))
            x2 = pos[0]
            y2 = pos[1]
            pygame.draw.line(screen, (0, 255, 0), (x1, y1), (x2, y2))
        
        pygame.display.update()
        if event.type == pygame.QUIT:
            loop = False

pygame.quit()
