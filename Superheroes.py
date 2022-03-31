import requests


def the_best_superheroes(*superheroes, powerstat='intelligence'):
    max_stat, hero = 0, []
    for name in superheroes:
        url = 'https://superheroapi.com/api/2619421814940190/search/' + name
        response = requests.get(url)
        stat = int(response.json()['results'][0]['powerstats'][powerstat])
        if stat > max_stat:
            max_stat = stat
            hero = [name]
        elif stat == max_stat:
            hero += [name]
    if len(hero) == 1:
        return f'Superhero with the highest {powerstat} is {" ".join(hero)}'
    else:
        return f'Superheroes with the highest {powerstat} are {" and ".join(hero)}'


if __name__ == '__main__':
    print(the_best_superheroes('Hulk', 'Captain America', 'Thanos'))
