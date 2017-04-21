# Text Classification: Song Lyrics
### Reid Fu, Sina Sabet, Catie Talbot, Logan Patiño, CSE 5525, SP17

## To Run
- install sklearn, numpy, gensim
  - `pip install sklearn numpy gensim`
- run `python run.py`
  - This will run the perceptron using the bag-of-words featurizer and "genre" labels.
  - Comment and uncomment relevant lines in `run.py` to change which model, labels, or featurizer will be used.
- To run Word2Vec, you will need to download the file at https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit, unzip it, and put it in the `data` folder to be used by `w2vec.py`. Importing Word2Vec is commented out of `run.py` to avoid an error running the other functions without the file.
