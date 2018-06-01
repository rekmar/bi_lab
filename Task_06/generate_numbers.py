def generate_numbers(number) ->dict:
    return {x: x*x for x in range(1, number+1)}