from dataclasses import dataclass

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

    def update(self):
        self.timer =- 1;
    
    def is_exploded(self):
        return self.timer <= 0;
