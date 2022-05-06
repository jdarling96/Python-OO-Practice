"""Word Finder: finds random words from a dictionary."""
import random

#words = open("words.txt" , "r")
class WordFinder:

    def __init__(self, txt):
        self.txt = open(txt , "r")
        self.count = 0
        self.r = []
        self.parse_file()
        
        
        
    def parse_file(self):

        for char in self.txt:
            self.count += 1
            self.r.append(char)

        #print(self.r)  
        print(f'{self.count} words read')
        
        
        
    def random(self):
        ran = random.choice(self.r)
        return ran[:-2]



        
class SpecialWordFinder(WordFinder):

    def __init__(self,txt):
        super().__init__(txt)

    def random_filter(self):
        filter = super().random()
        if len(filter) == 0 or filter.startswith('#'):
            return random_filter()
        else:
            return filter      


        

        



    
        

