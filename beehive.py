from dataclasses import dataclass, field

@dataclass
class Beehive:
    """A beehive has a position in 3d space. That's it!"""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = field(init=False)

    def __post_init__(self):
        self.volume = self.capacity
