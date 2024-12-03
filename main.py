import pygame, random, asyncio

pygame.init()
screen_size = [270, 400]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()
score = 0


def display_score(scr):
    font = pygame.font.SysFont("Ariel", 50)
    font_text = "score " + str(scr)
    font_img = font.render(font_text, True, (60, 98, 255))
    screen.blit(font_img, [20, 15])


bg = pygame.image.load('bg.png')
dab = pygame.image.load('dab.png')
panda = pygame.image.load('pand.png')


def random_offset():
    return -1 * random.randint(50, 1400)


def update_dab_pos(idx):
    global score
    if dab_y[idx] > 400:
        dab_y[idx] = random_offset()
        score += 15
    else:
        dab_y[idx] += 5


keep_alive = True


def crashed(idx):
    global score
    global keep_alive
    score -= 60
    dab_y[idx] = random_offset()
    if score < -150:
        keep_alive = False



dab_y = [random_offset(), random_offset(), random_offset()]
user_x = 110
clock = pygame.time.Clock()


async def main():
    while keep_alive:
        global user_x
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and user_x < 220:
            user_x += 10
        elif keys[pygame.K_LEFT] and user_x > 0:
            user_x -= 10

        update_dab_pos(0)
        update_dab_pos(1)
        update_dab_pos(2)

        if dab_y[0] > 290 and user_x < 70:
            crashed(0)
        if dab_y[1] > 290 and 50 < user_x < 160:
            crashed(1)
        if dab_y[2] > 290 and user_x > 200:
            crashed(2)

        screen.blit(bg, [0, 0])
        screen.blit(dab, [20, dab_y[0]])
        screen.blit(dab, [110, dab_y[1]])
        screen.blit(dab,  [200, dab_y[2]])
        screen.blit(panda, [user_x, 340])

        display_score(score)
        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)


asyncio.run(main())
