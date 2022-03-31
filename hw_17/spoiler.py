

class SpoilerMixin:

    def acceleration(self) -> None:
        if self.speed >= 90:
            self.speed += 10
        else:
            self.speed += 5
