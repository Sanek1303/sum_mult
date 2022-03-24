from Typing import Tuple
from sum_mult.sum.sum_config import sum_config
from sum_mult.mult.mult_config import mult_config

def sum_mult_config(x: int) -> Tuple[int, int]:
    summ = sum_config(x)
    mult = mult_config(x)
    return summ, mult
