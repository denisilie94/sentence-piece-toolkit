import time
import sentencepiece as spm

t0 = time.time()

# Set your input and output file paths
input_file = './data/ccnet_all.txt'
model_prefix = 'ro_tokenizer'

vocab_size = 20000
num_threads = 36
character_coverage = 1.0
input_sentence_size = 1e+7
shuffle_input_sentence = True
train_extremely_large_corpus = True

args = ''
args += f'--input={input_file} '
args += f'--model_prefix={model_prefix} '
args += f'--vocab_size={vocab_size} '
args += f'--num_threads={num_threads} '
args += f'--character_coverage={character_coverage} '
args += f'--input_sentence_size={input_sentence_size} '
args += f'--shuffle_input_sentence={shuffle_input_sentence} '
args += f'--train_extremely_large_corpus={train_extremely_large_corpus} '

# Train SentencePiece model
spm.SentencePieceTrainer.train(args)

sp = spm.SentencePieceProcessor()
sp.load(f'{model_prefix}.model')
tf = time.time()

print(f'Execution time: {tf - t0}')

text = "Hello, how are you?"
tokens = sp.encode(text)

# Get the size of the vocabulary
vocab_size = sp.get_piece_size()

# Get a list of all subwords in the vocabulary
subwords_list = [sp.id_to_piece(i) for i in range(vocab_size)]
