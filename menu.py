def menu(*args):
    choice = input(f'Enter choice ({args}): ').strip()

    if choice in args:
        return choice
