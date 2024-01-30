# Sentence Piece Toolkit

## Overview
This repository contains a collection of Python scripts for training a custom sentence piece tokenizer, which can be later merged with the original Llama 2 tokenizer. The tokenizer can be trained on the Cultura X dataset or a custom dataset such as ccnet.

## Scripts

### 1. `cultura_x_checksum.py`
This script generates and verifies checksums for the Cultura X dataset. Utilize this script to ensure the integrity of the files before using them in your projects.

### 2. `merge_datasets.py`
A utility script for merging multiple datasets into a single, cohesive file. This is particularly useful for unified processing and analysis of diverse data sources.

### 3. `sentence_piece_train.py`
Use this script to train a SentencePiece tokenizer model on your chosen dataset. It's a key component in developing your custom tokenizer.

### 4. `merge_tokenizers.py`
This script enables combining multiple tokenizer models into a single, comprehensive tokenizer. Execute the following command to merge a custom tokenizer with the Llama tokenizer:

```bash
python merge_tokenizers.py --llama_tokenizer_dir llama-tokenizer --custom_tokenizer_file ./tokenizers/ro_tokenizer.model
```

### 5. `merge_wiki_data.py`
The Romanian Wikipedia (rowiki) dump is used to evaluate the trained tokenizer. Before running this script, download the latest wiki dump and preprocess it using the wikiextractor command provided in the Installation section.

```bash
pip install wikiextractor
```
For wiki data extraction, run:

```bash
wikiextractor ./wiki-dumps/rowiki-20240120-pages-articles.xml.bz2 -o ./wiki-data --json
```

### 6. `compare_tokenizers.py`
An analytical tool for comparing the performance and output of different tokenization algorithms. It's instrumental in assessing the efficacy of your tokenizer against others.

## Requirements
- Python 3.x
- Additional dependencies are listed in `requirements.txt`.
