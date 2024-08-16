import math, secrets


def calc_min_number_qubits(minimum: int, maximum: int) -> int:
    return math.ceil(math.log2(abs(maximum-minimum)+1))


def calc_width(n: int) -> int:
    return math.floor(math.log10(n)) + 1


def scramble_str(s: str) -> str:
    s_list = list(s)
    secrets.SystemRandom().shuffle(s_list)
    return ''.join(s_list)


if __name__ == '__main__':
    raise RuntimeError("Please use 'main.py' to run.")