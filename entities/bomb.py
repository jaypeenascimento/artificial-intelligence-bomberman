@dataclass
class Bomb:
    px: int
    py: int
    timer: int
    radius: int
    owner_id: int

    moving: bool = False
    speed_x: int = 0
    speed_y: int = 0

