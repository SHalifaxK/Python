import pygame

############################################
#           Creating sprite                #
############################################


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        # adding all the images to sprite array
        self.images = []
        self.images.append(pygame.image.load('C:\\Users\\srpropro\\Desktop\\pytis\\images\\walk1.png'))
        self.images.append(pygame.image.load('C:\\Users\\srpropro\\Desktop\\pytis\\images\\walk2.png'))
        self.images.append(pygame.image.load('C:\\Users\\srpropro\\Desktop\\pytis\\images\\walk3.png'))
        self.images.append(pygame.image.load('C:\\Users\\srpropro\\Desktop\\pytis\\images\\walk4.png'))
        self.images.append(pygame.image.load('C:\\Users\\srpropro\\Desktop\\pytis\\images\\walk5.png'))
        self.images.append(pygame.image.load('C:\\Users\\srpropro\\Desktop\\pytis\\images\\walk6.png'))
        self.images.append(pygame.image.load('C:\\Users\\srpropro\\Desktop\\pytis\\images\\walk7.png'))
        self.images.append(pygame.image.load('C:\\Users\\srpropro\\Desktop\\pytis\\images\\walk8.png'))
        self.images.append(pygame.image.load('C:\\Users\\srpropro\\Desktop\\pytis\\images\\walk9.png'))
        self.images.append(pygame.image.load('C:\\Users\\srpropro\\Desktop\\pytis\\images\\walk10.png'))

        # index value to get the image from the array
        # initially it is 0
        self.index = 0

        # now the image that we will display will be the index from the image array
        self.image = self.images[self.index]

        # creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite
        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        # when the update method is called, we will increment the index
        self.index += 1

        # if the index is larger than the total images
        if self.index >= len(self.images):
            # we will make the index to 0 again
            self.index = 0

        # finally we will update the image that will be displayed
        self.image = self.images[self.index]


def main():
    pygame.init()
    FPS = 10

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # Set the width and height of the screen [width, height] and the bg_color
    size = (700, 500)
    screen = pygame.display.set_mode(size)

    # set window title
    pygame.display.set_caption("My Game")

    my_sprite = MySprite()

    my_group = pygame.sprite.Group(my_sprite)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        my_group.update()
        screen.fill(WHITE)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()
