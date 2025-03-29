import math
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        self.x /= mag
        self.y /= mag

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def multiply(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

"""# 假设我们有物体从点A(x1, y1)移动到点B(x2, y2)，并且知道移动时间t
dx = self.x - self.x
dy = y - y
distance = math.sqrt(dx**2 + dy**2)
speed = distance / t

# 计算速度向量的方向（以弧度为单位）
theta = math.atan2(dy, dx)

# 创建速度向量
speed_vector = Vector2D(speed * math.cos(theta), speed * math.sin(theta))


# 示例使用
vec1 = Vector2D(3, 4)
vec2 = Vector2D(-2, 1)

print(vec1)  # 输出: Vector2D(3, 4)
print(vec1.magnitude())  # 输出: 5.0
vec1.normalize()
print(vec1)  # 输出: Vector2D(0.6, 0.8)

vec3 = vec1.add(vec2)
print(vec3)  # 输出: Vector2D(1, 5)

vec4 = vec1.subtract(vec2)
print(vec4)  # 输出: Vector2D(5, -3)

vec5 = vec1.multiply(2)
print(vec5)  # 输出: Vector2D(6, 8)

dot_product = vec1.dot(vec2)
print(dot_product)  # 输出: -5.0"""