save_len = len
save_eval = eval
save_print = print
save_input = input
Exception = Exception
str = str

globals()['__builtins__'].__dict__.clear()

while(True):
    input = save_input()
    if save_len(input) > 59 or '[' in input or ']' in input:
        save_print('[pas comme ça]')
    else:
        try:
            result = save_eval(input, {}, {})
            save_print(result)
        except Exception as e:
            save_print(f'[Erreur]: {str(e)}')
