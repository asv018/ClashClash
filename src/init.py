def printTitleScreen():
    print(r'''
                          _______  _        _______  _______                   _______  _______        _______  _        _______  _        _______
                          (  ____ \( \      (  ___  )(  ____ \|\     /|        (  ___  )(  ____ \      (  ____ \( \      (  ___  )( (    /|(  ____ \
                          | (    \/| (      | (   ) || (    \/| )   ( |        | (   ) || (    \/      | (    \/| (      | (   ) ||  \  ( || (    \/
                          | |      | |      | (___) || (_____ | (___) |        | |   | || (__          | |      | |      | (___) ||   \ | || (_____
                          | |      | |      |  ___  |(_____  )|  ___  |        | |   | ||  __)         | |      | |      |  ___  || (\ \) |(_____  )
                          | |      | |      | (   ) |      ) || (   ) |        | |   | || (            | |      | |      | (   ) || | \   |      ) |
                          | (____/\| (____/\| )   ( |/\____) || )   ( |        | (___) || )            | (____/\| (____/\| )   ( || )  \  |/\____) |
                          (_______/(_______/|/     \|\_______)|/     \|        (_______)|/             (_______/(_______/|/     \||/    )_)\_______)'''
) # NOQA


def initializeLayout(gameHeight, gameWidth):
    layout = []
    for i in range(gameHeight):
        layout.append([' '] * gameWidth)
    for i in range(gameHeight):
        layout[i][gameWidth - 1] = '#'
        layout[i][0] = '#'
    for j in range(gameWidth):
        if j % 2 == 0:
            layout[0][j] = '#'
            layout[gameHeight - 1][j] = '#'
    layout[0][gameWidth - 1] = layout[gameHeight - 1][gameWidth - 1] = ' '
    return layout
