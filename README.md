# Semantic String Similarity CLI

`sim` is a CLI interface to [`spacy`](https://spacy.io)'s string similarity engine. It uses the `en_vectors_web_lg` dataset to compare strings for their English semantic similarity. Given two words, phrases, or sentences, `sim` will tell you how similar their meanings are.

## Usage:
```bash
$ sim first_file.txt second_file.txt # compare two files
$ sim -s "first string" "second string" # compare two strings
```

The output is a number between 0 and 1, representing how similar the two strings are.

## Details:

Under the hood this uses the [`en_vectors_web_lg`](https://spacy.io/models/en#en_vectors_web_lg) model of word vectors trained with [`GLoVe`](https://nlp.stanford.edu/projects/glove/).

This is a large dataset, which makes for long startup times. So `sim` spins off a process in the background to hold the model, and works under a client-server model with it. This means that if you run `sim` a number of times in a row, only the first run is slow.

This background process does take up a fair bit of memory, typically around 2GB. After 20 minutes of inactivity it will automatically be killed, in order not to take up memory indefinitely. You can change the length of this timeout with the `--timeout` flag.
