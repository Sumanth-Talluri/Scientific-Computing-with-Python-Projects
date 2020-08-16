class Rectangle:

    width = 0
    height = 0

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*(self.width+self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        res = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range(0, self.height):
                for j in range(0, self.width):
                    res += "*"
                res += "\n"
            return res

    def get_amount_inside(self, shape):
        count = 0
        if shape.width > self.width or shape.height > self.height:
            return count
        else:
            each_row = self.width//shape.width
            no_row = self.height//shape.height
            count = each_row*no_row
            return count

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, s):
        Rectangle.width = s
        Rectangle.height = s

    def set_side(self, s):
        Rectangle.width = s
        Rectangle.height = s

    def set_width(self, s):
        Rectangle.width = s

    def set_height(self, s):
        Rectangle.height = s

    def __str__(self):
        return f"Square(side={Rectangle.width})"
