#list of sandwich ingredients
def sandwich(*ingredients):
    for ingredient in ingredients:
        print(f"- {ingredient}")

sandwich('ham', 'lettuce', 'cheese')

sandwich('bacon', 'avocado', 'lettuce')
