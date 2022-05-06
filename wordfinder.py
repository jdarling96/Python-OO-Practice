"""Word Finder: finds random words from a dictionary."""
import random

#words = open("words.txt" , "r")
class WordFinder:
    """Machine to return a random word from a path to a file on disk that contains words.

    >>> wf = WordFinder("words.txt")
    235886 words read


    >>> wf.random() is isinstance(ran, str)
    True
    

     """

    def __init__(self, txt):
        self.txt = open(txt , "r")
        self.r = []
        self.parse_file()
        print(f'{len(self.r)} words read')

       
        
    def parse_file(self):

        for char in self.txt:
            char.split()
            self.r.append(char)

         
        
        
        def random(self):
        ran = random.choice(self.r)
        return ran[:-2]



        
class SpecialWordFinder(WordFinder):
    """ Sub class of Wordfinder that will filter out blank lines/comments.
    
    >>> wf = SpecialWordFinder("words.txt")
    235886 words read
    
    """

    # def __init__(self,txt):
        # super().__init__(txt)
        

    def random_filter(self):
        filter = super().random()
        if len(filter) == 0 or filter.startswith('#'):
            return random_filter()
        else:
            return filter  


        

        



    
        

