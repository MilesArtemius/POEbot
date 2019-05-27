import re
import random


# with open('sayings.tsv', encoding='utf-8') as f:
#     originals = f.read()


codes = ('пов,2-л',
         'нп=непрош,ед,изъяв,3-л',
         'мн,изъяв,1-л',
         'ед,кр,муж',
         'нп=непрош,ед,изъяв,3-л,сов',
         'нп=непрош,ед,изъяв,3-л,несов',
         'прош,мн,изъяв,сов,пе',
         'прош,мн,изъяв,сов,пе',
         'нп=прош,ед,изъяв,сред,сов',
         '=V,пе=инф,несов')

def clean_output(saying):
    saying = re.sub('{.+?}', '', saying)
    return saying



def generator(first_halves, second_halves):
    beginnings = {}
    endings = {}
    for first_half in first_halves:
        beginnings[first_half] = []
    for i, second_half in enumerate(second_halves):
        if re.search('{.+пов.+}', second_half):
            if 'imperative' not in endings:
                endings['imperative'] = []
            endings['imperative'].append(second_half)
            beginnings[first_halves[i]].append('imperative')
    for i, second_half in enumerate(second_halves):
        if re.search('{.+V.+мн.+1-л.+}', second_half):
            if '1pl' not in endings:
                endings['1pl'] = []
            endings['1pl'].append(second_half)
            beginnings[first_halves[i]].append('1pl')
    for i, second_half in enumerate(second_halves):
        if re.search('{.+им.+}', second_half) and not re.search('{.+V.+}', second_half):
            if 'nominative' not in endings:
                endings['nominative'] = []
            endings['nominative'].append(second_half)
            beginnings[first_halves[i]].append('nominative')
    for i, second_half in enumerate(second_halves):
        if re.search('{.+инф.+}', second_half):
            if 'infinitive' not in endings:
                endings['infinitive'] = []
            endings['infinitive'].append(second_half)
            beginnings[first_halves[i]].append('infinitive')
    for i in range(100):
        beginning = ''
        ending = ''
        while beginning == '' or ending == '':
            beginning = ''
            ending = ''
            beginning = random.choice(list(beginnings.keys()))
            if beginnings[beginning]:
                ending = random.choice(endings[beginnings[beginning][0]])
        beginning = clean_output(beginning)
        ending = clean_output(ending)
        print(beginning, ending)



def clean_output(saying):
    saying = re.sub('{.+?}', '', saying)
    return saying


def main():
    with open('first_halves.txt', encoding='utf-8') as f:
        first_halves = f.read().split('\n')
    with open('second_halves.txt', encoding='utf-8') as f:
        second_halves = f.read().split('\n')
    # saying = 'Яблоко от яблони недалеко падает'
    # while saying in originals:
    #     saying = clean_output(generator(first_halves, second_halves))
    # print(saying + '.')
    generator(first_halves, second_halves)

if __name__ == '__main__':
    main()
