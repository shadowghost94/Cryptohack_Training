def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

#def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    #????

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]
text = "The nôrth remember"
print(bytes2matrix(text))
#print(matrix2bytes(matrix))
