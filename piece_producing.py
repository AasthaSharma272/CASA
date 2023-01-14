import os
import random

anger = [[], [[], []], [[], []]]
calm = [[], [[], []], [[], []]]
fear = [[], [[], []], [[], []]]
joy = [[], [[], []], [[], []]]
nostalgia = [[], [[], []], [[], []]]
sad = [[], [[], []], [[], []]]

directory1 = '/home/runner/NewHacksforked/dataset/emotions/anger/art_pieces'
directory2 = '/home/runner/NewHacksforked/dataset/emotions/anger/poetry/english'
directory3 = '/home/runner/NewHacksforked/dataset/emotions/anger/poetry/hindi'
directory4 = '/home/runner/NewHacksforked/dataset/emotions/anger/songs/english'
directory5 = '/home/runner/NewHacksforked/dataset/emotions/anger/songs/hindi'
directory6 = '/home/runner/NewHacksforked/dataset/emotions/calm/art_pieces'
directory7 = '/home/runner/NewHacksforked/dataset/emotions/calm/poetry/english'
directory8 = '/home/runner/NewHacksforked/dataset/emotions/calm/poetry/hindi'
directory9 = '/home/runner/NewHacksforked/dataset/emotions/calm/songs/english'
directory10 = '/home/runner/NewHacksforked/dataset/emotions/calm/songs/hindi'
directory11 = '/home/runner/NewHacksforked/dataset/emotions/fear/art_pieces'
directory12 = '/home/runner/NewHacksforked/dataset/emotions/fear/poetry/english'
directory13 = '/home/runner/NewHacksforked/dataset/emotions/fear/poetry/hindi'
directory14 = '/home/runner/NewHacksforked/dataset/emotions/fear/songs/english'
directory15 = '/home/runner/NewHacksforked/dataset/emotions/fear/songs/hindi'
directory16 = '/home/runner/NewHacksforked/dataset/emotions/joy/art_pieces'
directory17 = '/home/runner/NewHacksforked/dataset/emotions/joy/poetry/english'
directory18 = '/home/runner/NewHacksforked/dataset/emotions/joy/poetry/hindi'
directory19 = '/home/runner/NewHacksforked/dataset/emotions/joy/songs/english'
directory20 = '/home/runner/NewHacksforked/dataset/emotions/joy/songs/hindi'
directory21 = '/home/runner/NewHacksforked/dataset/emotions/nostalgia/art_pieces'
directory22 = '/home/runner/NewHacksforked/dataset/emotions/nostalgia/poetry/english'
directory23 = '/home/runner/NewHacksforked/dataset/emotions/nostalgia/poetry/hindi'
directory24 = '/home/runner/NewHacksforked/dataset/emotions/nostalgia/songs/english'
directory25 = '/home/runner/NewHacksforked/dataset/emotions/nostalgia/songs/hindi'
directory26 = '/home/runner/NewHacksforked/dataset/emotions/sad/art_pieces'
directory27 = '/home/runner/NewHacksforked/dataset/emotions/sad/poetry/english'
directory28 = '/home/runner/NewHacksforked/dataset/emotions/sad/poetry/hindi'
directory29 = '/home/runner/NewHacksforked/dataset/emotions/sad/songs/english'
directory30 = '/home/runner/NewHacksforked/dataset/emotions/sad/songs/hindi'


def angerlist():
    for filename in os.listdir(directory1):
        f = os.path.join(directory1, filename)
        if os.path.isfile(f):
            anger[0] += [f]
    for filename in os.listdir(directory2):
        f = os.path.join(directory2, filename)
        if os.path.isfile(f):
            anger[1][0] += [f]
    for filename in os.listdir(directory3):
        f = os.path.join(directory3, filename)
        if os.path.isfile(f):
            anger[1][1] += [f]
    for filename in os.listdir(directory4):
        f = os.path.join(directory4, filename)
        if os.path.isfile(f):
            anger[2][0] += [f]
    for filename in os.listdir(directory5):
        f = os.path.join(directory5, filename)
        if os.path.isfile(f):
            anger[2][1] += [f]


def calmlist():
    for filename in os.listdir(directory6):
        f = os.path.join(directory6, filename)
        if os.path.isfile(f):
            calm[0] += [f]
    for filename in os.listdir(directory7):
        f = os.path.join(directory7, filename)
        if os.path.isfile(f):
            calm[1][0] += [f]
    for filename in os.listdir(directory8):
        f = os.path.join(directory8, filename)
        if os.path.isfile(f):
            calm[1][1] += [f]
    for filename in os.listdir(directory9):
        f = os.path.join(directory9, filename)
        if os.path.isfile(f):
            calm[2][0] += [f]
    for filename in os.listdir(directory10):
        f = os.path.join(directory10, filename)
        if os.path.isfile(f):
            calm[2][1] += [f]


def fearlist():
    for filename in os.listdir(directory11):
        f = os.path.join(directory11, filename)
        if os.path.isfile(f):
            fear[0] += [f]
    for filename in os.listdir(directory12):
        f = os.path.join(directory12, filename)
        if os.path.isfile(f):
            fear[1][0] += [f]
    for filename in os.listdir(directory13):
        f = os.path.join(directory13, filename)
        if os.path.isfile(f):
            fear[1][1] += [f]
    for filename in os.listdir(directory14):
        f = os.path.join(directory14, filename)
        if os.path.isfile(f):
            fear[2][0] += [f]
    for filename in os.listdir(directory15):
        f = os.path.join(directory15, filename)
        if os.path.isfile(f):
            fear[2][1] += [f]


def joylist():
    print()
    for filename in os.listdir(directory16):
        f = os.path.join(directory16, filename)
        if os.path.isfile(f):
            joy[0] += [f]
    for filename in os.listdir(directory17):
        f = os.path.join(directory17, filename)
        if os.path.isfile(f):
            joy[1][0] += [f]
    for filename in os.listdir(directory18):
        f = os.path.join(directory18, filename)
        if os.path.isfile(f):
            joy[1][1] += [f]
    for filename in os.listdir(directory19):
        f = os.path.join(directory19, filename)
        if os.path.isfile(f):
            joy[2][0] += [f]
    for filename in os.listdir(directory20):
        f = os.path.join(directory20, filename)
        if os.path.isfile(f):
            joy[2][1] += [f]


def nostalgialist():
    for filename in os.listdir(directory21):
        f = os.path.join(directory21, filename)
        if os.path.isfile(f):
            nostalgia[0] += [f]
    for filename in os.listdir(directory22):
        f = os.path.join(directory22, filename)
        if os.path.isfile(f):
            nostalgia[1][0] += [f]
    for filename in os.listdir(directory23):
        f = os.path.join(directory23, filename)
        if os.path.isfile(f):
            nostalgia[1][1] += [f]
    for filename in os.listdir(directory24):
        f = os.path.join(directory24, filename)
        if os.path.isfile(f):
            nostalgia[2][0] += [f]
    for filename in os.listdir(directory25):
        f = os.path.join(directory25, filename)
        if os.path.isfile(f):
            nostalgia[2][1] += [f]


def sadlist():
    for filename in os.listdir(directory26):
        f = os.path.join(directory26, filename)
        if os.path.isfile(f):
            sad[0] += [f]
    for filename in os.listdir(directory27):
        f = os.path.join(directory27, filename)
        if os.path.isfile(f):
            sad[1][0] += [f]
    for filename in os.listdir(directory28):
        f = os.path.join(directory28, filename)
        if os.path.isfile(f):
            sad[1][1] += [f]
    for filename in os.listdir(directory29):
        f = os.path.join(directory29, filename)
        if os.path.isfile(f):
            sad[2][0] += [f]
    for filename in os.listdir(directory30):
        f = os.path.join(directory30, filename)
        if os.path.isfile(f):
            sad[2][1] += [f]


def produce_piece(emotion: str, piece: str, lang='english') -> str:
    if emotion == 'anger':
        angerlist()
        if piece == 'art':
            index = random.randint(0, len(anger[0]) - 1)
            return contents(("art", anger[0][index]))
        elif piece == 'poem':
            if lang == 'english':
                index = random.randint(0, len(anger[1][0]) - 1)
                return contents(("poem", anger[1][0][index]))
            else:
                index = random.randint(0, len(anger[1][1]) - 1)
                return contents(("poem", anger[1][1][index]))
        else:
            if lang == 'english':
                index = random.randint(0, len(anger[2][0]) - 1)
                return contents(("song", anger[2][0][index]))
            else:
                index = random.randint(0, len(anger[2][1]) - 1)
                return contents(("song", anger[2][1][index]))

    elif emotion == 'calmness':
        calmlist()
        if piece == 'art':
            index = random.randint(0, len(calm[0]) - 1)
            return contents(("art", calm[0][index]))
        elif piece == 'poem':
            if lang == 'english':
                index = random.randint(0, len(calm[1][0]) - 1)
                return contents(("poem", calm[1][0][index]))
            else:
                index = random.randint(0, len(calm[1][1]) - 1)
                return contents(("poem", calm[1][1][index]))
        else:
            if lang == 'english':
                index = random.randint(0, len(calm[2][0]) - 1)
                return contents(("song", calm[2][0][index]))
            else:
                index = random.randint(0, len(calm[2][1]) - 1)
                return contents(("song", calm[2][1][index]))

    elif emotion == 'fear':
        fearlist()
        if piece == 'art':
            index = random.randint(0, len(fear[0]) - 1)
            return contents(("art", fear[0][index]))
        elif piece == 'poem':
            if lang == 'english':
                index = random.randint(0, len(fear[1][0]) - 1)
                return contents(("poem", fear[1][0][index]))
            else:
                index = random.randint(0, len(fear[1][1]) - 1)
                return contents(("poem", fear[1][1][index]))
        else:
            if lang == 'english':
                index = random.randint(0, len(fear[2][0]) - 1)
                return contents(("song", fear[2][0][index]))
            else:
                index = random.randint(0, len(fear[2][1]) - 1)
                return contents(("song", fear[2][1][index]))
    elif emotion == 'joy':
        joylist()
        if piece == 'art':
            index = random.randint(0, len(joy[0]) - 1)
            return contents(("art", joy[0][index]))
        elif piece == 'poem':
            if lang == 'english':
                index = random.randint(0, len(joy[1][0]) - 1)
                return contents(("poem", joy[1][0][index]))
            else:
                index = random.randint(0, len(joy[1][1]) - 1)
                return contents(("poem", joy[1][1][index]))
        else:
            if lang == 'english':
                index = random.randint(0, len(joy[2][0]) - 1)
                return contents(("song", joy[2][0][index]))
            else:
                index = random.randint(0, len(joy[2][1]) - 1)
                return contents(("song", joy[2][1][index]))
    elif emotion == 'nostalgia':
        nostalgialist()
        if piece == 'art':
            index = random.randint(0, len(nostalgia[0]) - 1)
            return contents(("art", nostalgia[0][index]))
        elif piece == 'poem':
            if lang == 'english':
                index = random.randint(0, len(nostalgia[1][0]) - 1)
                return contents(("poem", nostalgia[1][0][index]))
            else:
                index = random.randint(0, len(nostalgia[1][1]) - 1)
                return contents(("poem", nostalgia[1][1][index]))
        else:
            if lang == 'english':
                index = random.randint(0, len(nostalgia[2][0]) - 1)
                return contents(("song", nostalgia[2][0][index]))
            else:
                index = random.randint(0, len(nostalgia[2][1]) - 1)
                return contents(("song", nostalgia[2][1][index]))
    else:
        sadlist()
        if piece == 'art':
            index = random.randint(0, len(sad[0]) - 1)
            return contents(("art", sad[0][index]))
        elif piece == 'poem':
            if lang == 'english':
                index = random.randint(0, len(sad[1][0]) - 1)
                return contents(("poem", sad[1][0][index]))
            else:
                index = random.randint(0, len(sad[1][1]) - 1)
                return contents(("poem", sad[1][1][index]))
        else:
            if lang == 'english':
                index = random.randint(0, len(sad[2][0]) - 1)
                return contents(("song", sad[2][0][index]))
            else:
                index = random.randint(0, len(sad[2][1]) - 1)
                return contents(("song", sad[2][1][index]))


def contents(piece_loc):
    if piece_loc[0] == 'poem':
        with open(piece_loc[1], 'r') as f:
            text = f.readlines()
        f.close()
        return ''.join(text).replace('\n', ' ')

    elif piece_loc[0] == 'song':
        with open(piece_loc[1], 'r') as f:
            text = f.readlines()
        f.close()
        return text[0]

    else:
        return "https://replit.com/@cginko/NewHacksforked#"+ piece_loc[1][28:]
