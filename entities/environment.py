import numpy as np
from dataclasses import dataclass

# Static Grid entities
VOID = 0
WALL = 1
BOX = 2
FIRE = 3
PLAYER = 4
BOMB = 5

CELL_SIZE = 16

@dataclass
class Environment:
    grid: np.ndarray
    players: dict[int, Player]
    bombs: list[Bomb]

    ## np.Copy eh mais rapido que o deepcopy do python.
    def clone(self):
        return Environment(
                grid=np.Copy(self.grid),
                players={k: Player(**v.__dict__) for k, v in self.players.items()},
                bombs=[Bomb(**b.__dict__) for b in self.bombs]
        )

    def update(self):
        self.update_bombs()

    def update_bombs(self):
        for b in self.bombs:
            b.update()

            if b.is_exploded():
                self.create_explosion(b)


    # Checa se uma entidade de hitbox (x,y) com centro em (px, py) 
    # colide com alguma entidade de tipo TYPE posicionada no grid.
    def collides_entity(self, entity_type):
        targets = []

        match entity_type:
            case BOMB:
                targets = self.bombs
            case PLAYER:
                targets = self.players
            # case WALL:
            # case BOX:
            # case FIRE:




    # Checa se uma entidade de hitbox (x,y) com centro em (px, py) 
    # colide com outra hitbox (x2, y2) e centro em (px2, py2).
    # TODO: mover para um lugar de helpers. Nao ha necessidade de ficar em Environment.
    def collides(x1,y1,px1,py1,x2,y2,px2,py2):
        deltaX = abs(px1 - px2);
        deltaY = abs(py1 - py2);

        hitboxSumX = x1 + x2
        hitboxSumY = y1 + y2

        return (deltaX < hitboxSumX) and (deltaY < hitboxSumY)

    # def create_explosion(b):



    



