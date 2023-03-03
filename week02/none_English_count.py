## Import required libraries
import enchant
from mrjob.job import MRJob

# Define WordCounter
class WordCounter(MRJob):
    # Define the mapper function
    def mapper(self, _, line):
        
        # Create an instance of the enchant dictionary for the English language
        d = enchant.Dict("en_US")
        # Split the line into words
        w = line.split()
        for w in w:
            
            # Check if the word is not in the dictionary
            if not d.check(w):
                yield w.lower(), 1
    # Define the reducer function
    def reducer(self, w, counts):
        yield w, sum(counts)
#executed the main program
if __name__ == '__main__':
    WordCounter.run()
