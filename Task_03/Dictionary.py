def generate_numbers(number) ->dict:
    return {x: x * x for x in range(1, number + 1)}


def count_characters(string) -> dict:
    return {x: string.count(x) for x in list(string)}
