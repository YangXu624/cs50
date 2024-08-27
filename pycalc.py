import math

angles = [8, 10, 12, 14]

for angle in angles:
    theta = float(angle * math.pi / 180)

    ux = 63 * math.cos(theta)
    uy = 63 * math.sin(theta)

    vx = ux
    vy = 4.9 * 9.81 - uy

    print(math.degrees(math.atan(vy / vx)))
