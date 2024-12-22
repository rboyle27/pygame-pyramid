import pygame
import numpy as np

FPS = 60

WIDTH = 800
HEIGHT = 800

SCALE = 100
OFFSET = WIDTH // 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def init():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    return window, clock

PROJECTION_MATRIX = np.array([[1, 0, 0],
                              [0, 1, 0],
                              [0, 0, 0]])

pyramid_points = [np.array([[-1], [-1], [-1]]),
                  np.array([[ 1], [-1], [-1]]),
                  np.array([[ 1], [ 1], [-1]]),
                  np.array([[-1], [ 1], [-1]]),
                  np.array([[ 0], [ 0], [ 1]])]

transform = lambda a: a * SCALE + OFFSET

def project(point: np.ndarray):
    projection = PROJECTION_MATRIX.dot(point)
    x, y = (transform(projection[0][0]), 
            transform(projection[1][0]))
    return x, y

def connect(window: pygame.Surface, i: int, j: int, points: list):
    start = (points[i][0], points[i][1]) # Get projected position of point i
    end = (points[j][0], points[j][1]) # Get projected position of point j
    pygame.draw.line(window, WHITE, start, end)

def rotate(point: np.ndarray, x: float = 0, y: float = 0, z: float = 0):
    rotation_x = np.array([[1, 0, 0],
                           [0, np.cos(x), -np.sin(x)],
                           [0, np.sin(x), np.cos(x)]])
    rotation_y = np.array([[np.cos(y), 0, np.sin(y)],
                           [0, 1, 0],
                           [-np.sin(y), 0, np.cos(y)]])
    rotation_z = np.array([[np.cos(z), -np.sin(z), 0],
                           [np.sin(z), np.cos(z), 0],
                           [0, 0, 1]])
    rotate_x = rotation_x.dot(point)
    rotate_y = rotation_y.dot(rotate_x)
    rotate_z = rotation_z.dot(rotate_y)
    return rotate_z

def main():
    pygame.init()
    window, clock = init()
    angle_x = angle_y = angle_z = 0

    while True:
        clock.tick(FPS)
        window.fill(BLACK)

        points = [0 for e in pyramid_points]
        i = 0

        for point in pyramid_points:
            rotated = rotate(point, angle_x, angle_y, angle_z)
            x, y = project(rotated)

            points[i] = (x, y)
            i += 1

            pygame.draw.circle(window, RED, (x, y), 5)
        
        edges = [(0, 1), (0, 3), 
                (0, 4), (1, 2), 
                (1, 4), (2, 3), 
                (2, 4), (3, 4)]
        
        for edge in edges:
            connect(window, edge[0], edge[1], points)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            angle_x += 0.1
        if keys[pygame.K_a]:
            angle_y -= 0.1
        if keys[pygame.K_s]:
            angle_x -= 0.1
        if keys[pygame.K_d]:
            angle_y += 0.1

        pygame.display.update()

if __name__ == '__main__':
    main()
