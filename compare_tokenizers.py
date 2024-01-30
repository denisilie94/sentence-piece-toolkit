from transformers import LlamaTokenizer

llama_tokenizer_dir = './llama-tokenizer'
custom_tokenizer_dir = './merged_tokenizer_hf'
wiki_text_file = 'romanian_wiki_text.txt'

llama_tokenizer = LlamaTokenizer.from_pretrained(llama_tokenizer_dir)
custom_llama_tokenizer = LlamaTokenizer.from_pretrained(custom_tokenizer_dir)

print(custom_llama_tokenizer.all_special_tokens)
print(custom_llama_tokenizer.all_special_ids)
print(custom_llama_tokenizer.special_tokens_map)

with open(wiki_text_file, 'r', encoding='utf-8') as file:
    text = file.read()

text = text[:272812446]
print(f"Tokenized by LLaMA tokenizer: {len(llama_tokenizer.tokenize(text))}")
print(f"Tokenized by Custom-LLaMA tokenizer: {len(custom_llama_tokenizer.tokenize(text))}")
