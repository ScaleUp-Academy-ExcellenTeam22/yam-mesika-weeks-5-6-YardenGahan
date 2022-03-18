# Arguments:
# prices - dictionary[key: item's name, value: price for 100g]
# optionals - list of ingredients to ignore.
# ingredients - dictionary[ingredient_name : amount in grams]
# Return value - float
# This functions calculates the total price for wanted ingredients
def get_recipe_price(prices, optionals=[], **ingredients):

    if not ingredients:
        return 0

    return sum(prices[ingredient] / 100 * amount
               for ingredient, amount in ingredients.items()
               if ingredient not in optionals)
