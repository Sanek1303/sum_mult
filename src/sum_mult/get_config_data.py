

CONFIG_PATH = 'config.txt'

def get_number() -> int:
    with open(CONFIG_PATH, 'r') as f:
        x = int(f.readline())
    return x
