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

print(stemmer.stem('siapapun yang makan kueku'))

# import re

# # def akhiran(imbuhan):
# #     if ('lah'|'kah'|'tah'|'yah') in imbuhan:
# #         return 'ada'
# # ar = ['kah', 'sih']
# # # cob = re.search(r'(lah|kah|tah|pun)', ar)
# # print(akhiran(ar))

# ditt = ['str1', 'str2', 'str3']

# test = ['78', '1111', 'str3', 'str4', 'str5']


# for d in ditt:
#     if d in test:
#         print(d)
#         break

# def awalan(imbuhan):clea
#     prefix = ['me', 'be', 'di', 'ter', 'pe', 'se', 'ke']
#     for awal in imbuhan:
#         if awal in prefix:
#             return awal + ' '
#         break

# def akhiran(imbuhan):
#     suffix = ['lah', 'kah', 'tah', 'pun', 'kan', 'an', 'i', 'nya']
#     for akhir in imbuhan:
#         if akhir in suffix:
#             return akhir + ' '
#         break

# ar = ['be', 'lah']
# print(awalan(ar))