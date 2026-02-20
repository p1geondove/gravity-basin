import pygame
from pygame import Vector2

WIDTH, HEIGHT = 500,500
BACKGROUND_COLOR = pygame.Color("grey15")
GRAV_CONST = 100
MAX_FORCE = .1
RESISTANCE = .999
GRID_SIZE = 5
COLORS = ["red","blue","yellow"]

def main():
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.Clock()
    draw_particles = True

    attactors = [Vector2(125,0).rotate(x*120)+Vector2(WIDTH,HEIGHT)/2 for x in range(3)]
    paritcles_pos = []
    paritcles_vel = []
    start_rect = []
    for y in range(0,HEIGHT,GRID_SIZE):
        for x in range(0,WIDTH,GRID_SIZE):
            paritcles_pos.append(Vector2(x,y))
            paritcles_vel.append(Vector2())
            start_rect.append(pygame.Rect(x,y,GRID_SIZE,GRID_SIZE))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit(0)
                elif event.key == pygame.K_h:
                    draw_particles = not draw_particles

        # update
        for _ in range(10):
            for p_pos, p_vel in zip(paritcles_pos, paritcles_vel):
                acc = Vector2()
                for a in attactors:
                    dist = p_pos.distance_squared_to(a)
                    if dist < 0.1:
                        force = 0
                    else:
                        force = min(MAX_FORCE,GRAV_CONST/dist)
                        acc += (a-p_pos).normalize() * force
                p_vel += acc
                p_pos += p_vel
                p_vel *= RESISTANCE

        # draw
        window.fill(BACKGROUND_COLOR)

        for attr in attactors:
            pygame.draw.aacircle(window,"white",attr,3)
        for p,s in zip(paritcles_pos,start_rect):
            i,_ = min([(i,a.distance_squared_to(p)) for i,a in enumerate(attactors)],key=lambda x:x[1])
            color = COLORS[i]
            pygame.draw.rect(window,color,s)
            if draw_particles:
                pygame.draw.aacircle(window,"red",p,1)
        pygame.display.flip()
        clock.tick(72)

if __name__ == "__main__":
    main()
