import sys, pygame

pygame.init()

pygame.font.init()
myFont = pygame.font.SysFont("Comic Sans MS", 30)

size = width, height = 320, 240
black = 0, 0, 0
screen = pygame.display.set_mode(size)

star1 = pygame.image.load("star1.png")
star1rect =star1.get_rect()

speed = [1, 1]

star2 = pygame.image.load("star2.png")
star2rect = star2.get_rect()

star2rect.x = 40
star2rect.y = 200
speed2 = [1, 1]

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif pygame.key.get_pressed()[pygame.K_1]:
            print("1 pressed")
        elif pygame.key.get_pressed()[pygame.K_UP]:
            print("Up Arrow Pressed")
            speed = [speed[0] + 1, speed[1] + 1]
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            print("Down Arrow Pressed")
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            print("Left Arrow Pressed")
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            print("Right Arrow Pressed")
        elif pygame.key.get_pressed()[pygame.K_m]:
            print("OMG You pressed the m key")

    star1rect = star1rect.move(speed)
    star2rect = star2rect.move(speed2)

    print("({0}, {1})".format(star1rect.x, star1rect.y))

    if star1rect.left < 0 or star1rect.right > width:
        speed[0] = -speed[0]
    if star2rect.left < 0 or star2rect.right > width:
        speed2[0] = -speed2[0]
    if star1rect.top < 0 or star1rect.bottom > height:
        speed[1] = -speed[1]
    if star2rect.top < 0 or star2rect.bottom > height:
        speed2[1] = -speed2[1]

    screen.fill(black)

    ren = False
    if star1rect.colliderect(star2rect):
        speed[0] = -speed[0]
        speed[1] = -speed[1]
        speed2[0] = -speed2[0]
        speed2[1] = -speed2[1]

        text = myFont.render("Blam!", False, (255, 0, 0))
        ren = True

    pygame.time.delay(30)

    screen.blit(star1, star1rect)
    screen.blit(star2, star2rect)
    if ren:
        screen.blit(text, (0, 0))

    pygame.display.flip()