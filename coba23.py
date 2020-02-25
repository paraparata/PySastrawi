# import StemmerFactory class
from build.lib.Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stemming process
sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan'
output   = stemmer.stem(sentence)

# print(output)
# ekonomi indonesia sedang dalam tumbuh yang bangga

print(stemmer.stem('siapapun'))
# mereka tiru

#Need module 're' for regular expression
# import re
# cobs = re.split(r'-*(lah|kah|tah|pun)$', 'siapapun yang bersalah')
# pisah = ' '
# print(pisah.join(cobs))
#
# search_string = 'dan makan 134-234-234'
# pattern = r'(\d{4}|dan)'
# match = re.match(pattern, search_string)
# #If-statement after search() tests if it succeeded
# if match:
#    print('regex matches: {}'.format(match.group()))
# else:
#    print('pattern not found')

# requid library
# import re
# #given string
# str = 'siapapun'
# #pattern to match
# pattern = r'-*(lah|kah|tah|pun)$'
# #replace the matched pattern from string with,
# replace = r' -*'
#    ## re.sub(pat, replacement, str) -- returns new string with all replacements,
#    ## \1 is group(1), \2 group(2) in the replacement
# print (re.sub(pattern, replace, str))