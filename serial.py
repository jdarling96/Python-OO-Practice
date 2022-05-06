"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        self.start = start
        self.count = 0

    def __repr__(self):
        return f"SerialGenerator start={self.start} next={self.start + 1}"    

    def generate(self):
        self.count += 1
        return self.start + self.count - 1

    def reset(self):
        self.count = 0
        
          

        
        
        

       

        

            


