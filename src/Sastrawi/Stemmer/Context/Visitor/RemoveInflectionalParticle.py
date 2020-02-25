import re
from Sastrawi.Stemmer.Context.Removal import Removal

class RemoveInflectionalParticle(object):
    """Remove Inflectional particle.
    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval". page 60

    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    def visit(self, context):
        result = self.remove(context.current_word)
        if result != context.current_word:
            removedPart = re.sub(result, '', context.current_word, 1)
            
            removal = Removal(self, context.current_word, result, removedPart, 'P')

            context.add_removal(removal.get_removed_part())
            context.current_word = result

    # def visit(self, context):
    #     result = self.remove(context)
    #     if result != context:
    #         removedPart = re.sub(result, '', context, 1)
            
    #         # removal = Removal(self, context.current_word, result, removedPart, 'P')
    #         removal = Removal(self, context, result, removedPart, 'P')

    #         # context.add_removal(removal)
    #         context = result + ' ' + removal.get_removed_part()
    #     return context

    def remove(self, word):
        """Remove inflectional particle : lah|kah|tah|pun"""
        return re.sub(r'-*(lah|kah|tah|pun)$', '', word, 1)

    # def remove(self, word):
    #     """Remove inflectional particle : lah|kah|tah|pun"""
    #     splitting = re.split(r'-*(lah|kah|tah|pun)$', word)
    #     splitter = ' '
    #     return splitter.join(splitting)

# string = 'siapapun'
# cobs = RemoveInflectionalParticle()
# hapus = cobs.visit(string)
# print(hapus)