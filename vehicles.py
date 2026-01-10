class TransportnyiZasib:
    def __init__(self, shvydkist):
        self.shvydkist = shvydkist

    def peremishchennia(self):
        print("Транспортний засіб рухається зі швидкістю", self.shvydkist, "км/год")

class Avtomobil(TransportnyiZasib):
    def peremishchennia(self):
        print("Автомобіль їде зі швидкістю", self.shvydkist, "км/год")

class Velosyped(TransportnyiZasib):
    def peremishchennia(self):
        print("Велосипед їде зі швидкістю", self.shvydkist, "км/год")

class Litak(TransportnyiZasib):
    def peremishchennia(self):
        print("Літак летить зі швидкістю", self.shvydkist, "км/год")

auto = Avtomobil(80)
velo = Velosyped(25)
plane = Litak(900)

auto.peremishchennia()
velo.peremishchennia()
plane.peremishchennia()
