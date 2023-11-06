class Map:
    bg = None  # изображение заднего фона
    X = None  # расположение заднего фона ппо x и Y
    Y = None
    speed = 10


bgsp = Map()


bg_1 = Map()
bg_1.bg = "images/background.jpg"  # Сохдаём первую карту
bg_1.X = 0
bg_1.Y = 0

bg_2 = Map()
bg_2.bg = "images/background.jpg"  # Сохдаём первую карту
bg_2.X = 1003
bg_2.Y = 0

bg_3 = Map()
bg_3.bg = "images/background.jpg"  # Сохдаём первую карту
bg_3.X = 0
bg_3.Y = -1000

bg_4 = Map()
bg_4.bg = "images/background.jpg"  # Сохдаём первую карту
bg_4.X = 1003
bg_4.Y = -1000


class Obstacle:
    view = None
    X = None
    Y = None


obs1 = Obstacle()
obs1.view = "images/препятствие.png"
obs1.X = 250
obs1.Y = -250
