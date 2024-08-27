import math

angles = [8, 10, 12, 14, 40.79]

for angle in angles:
    theta = math.radians(angle)

    ux = 63 * math.cos(theta)
    uy = 63 * math.sin(theta)

    vx = ux
    vy = 4.9 * 9.81 - uy

    print(math.degrees(math.atan(vy / vx)))
