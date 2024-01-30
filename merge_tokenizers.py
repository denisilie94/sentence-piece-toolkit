import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

import argparse
import sentencepiece as spm

from sentencepiece import sentencepiece_model_pb2 as sp_pb2_model
from transformers import LlamaTokenizer


# Argument parser setup
parser = argparse.ArgumentParser()
parser.add_argument('--llama_tokenizer_dir', default=None, type=str, required=True)
parser.add_argument('--custom_tokenizer_file', default=None, type=str)
args = parser.parse_args()

# Read arguments
llama_tokenizer_dir = args.llama_tokenizer_dir
custom_tokenizer_file = args.custom_tokenizer_file

# Load tokenizers
llama_tokenizer = LlamaTokenizer.from_pretrained(llama_tokenizer_dir)
custom_tokenizer = spm.SentencePieceProcessor()
custom_tokenizer.Load(custom_tokenizer_file)

# Load models
llama_spm = sp_pb2_model.ModelProto()
llama_spm.ParseFromString(llama_tokenizer.sp_model.serialized_model_proto())
custom_spm = sp_pb2_model.ModelProto()
custom_spm.ParseFromString(custom_tokenizer.serialized_model_proto())

# Print number of tokens
print(len(llama_tokenizer), len(custom_tokenizer))
print(llama_tokenizer.all_special_tokens)
print(llama_tokenizer.all_special_ids)
print(llama_tokenizer.special_tokens_map)

# Add Custom tokens to LLaMA tokenizer
llama_spm_tokens_set = set(p.piece for p in llama_spm.pieces)
print(f"Before: {len(llama_spm_tokens_set)}")
for p in custom_spm.pieces:
    piece = p.piece
    if piece not in llama_spm_tokens_set:
        new_p = sp_pb2_model.ModelProto().SentencePiece()
        new_p.piece = piece
        new_p.score = 0
        llama_spm.pieces.append(new_p)
print(f"New model pieces: {len(llama_spm.pieces)}")

# Save merged tokenizer
output_sp_dir = 'merged_tokenizer_sp'
output_hf_dir = 'merged_tokenizer_hf'
os.makedirs(output_sp_dir, exist_ok=True)
with open(output_sp_dir + '/custom_llama.model', 'wb') as f:
    f.write(llama_spm.SerializeToString())
tokenizer = LlamaTokenizer(vocab_file=output_sp_dir + '/custom_llama.model')
tokenizer.save_pretrained(output_hf_dir)
print(f"Custom-LLaMA tokenizer has been saved to {output_hf_dir}")

# Test merged tokenizer
llama_tokenizer = LlamaTokenizer.from_pretrained(llama_tokenizer_dir)
custom_llama_tokenizer = LlamaTokenizer.from_pretrained(output_hf_dir)
print(tokenizer.all_special_tokens)
print(tokenizer.all_special_ids)
print(tokenizer.special_tokens_map)
text = '''Românie, țara mea, astăzi este ziua ta! La mulți ani!
The primary use of LLaMA is research on large language models, including'''
print("Test text:\n", text)
print(f"Tokenized by LLaMA tokenizer: {llama_tokenizer.tokenize(text)}")
print(f"Tokenized by Custom-LLaMA tokenizer: {custom_llama_tokenizer.tokenize(text)}")
