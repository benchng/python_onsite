'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''


current_population = 380123456

secondsperyear = 356 * 24 * 60 * 60
secondsperyear = 356 * 24 * 60 * 60
secondsperyear = 356 * 24 * 60 * 60

birth = secondsperyear / 6
death = secondsperyear / 12
immigrants = secondsperyear / 40

first_year = current_population + birth - death + immigrants
second_year = first_year + birth - death + immigrants
third_year = second_year + birth - death + immigrants

print(f"The population after the first year is {first_year}, the population after the second year is {second_year}, lastly the population of the third year is {third_year}")
