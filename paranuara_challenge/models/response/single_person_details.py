from dataclasses import dataclass
from typing import List


@dataclass
class SinglePersonDetails:
    username: str
    age: int
    fruits: List[str]
    vegetables: List[str]