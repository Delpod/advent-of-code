# Setup
import re
import math
from PIL import Image

file = open('adv14.txt', 'r')
lines = file.read().splitlines()

width, height = 101, 103
def calculate_robots(seconds = 100):
    q1, q2, q3, q4 = 0, 0, 0, 0
    matrix = []

    for i in range(height):
        matrix.append([])
        for j in range(width):
            matrix[-1].append(' ')

    for i, line in enumerate(lines):
        px, py, vx, vy = [int(n) for n in re.findall(r'-?\d+', line)]

        x = (px + seconds * vx) % width
        y = (py + seconds * vy) % height

        if matrix[y][x] == ' ':
            matrix[y][x] = 'X'

        if x < math.floor(width / 2):
            if y < math.floor(height / 2):
                q1 += 1
            elif y >= math.ceil(height / 2):
                q3 += 1
        elif x >= math.ceil(width / 2):
            if y < math.floor(height / 2):
                q2 += 1
            elif y >= math.ceil(height / 2):
                q4 += 1

    im= Image.new('RGB', (width, height), 'black')
    pixels = im.load()
    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            if char != ' ':
                pixels[j,i] = (255,255, 255)

    im.save(f'.\\adv14\\image{seconds}.png')

    return q1 * q2 * q3 * q4

print(f"Part 1: {calculate_robots(100)}")

# Part 2 - i manually checked images then
for i in range(10000):
    calculate_robots(i)
