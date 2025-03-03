from pwn import xor

# matrix 4x4 du bloc de message
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

# la clé de round correspondant
# e.g: key[1] => round 1; key[2] => round 2; key[3] => round 3; ...
round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(state, round_key):
    result = xor(state, round_key)
    return result


print(add_round_key(state, round_key))

