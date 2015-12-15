import re
from collections import namedtuple

Ingredient = namedtuple('Ingredient', 'name, properties')


def find_recipe(lines, limit=100):
    ingredients = []

    # Load ingredients
    regex = re.compile(r'^(\w+): capacity ([\d-]+), durability ([\d-]+), flavor ([\d-]+), texture ([\d-]+), calories ([\d-]+)')
    for line in lines:
        res = regex.match(line)
        data = res.groups()
        ingredients.append(Ingredient(data[0], map(int, data[1:])))

    # List all recipes
    recipes = []
    def _make_recipes(available, recipe, nb):
        if recipe and len(recipe) == nb:
            recipes.append(list(recipe))
            return

        if recipe is None:
            recipe = []

        count = sum([x for _,x in recipe])
        start = 0
        end = limit - count
        if len(recipe) == nb - 1:
            # special case Last
            start = limit - count
            end = start + 1

        # Build combinations
        for i in range(start, end):
            ingredient = available[len(recipe)]
            recipe.append((ingredient, i))
            _make_recipes(available, recipe, nb)
            recipe.pop()

    _make_recipes(ingredients, None, len(ingredients))

    # Search best score
    best_score = 1
    for recipe in recipes:
        # Calc score
        score = 1
        for i in range(0, 4):
            score *= max(sum([ingredient.properties[i]*nb for ingredient, nb in recipe]), 0)

        # Best ?
        best_score = max(best_score, score)
        if score  == best_score:
            print ' + '.join(['%d x %s' % (x, i.name) for i,x in recipe]), score

    return best_score

if __name__ == '__main__':
    with open('15.input', 'r') as f:
        print find_recipe(f.readlines())
