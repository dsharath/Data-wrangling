#
# Find the names of the individual animals that eat fish.
#
# The animals table has columns (name, species, birthdate) for each individual.
# The diet table has columns (species, food) for each food that a species eats.
#

QUERY = '''
SELECT ...
'''

select animals.name from animals join.dite where animals.species = diet.species and diet.food='fish';