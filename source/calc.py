def calc_width(n: int) -> int:
    import math
    return math.floor(math.log10(n-1)) + 1


def scramble_str(s: str) -> str:
    import secrets
    s_list = list(s)
    secrets.SystemRandom().shuffle(s_list)
    return ''.join(s_list)


if __name__ == '__main__':
    raise RuntimeError("Please use 'main.py' to run.")