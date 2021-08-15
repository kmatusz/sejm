# Analysis of gender bias in Polish Parliamentary Corpus 

File contents:

- analyse_similarities.ipynb - notebook with main analysis. It reads data saved from the script run_similarities.py. 
- run_similarities.py - a script to obtain similarities between all entity-description pairs in all word2vec models. Input files are the word2vec models from models/ file, and words list from words_const.py. It saves similarities between sets and other stats to pickle files.
- word2vec.ipynb - training the word2vec models on all subcorpuses separately (one subcorpus - one kadencja). It outputs the models to models/ folder. As the input it takes data preprocessed using download_preprocess_corpus notebook - about 2GB worth of files.
- words_const.py - lists of words to describe entities and descriptive features
- download_preprocess_corpus.ipynb - a notebook to download the whole 30GB corpus from the IPI PAN website and preprocess it to reduce the size. This task was infeasible on our laptops, so we have run this notebook on Google Colab service. Even on the cloud, running of the file took about 8 hours, so we don't recommend to do it again.
