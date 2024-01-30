# Sentence Piece Toolkit

## Overview
This repository contains a collection of Python scripts for training a custom sentence piece tokenizer which can be later merged with the original Llama 2 tokenizer. The tokenizer can be trained on the Cultura X dataset or on a custom dataset such as ccnet.

pip install wikiextractor
wikiextractor ./wiki-dumps/rowiki-20240120-pages-articles.xml.bz2 -o ./wiki-data --json


## Scripts

### 1. `cultura_x_checksum.py`: generates and verifies checksums for the Cultura X dataset; if you are going to use it you can check the integrity of the files with this script

### 2. `merge_datasets.py`: merges multiple datasets into a single file, facilitating unified processing

### 3. `sentence_piece_train.py`: trains a SentencePiece tokenizer model on a given dataset

### 4. `merge_tokenizers.py`: combines multiple tokenizer models into a single, comprehensive tokenizer; you can achieve this by running the following command `python merge_tokenizers.py --llama_tokenizer_dir llama-tokenizer --custom_tokenizer_file ./tokenizers/ro_tokenizer.model`

### 5. `merge_wiki_data.py`: for evaluation of the trained tokenizer I used the rowiki dump; before using this script you have to download the latest wiki dump and preprocess it with wikiextractor `wikiextractor ./wiki-dumps/rowiki-latest-pages-articles.xml.bz2 -o ./wiki-data --json`

### 6. `compare_tokenizers.py`: compares the performance and output of different tokenization algorithms


## Requirements
- Python 3.x
- Additional dependencies are listed in `requirements.txt`.
