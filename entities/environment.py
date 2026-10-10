# import numpy as np

VOID = 0
WALL = 1
BOX = 2
FIRE = 3
CELL_SIZE = 16

@dataclass
class Environment:
    grid: np.ndarray
    players: dict[int, Player]
    bombs: list[Bomb]

    ## np.Copy eh mais rapido que o deepcopy do python.
    def clone(self):
        return Environment(
                grid=np.Copy(self.grid)
                players={k: Player(**v.__dict__) for k, v in self.players.items()}
                bombs=[Bomb(**b.__dict__) for b in self.bombs]
        )


