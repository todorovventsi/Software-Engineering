countries = input().split(', ')
capitals = input().split(', ')

all_stored = {countries[i]: capitals[i] for i in range(len(countries))}
print(*[f"{country} -> {capital}" for country, capital in all_stored.items()], sep='\n')
