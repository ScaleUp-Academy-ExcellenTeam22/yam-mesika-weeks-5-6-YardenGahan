"""
This functions calculates the total price for wanted ingredients
Arguments:
@param prices - dictionary[key: item's name, value: price for 100g]
@param optionals - list of ingredients to ignore.
@param ingredients - dictionary[ingredient_name : amount in grams]
@return - The total price of all the ingredients
#
"""
def get_recipe_price(prices, optionals= None, **ingredients):

    if optionals is None:
        optionals = []

    if not ingredients:
        return 0

    return sum(prices[ingredient] / 100 * amount
               for ingredient, amount in ingredients.items()
               if ingredient not in optionals)
