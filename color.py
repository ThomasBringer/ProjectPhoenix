class Color:

    def __init__(self, r=0, g=0, b=0, a=1):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __add__(c, d): return Color(c.r + d.r, c.g + d.g, c.b + d.b, c.a + d.a)

    def __mul__(c, d): return Color(c.r * d.r, c.g * d.g, c.b * d.b, c.a * d.a)
    def __truediv__(c, d): return Color(
        c.r / d.r, c.g / d.g, c.b / d.b, c.a / d.a)

    def __mul__(c, d: float): return Color(c.r * d, c.g * d, c.b * d, c.a)
    def __truediv__(c, d: float): return Color(c.r / d, c.g / d, c.b / d, c.a)

    def normalized(c):
        return c / 255

    def to255(c):
        return c * 255

    def toTuple(c, alpha=True):
        return (c.r, c.g, c.b) + ((c.a,)if alpha else ())

    def __str__(self):
        return "Color(Red=" + str(self.r) + ", Green=" + str(self.g) + ", Blue=" + str(self.b) + ", Transparency=" + str(self.a) + ")"


Color.white = Color(255, 255, 255, 1)
Color.grey = Color(128, 128, 128, 1)
Color.black = Color(0, 0, 0, 1)
Color.red = Color(255, 0, 0, 1)
Color.green = Color(0, 255, 0, 1)
Color.blue = Color(0, 0, 255, 1)
Color.cyan = Color(0, 255, 255, 1)
Color.magenta = Color(255, 0, 255, 1)
Color.yellow = Color(255, 255, 0, 1)
Color.orange = Color(255, 128, 0, 1)
