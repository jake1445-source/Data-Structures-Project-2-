# initiate a class with the book file as the input 

from collections import Counter
import string 
import pandas as pd 
import matplotlib.pyplot as plt 


class TextAnalysis: 
    '''This method used to perform analytics on any piece of text. Simply instantiate the class with the file path to the .txt 
    file that contains the piece of text to be analyzed. 
    ----------------------------------------------------

    Functions: 

        lettercounter: counts the number of times a letter (a-z) appears in the text, and plots by frequency
            Args
                table: default True, prints a table of letter counts and frequencies
                plot: default True, displays a bar graph of the letter frequencies

        wordcounter: Same as lettercounter, but for words 

        kgramcounter: finds the 20 most common k-word pairs, and arranges them into a table and graph by frequency 
            Args
                k: (int) defines the number of words in the sequence. EX: k = 2 for bigrams, 3 for trigrams, etc...
                plot: default True, shows plot of the most common k-grams 
                
    
    
    '''
    
    def __init__(self, filepath):
        self.filepath = filepath 
        
        # Open the file and store as self.text
        with open(filepath, 'r', encoding='utf-8') as f:
            self.text = f.read()
    


    def lettercounter(self, table = True, plot = True): 

        # Count letters using collections.Counter
        counter = Counter()

        for i in self.text: 
            if i in string.ascii_lowercase: 
                counter[i] += 1

        # Now we have counter, a dictionary containing the counts for each letter, using the letters as keys

        
        df = pd.DataFrame(list(counter.items()), columns=['Letter', 'Count'])

        # sort by 
        df = df.sort_values(by='Count', ascending=False).reset_index(drop=True)

        # Plotting code 
        
        if plot:
            plt.figure(figsize=(10, 6))
            plt.bar(df['Letter'], df['Count'])
            plt.title('Letter Frequency')
            plt.xlabel('Letter')
            plt.ylabel('Count')
            plt.show()

        # If table is True, then return the table 
        if table:
            return df 


    def wordcounter(self, table=True, plot=True): 
        # split into words, split() is a built in python function to split a string 
        words = self.text.split(' ')
        counter = Counter(words)

        top40 = counter.most_common(40)

        # Like lettercounter, convert the dictionary into a df 

        df = pd.DataFrame(top40, columns = ['Words', 'Count'])

        

        if plot: 
            plt.figure(figsize=(12, 4))
            plt.bar(df['Words'], df['Count'], width=0.9)
            plt.title('Top 40 Words and thier Frequencies')
            
            plt.xlabel('Word')
            plt.ylabel('Count')
            plt.xticks(rotation=55, ha='right')
            plt.show()

        if table: 
            return df


    def kgramcounter(self, k = 2, table = True, plot = True): 
        '''This function will find the most common k-grams, and plot their frequencies on a bar chart. 

            k represents the number of consecutive words that define the k-gram. For example, k = 3 is a 3-gram (or trigram). 
            The function will find the most common set of 3 consecutive words. 

            To get a pandas df containing the most common k-grams, call the function by assigning it to a variable, and set plot = False.
            EX: 
                x = textanalysis.kgramcounter(k = 2, table = True, plot = False)

            By doing this, the variable x is now a dataframe with the k-grams 

            
        
        '''
        # Split strings into words, default is to split by whitespace 
        words = self.text.split()
        
        # empty list to store them, to be updated in loop 
        kgrams = []

        # Loop through the words, joining every pair 
        for i in range(len(words)): 
            kgram = " ".join(words[i:i+k])
            kgrams.append(kgram)

        # Get top 20 k-grams 
        counter = Counter(kgrams)
        most_common = counter.most_common(20)

        # Make into a df 
        df = pd.DataFrame(most_common, columns=['K-gram', 'Count'])
            
        # Visualize this with a bar chart 
        plt.figure(figsize=(12, 4))
        plt.bar(df['K-gram'], df['Count'], width =0.9)
        plt.title(f'Top 20 {k}-grams and thier Frequencies')
        plt.xlabel('k-grams')
        plt.ylabel('Count')
        plt.xticks(rotation=55, ha='right')
        plt.show()

        if table: 
            return df

