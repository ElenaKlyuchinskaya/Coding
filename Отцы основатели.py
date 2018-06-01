fathers = {'Harold Abelson': 'Logo',
        'Kenneth Eugene Iverson': 'APL',
        'Guido van Rossum': 'Python',
        'Rasmus Lerdorf': 'Php',
        'Andrei Alexandrescu': 'C++',
        'Alfred Vaino Aho': 'AWK',
        'Simon Cozens': 'Parrot',
        'James Gosling': 'Java',
        'Jeremy Ashkenas': 'CoffeeScript',
        'Walter Bright': 'D',
        'John George Kemeny': 'Basic',
        'Larry Wall': 'Perl',
        'Peter Naur': 'Algol',
        'Don Syme': 'F#'
        }
choiceAction = input('Введите sorted или search: ')
if choiceAction == 'sorted':
        sortName = sorted(fathers.keys())
        for lang in sortName:
                print(lang, " - ", fathers[lang])
elif choiceAction == 'search':
        searchName = input("Введите имя: ")
        for name, value in fathers.items():
                if name == searchName:
                        print(searchName, 'участовал в разработке языка', fathers[name])
                        break
        else:
                print("Не удалось найти этого человека")
else:
        print('Попробуйте ещё раз, возможно вы ввели команду неправильно')