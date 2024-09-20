class Rhombus:
    def __init__(self, side_a, angle_a):
        self.set_side_a(side_a)
        self.set_angle_a(angle_a)

    def set_side_a(self, side_a):
        if side_a > 0:
            setattr(self, 'side_a', side_a)
        else:
            raise ValueError("Довжина сторони повинна бути більше 0")

    def set_angle_a(self, angle_a):
        if 0 < angle_a < 180:
            setattr(self, 'angle_a', angle_a)
            setattr(self, 'angle_b', 180 - angle_a)  # Протилежний кут
        else:
            raise ValueError("Кут повинен бути в межах від 0 до 180 градусів")

    def get_info(self):
        return f"Сторона: {self.side_a}, Кут між сторонами a і b: {self.angle_a}°, Протилежний кут: {self.angle_b}°"


rhombus = Rhombus(5, 60)


print(rhombus.get_info())

