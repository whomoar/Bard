class Entity:

        #A generic object to represent players

        # Ist init eine spezial function??
        def __init__(self, x, y, char, color):
            self.x = x
            self.y = y
            self.char = char
            self.color = color

        def move(self, dx, dy):
            # Move the enity by a given amount
            self.x += dx
            self.y += dy
