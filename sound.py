import numpy
import pygame

pygame.mixer.init(frequency=4096, size=8, channels=1)
make_sound = pygame.sndarray.make_sound

pygame.display.set_mode((200,200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print event.key
            make_sound(
                numpy.array(
                    list(
                        (numpy.sin(numpy.arange(0,numpy.pi*2,0.05 * event.key)) + 3
                    ) * 128) * 60, numpy.uint8
                )
            ).play()
        if event.type == pygame.QUIT:
            sys.exit()
