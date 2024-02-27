import pygame
import random
from constants import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def drawScreen(positions):
    screen.fill(GREY)
    drawGrid(positions)
    pygame.display.update()


def gen(nums):
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for _ in range(nums)])


def drawGrid(positions):
    for position in positions:
        col, row = position
        topLeft = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*topLeft, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE),
                         (WIDTH, row*TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0),
                         (col*TILE_SIZE, HEIGHT))


def adjustGrid(positions):
    allNeighbors = set()
    newPositions = set()

    for position in positions:
        neighbors = getNeighbors(position)
        allNeighbors.update(neighbors)

        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) in [2, 3]:
            newPositions.add(position)

    for position in allNeighbors:
        neighbors = getNeighbors(position)
        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) == 3:
            newPositions.add(position)

    return newPositions


def getNeighbors(position):
    x, y = position
    neighbors = []

    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx > GRID_WIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > GRID_WIDTH:
                continue
            if dx == 0 and dy == 0:
                continue

            neighbors.append((x + dx, y + dy))
    return neighbors


def checkEvents(running, playing, positions, count):
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False

            case pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                position = (col, row)

                if position in positions:
                    positions.remove(position)
                else:
                    positions.add(position)

            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_SPACE:
                        playing = not playing

                    case pygame.K_c:
                        positions = set()
                        playing = False
                        count = 0

                    case pygame.K_g:
                        positions = gen(random.randrange(4, 10) * GRID_WIDTH)

                    case pygame.K_q:
                        pygame.quit()

    return running, playing, positions, count


def eventLoop(running, playing, count, updateFreq, positions):
    while running:
        clock.tick(FPS)

        if playing:
            count += 1

        if count >= updateFreq:
            count = 0
            positions = adjustGrid(positions)

        pygame.display.set_caption("Playing" if playing else "Paused")

        running, playing, positions, count = checkEvents(
            running, playing, positions, count)

        drawScreen(positions)
    return


def game():
    eventLoop(running=True, playing=False, count=0,
              updateFreq=60, positions=set())

    pygame.quit()

    return
