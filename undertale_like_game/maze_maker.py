import pygame
import sys
import random

CYAN = (0, 255, 255)
GRAY = (96, 96, 96)

MAZE_W = 11
MAZE_H = 9
maze = []

for y in range(MAZE_H):
  maze.append([0]*MAZE_W)

def make_maze():
  XP = [0, 1, 0, -1]
  YP = [-1, 0, 1, 0]

  #edge
  for x in range(MAZE_W):
    maze[0][x] = 1
    maze[MAZE_H-1][x] = 1

  for y in range(1, MAZE_H-1):
    maze[y][0] = 1
    maze[y][MAZE_W-1] = 1
  
  #space
  for y in range(1, MAZE_H-1):
    for x in range(1, MAZE_W-1):
      maze[y][x] = 0
  
  #pullar
  for y in range(2, MAZE_H-2, 2):
    for x in range(2, MAZE_W-2, 2):
      maze[y][x] = 1

  #wall around the pullar
  for y in range(2, MAZE_H-2, 2):
    for x in range(2, MAZE_W-2, 2):
      d = random.randint(0, 3)
      if x > 2:
        d = random.randint(0, 2)
      maze[y+YP[d]][x+XP[d]] = 1

def main():
  pygame.init()
  pygame.display.set_caption('Maze')
  screen = pygame.display.set_mode((528, 432))
  clock = pygame.time.Clock()

  make_maze()

  while True:
    for event in pygame.event.get():
      if event == pygame.QUIT:
        pygame.quit()
        sys.exit()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          make_maze()

    for y in range(MAZE_H):
      for x in range(MAZE_W):
        W = 48
        H = 48
        X = x*W
        Y = y*H
        if maze[y][x] == 0:
          pygame.draw.rect(screen, CYAN, [X, Y, W, H])
        if maze[y][x] == 1:
          pygame.draw.rect(screen, GRAY, [X, Y, W, H])
    pygame.display.update()
    clock.tick(2)

if __name__ == '__main__':
  main()