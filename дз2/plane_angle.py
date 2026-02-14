# import math

# class Point:
#     def __init__(self, x, y, z):
#         # your code here        
        
#     def __sub__(self, no):
#         # your code here        
        
#     def dot(self, no):
#         # your code here        
        
#     def cross(self, no):
#         # your code here        
        
#     def absolute(self):
#         return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

# def plane_angle(a, b, c, d):
#     # your code here

# if __name__ == '__main__':
#     # your code here

import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __sub__(self, no):
        return Point(self.x - no.x, self.y - no.y, self.z - no.z)
        
    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z
        
    def cross(self, no):
        # векторное произведение: i(j*k' - k*j') - j(i*k' - k*i') + k(i*j' - j*i')
        return Point(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )
        
    def absolute(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

def plane_angle(a, b, c, d):
    # AB = B - A
    # BC = B - C
    # CD = C - D
    ab = b - a
    bc = b - c
    cd = c - d
    
    # X = AB × BC
    x = ab.cross(bc)
    # Y = BC × CD
    y = bc.cross(cd)
    
    # скалярное произведение и длины
    dot_xy = x.dot(y)
    mag_x = x.absolute()
    mag_y = y.absolute()
    
    # защита от деления на ноль
    if mag_x == 0 or mag_y == 0:
        return 0.0
    
    # cos(phi) = (X·Y) / (|X||Y|)
    cos_phi = dot_xy / (mag_x * mag_y)
    
    # ограничиваем, чтобы избежать ошибок округления
    cos_phi = max(-1.0, min(1.0, cos_phi))
    
    # угол в радианах переводи в градусы
    phi_rad = math.acos(cos_phi)
    phi_deg = math.degrees(phi_rad)
    
    return f"{phi_deg:.2f}"

if __name__ == '__main__':
    points = []
    for _ in range(4):
        x, y, z = map(float, input().split())
        points.append(Point(x, y, z))
    
    a, b, c, d = points
    angle = plane_angle(a, b, c, d)
    print(angle)