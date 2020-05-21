import random


class Blob:

    def __init__(self, color, w, h, size_range=(5, 11), move_range=(-1, 2)):
        self.color = color
        self.x = random.randrange(0, w)
        self.y = random.randrange(0, h)
        self.size = random.randint(size_range[0], size_range[1])
        self.x_boundary = w
        self.y_boundary = h
        self.move_range = move_range

    def move(self):
        self.move_x = random.randrange(self.move_range[0], self.move_range[1])
        self.move_y = random.randrange(self.move_range[0], self.move_range[1])
        self.x += self.move_x
        self.y += self.move_y
        self.check_bounds()

    def check_bounds(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.x_boundary:
            self.x = self.x_boundary

        if self.y < 0:
            self.y = 0
        elif self.y > self.y_boundary:
            self.y = self.y_boundary