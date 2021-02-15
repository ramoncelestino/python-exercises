
import re
def remove_vowels(str):
    s = re.findall(r'[^aeiou]*', str)
    print(''.join(s))


remove_vowels("Hoje e aqui na festa tentar encontrar cachorro")