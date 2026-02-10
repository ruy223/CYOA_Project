
# Used to make my text all uniform
def print_wrapped(text, width=100):
    words = text.split()
    line = []
    for word in words:
        if len(' '.join(line + [word])) > width:
            print(' '.join(line))
            line = [word]
        else:
            line.append(word)
    if line:
        print(' '.join(line))