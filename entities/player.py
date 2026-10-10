
@dataclass
class Jogador:
    id: int
    px: int
    py: int
    alive: bool = True
    speed: int = 2

    powerup_kick: bool = False
    bomb_radius: int = 2
    bomb_max: int = 1
    bomb_active: int = 0

    @property
    def grid_pos(self):
        return self.px // CELL_SIZE, self.py // CELL_SIZE


