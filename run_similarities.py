# This python file is aimed at computing similarities between word sets. 

# 1. Read entities words sets and descriptive words sets from the file words_const.py
# 2. Generate cartesian product to obtain all possible pairs of entities and description
# 3. For each entities-description pair, obtain similarity between these two sets of words for all models. This gives similarity for each kadencja.
# 4. Gather some additional information, like word counts per each set per each kadencja
# 5. Create pandas dataframes and save these in the pickle files.


# %%
# Get needed imports 
import gzip
import gensim 
import logging
import re
import pandas as pd
import string
import os
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import pickle




# %%

class Words():
    '''
    This class is meant to represent the set of words in context of particular Word2vec embedding. 
    The methods are able to get word counts from particular kadencja, and also filter the words not present in the particular corpus.
    This is needed both for exploratory analysis of words later on, 
    but also gensim models throw an error when given a word that's not present in the vocabulary.

    '''
    def __init__(self, model, words_in):
        self.model = model
        self.words_in = words_in

    def find_counts(self):
        self.word_counts = [None]*len(self.words_in)

        for i, word in enumerate(self.words_in):
            try:
                self.word_counts[i] = self.model.wv.vocab[word].count
            except KeyError:
                self.word_counts[i] = 0
        
        self.words_dict = {k:v for k, v in zip(self.words_in, self.word_counts)}
        return self.words_dict

    def get_output_words(self):
        self.find_counts()
        self.output_words = []
        for i in range(len(self.word_counts)):
            if self.word_counts[i] >0:
                self.output_words.append(self.words_in[i])
        return self.output_words

# %%
class SimilarityOneYear():
    '''
    Get cosine similarity score for one particular model, after providing two sets of words. 
    Also, word statistics are computed with Word class defined above.
    
    '''
    def __init__(self, model, words1, words2):
        self.model = model
        self.words1 = words1
        self.words2 = words2
        self.words_class2 = Words(self.model, words2)
        self.words_class1 = Words(self.model, words1)
        self.words1_out = self.words_class1.get_output_words()
        self.words2_out = self.words_class2.get_output_words()

        print(f'From set one dropped {len(self.words1)-len(self.words1_out)} of {len(self.words1)} words')
        print(f'From set two dropped {len(self.words2)-len(self.words2_out)} of {len(self.words2)} words')

        if len(self.words1_out) == 0 or len(self.words1_out) == 0:
            print('one of the word sets was empty. Aborting')
            self.similarity = None
            return None

        self.similarity = self.model.wv.n_similarity(self.words1_out, self.words2_out)

# %%
class RunOneYear():
    '''
    This class runs similarity comparison for one kadencja. Besides functonality from SimilarityOneYear class, it also loads the model from specified path. 

    '''
    def __init__(self, path, words_entity = None, words_description = None):
        self.path = path
        self.model = None

        if words_description is None and words_entity is None:
            
            self.words_entity = ['kobieta', 'dziewczyna', 'antysemityzm']
            self.words_description = ['dobry', 'nowy']
        else:
            self.words_entity = words_entity
            self.words_description = words_description
            
    def run(self):
        self.model = Word2Vec.load(self.path)

        self.get_year_stats()
        self.similarity_class = SimilarityOneYear(self.model, self.words_entity, self.words_description)
        self.similarity = self.similarity_class.similarity

    def get_year_stats(self):
        self.no_distinct_words = len(self.model.wv.vocab)
        self.no_words = sum([i.count for _, i in self.model.wv.vocab.items()])


# %%
# Find paths to models for all kadencje  
models_paths = ['models/'+ i for i in os.listdir('models')]


# %%
# Test run with random input word sets - not run
similarities_scores = []
no_words = []
for path in models_paths:
    print(f'Running model at path {path}')
    a = RunOneYear(path)
    a.run()
    print(f'Model at path: {path}')
    print(a.similarity)
    similarities_scores.append((path, a.similarity))

    print(f'No. words {a.no_words}')
    no_words.append(a.no_words)

print(similarities_scores)
# %%
# create two helper lists - one with starting year of each kadencja, other with duration of kadencja (e.g. '1917-1922')
years =[re.sub('[^0-9\-]', '', i) for i in models_paths]
years_start = [int(i.split('-')[0]) for i in years]
# %%

similarities_scores
# %%
# Test plots - similarity score per year
plt.plot(years_start, [i[1] for i in similarities_scores])

# %%
# Test plot - number of words in each subcorpus
plt.plot(years_start, no_words)

# %%
# Use words from external file, first test run for all years:
import words_const
words_const.words_women

similarities_scores = []
no_words = []
for path in models_paths:
    print(f'Running model at path {path}')
    a = RunOneYear(path,words_entity=words_const.words_women,words_description=words_const.words_positive)
    a.run()
    print(f'Model at path: {path}')
    print(a.similarity)
    similarities_scores.append((path, a.similarity))
    print(f'No. words {a.no_words}')
    no_words.append(a.no_words)
print(similarities_scores)


# %%
words_const.words_entities
# %%
words_const.words_descriptions
# %%

a.get_year_stats()
# %%
1
# %%
a
# %%
# 
# 
def run_all_years(models_paths, words_entity, words_description):
    """Function to get similarities scores for particular word sets for all years

    Args:
        models_paths (list -> str): Paths to all word2vec models 
        words_entity (list -> str): List of words describing entities (like ['kobieta', 'dziewczyna']) 
        words_description ([type]): List of words for descriptors (like ['leniwy', 'głupi']) 

    Returns:
        Tuple with 3 elements:
        0: list of similarities scores per each year
        1: List of word counts for entities. This is sum of all occurences of the words from words_entity list in the subcorpus per one kadencja
        1: Same as above, but for descriptors instead of entities.
    """    
    similarities_scores = []
    no_words = []
    count_words_entity = []
    count_words_description = []
    

    for path in models_paths:
        print(f'Running model at path {path}')
        a = RunOneYear(path,words_entity=words_entity,words_description=words_description)
        a.run()
        print(f'Model at path: {path}')
        print(a.similarity)
        similarities_scores.append(a.similarity)
        count_words_entity.append(sum(a.similarity_class.words_class1.word_counts))
        count_words_description.append(sum(a.similarity_class.words_class2.word_counts))
        print(f'No. words {a.no_words}')
        no_words.append(a.no_words)

    print(similarities_scores)
    return (similarities_scores, count_words_entity, count_words_description)

# run_all_years(models_paths, words_const.words_women, words_const.words_positive)
# %%

# Main run. This loop creates cartesian join of entities sets and descriptors set, and saves similarities for each pair to a dict.
similarities_for_all_pairs = {}
counts_entities_for_all_pairs = {}
counts_description_for_all_pairs = {}

for entity in words_const.words_entities:
    for description in words_const.words_descriptions:
        print('New run for pair:')
        print((entity, description))

        out = run_all_years(models_paths, words_const.words_entities[entity], words_const.words_descriptions[description])

        similarities_for_all_pairs.update({f'{entity}_{description}': out[0]})
        counts_entities_for_all_pairs.update({f'{entity}_{description}': out[1]})
        counts_description_for_all_pairs.update({f'{entity}_{description}': out[2]})


# %%
# Last steps are for converting the similarities and word counts to pandas dataframes, and saving these to pickle files for further analysis.
with open('similarities_dict.pickle', 'wb') as handle:
    pickle.dump(similarities_for_all_pairs, handle)


# %%
df = pd.DataFrame(similarities_for_all_pairs)
# %%
df['year_start'] = years_start
df['years'] = years
df['no_words'] = no_words

df.to_pickle('similarities.pickle')
# %%

df_counts_entities = pd.DataFrame([(k.split('_')[0], v) for k, v in counts_entities_for_all_pairs.items()]).groupby(0).first()
df_counts_entities = pd.DataFrame(df_counts_entities.to_dict()[1])
df_counts_entities['year_start'] = years_start
df_counts_entities['years'] = years


 # %%
df_counts_description = pd.DataFrame([(k.split('_')[0], v) for k, v in counts_description_for_all_pairs.items()]).groupby(0).first()
df_counts_description = pd.DataFrame(df_counts_description.to_dict()[1])
df_counts_description['year_start'] = years_start
df_counts_description['years'] = years
# %%

df_counts_entities.to_pickle('counts_entities.pickle')
df_counts_description.to_pickle('counts_description.pickle')
# %%
