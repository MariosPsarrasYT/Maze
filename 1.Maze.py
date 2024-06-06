import time
import pygame

pygame.init()
screen = pygame.display.set_mode((1800,1000))
done = False

x = 950
y = 850
x2 = 750
y2 = 850

timer1 = time.time()
timer2 = time.time()
stopwatch2 = time.time()
stopwatch1 = time.time()
timer1Updated = 1000
timer2Updated = 0

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0))
    Font = pygame.font.SysFont("comicsansms", 70, True, False)
    Title = Font.render("Maze Mariolhs", True, (255,255,255))
    screen.blit(Title, (650,400))

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]: y = y - 10
    if pressed[pygame.K_DOWN]: y = y + 10
    if pressed[pygame.K_LEFT]: x = x - 10
    if pressed[pygame.K_RIGHT]: x = x + 10

    if pressed[pygame.K_w]: y2 = y2 - 10
    if pressed[pygame.K_s]: y2 = y2 + 10
    if pressed[pygame.K_a]: x2 = x2 - 10
    if pressed[pygame.K_d]: x2 = x2 + 10

    player = pygame.draw.rect(screen, (25, 207, 174), pygame.Rect(x, y, 30, 30))
    player2 = pygame.draw.rect(screen, (174, 207, 25), pygame.Rect(x2, y2, 30, 30))
    wall1 = pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,1800,50))
    wall2 = pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,50,1800))
    wall3 = pygame.draw.rect(screen, (255,255,255), pygame.Rect(1750,0,50,1800))
    wall4 = pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,950,1800,50))

    mazewall1 = pygame.draw.rect(screen, (255,0,0), pygame.Rect(250,50,50,650)) #kokkinos aristeros ka8etos
    mazewall2 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(1550, 50, 50, 750)) #kokkinos deksis ka8etos
    mazewall3 = pygame.draw.rect(screen, (0,0,255), pygame.Rect(500, 150, 900, 50)) #mple panw orizontios
    mazewall4 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(120, 750, 1580, 50)) #mple katw orizontios
    mazewall5 = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(120, 100, 50, 700)) #prasinos aristera
    mazewall6 = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(1650, 100, 50, 700)) #prasinos deksia

    final = pygame.draw.rect(screen, (191, 64, 191), pygame.Rect(900,95,30,30))

    if player.colliderect(wall1) or player.colliderect(wall2) or player.colliderect(wall3) or player.colliderect(wall4) or player.colliderect(mazewall1) or player.colliderect(mazewall2) or player.colliderect(mazewall3) or player.colliderect(mazewall4) or player.colliderect(mazewall5) or player.colliderect(mazewall6):
        if pressed[pygame.K_UP]: y = y + 10
        if pressed[pygame.K_DOWN]: y = y - 10
        if pressed[pygame.K_LEFT]: x = x + 10
        if pressed[pygame.K_RIGHT]: x = x - 10

    if player2.colliderect(wall1) or player2.colliderect(wall2) or player2.colliderect(wall3) or player2.colliderect(wall4) or player2.colliderect(mazewall1) or player2.colliderect(mazewall2) or player2.colliderect(mazewall3) or player2.colliderect(mazewall4) or player2.colliderect(mazewall5) or player2.colliderect(mazewall6):
        if pressed[pygame.K_w]: y2 = y2 + 10
        if pressed[pygame.K_s]: y2 = y2 - 10
        if pressed[pygame.K_a]: x2 = x2 + 10
        if pressed[pygame.K_d]: x2 = x2 - 10

    if player.colliderect(final):
        x = 950
        y = 850
        timer1 = time.time()
        timer1Updated = round(timer1 - stopwatch1,2)
        stopwatch1 = time.time()

    Font1 = pygame.font.SysFont("comicsansms", 20, True, False)
    Time1 = Font1.render("Time (Player ): " + str(timer1Updated), True, (255,255,255))
    screen.blit(Time1, (1400, 900))

    if player2.colliderect(final):
        x2 = 750
        y2 = 850
        timer2= time.time()
        timer2Updated = round(timer2 - stopwatch2,2)
        stopwatch2 = time.time()

    Font2 = pygame.font.SysFont("comicsansms", 20, True, False)
    Time2 = Font2.render("Time (Player 1): " + str(timer2Updated), True, (255,255,255))
    screen.blit(Time2, (50, 900))

    pygame.display.flip()
    clock.tick(60)


