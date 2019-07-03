import os
import re
import random
# TODO: Ai suggest madding some \n's in code 2 make it more READABLE!
import system.command


class SayingCommand(system.command.Command):
    def __init__(self):
        super().__init__()
        self.description = 'Пришлю тебе твою любимую пословицу)'

    def process(self, text):
        return sayings(text)


def clean_output(text):
    text = re.sub('{.+?}', '', text)
    return text


def generator(first_halves, second_halves):
    # codes = ('пов,2-л',
    #          'нп=непрош,ед,изъяв,3-л',
    #          'мн,изъяв,1-л',
    #          'ед,кр,муж',
    #          'нп=непрош,ед,изъяв,3-л,сов',
    #          'нп=непрош,ед,изъяв,3-л,несов',
    #          'прош,мн,изъяв,сов,пе',
    #          'прош,мн,изъяв,сов,пе',
    #          'нп=прош,ед,изъяв,сред,сов',
    #          '=V,пе=инф,несов')

    with open(os.path.join(os.getcwd(), 'resources_sayings', 'sayings.txt'), encoding='utf-8') as f:
        originals = f.read()
    codes = {
        'imperative': '{.+пов.+}',
        '1pl': '{.+V.+мн,изъяв,1-л}',
        '3sg': '{.+V.+ед,изъяв,3-л}',
        '2sg': '{.+V.+ед,изъяв,2-л}'
    }
    beginnings = {}
    endings = {}
    for first_half in first_halves:
        beginnings[first_half] = []
    # Записываем коды половин пословиц
    for i, second_half in enumerate(second_halves):
        for code in list(codes.keys()):
            if re.search(codes[code], second_half):
                if code not in endings:
                    endings[code] = []
                endings[code].append(second_half)
                beginnings[first_halves[i]].append(code)
    for i, second_half in enumerate(second_halves):
        if re.search('{.+инф.+}', second_half) and not re.search('{.+изъяв.+}', second_half) and not re.search(
                '{.+пов.+}', second_half):
            if 'infinitive' not in endings:
                endings['infinitive'] = []
            endings['infinitive'].append(second_half)
            beginnings[first_halves[i]].append('infinitive')
    for i, second_half in enumerate(second_halves):
        if re.search('{.+им.+}', second_half) and not re.search('{.+V.+}', second_half):
            if 'nominative' not in endings:
                endings['nominative'] = []
            endings['nominative'].append(second_half)
            beginnings[first_halves[i]].append('nominative')
    for i, second_half in enumerate(second_halves):
        if not re.search('{.+им.+}', second_half) and not re.search('{.+V.+}', second_half):
            if 'oblique' not in endings:
                endings['oblique'] = []
            endings['oblique'].append(second_half)
            beginnings[first_halves[i]].append('oblique')
    beginning = ''
    ending = ''
    saying = ''
    code = ''
    while beginning == '' or ending == '':
        beginning = random.choice(list(beginnings.keys()))
        if beginnings[beginning]:
            ending = random.choice(endings[beginnings[beginning][0]])
        code = beginnings[beginning]
        saying = clean_output('{beginning} {ending}'.format(beginning=beginning, ending=ending))
        if saying in originals:
            beginning = ''
            ending = ''
            continue
    output = '{code}\n{saying}.'.format(code=code, saying=saying)
    return output


def sayings(text):
    with open(os.path.join(os.getcwd(), 'resources_sayings', 'first_halves.txt'), encoding='utf-8') as f:
        first_halves = f.read().split('\n')
    with open(os.path.join(os.getcwd(), 'resources_sayings', 'second_halves.txt'), encoding='utf-8') as f:
        second_halves = f.read().split('\n')
    final_output = generator(first_halves, second_halves)
    return final_output, ''
