def naamLeeftijd(naam:str, leeftijd:int):
    print(f'Jouw naam is {naam} en je hebt een leeftijd van {leeftijd} jaar')
while True:
    naam = input('Wat is je naam? ')
    leeftijd = int(input('Wat is je leeftijd? '))
    naamLeeftijd(naam, leeftijd)
    if input('Wilt u nog een keer? ') == 'nee':
        break