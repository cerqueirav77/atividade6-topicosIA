vocab = {
    'l o w </w>': 5,
    'l o w e r </w>': 2,
    'n e w e s t </w>': 6,
    'w i d e s t </w>': 3
}

def get_stats(vocab):
    pairs = {}
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i+1])
            pairs[pair] = pairs.get(pair, 0) + freq
    return pairs

def merge_vocab(pair, v_in):
    v_out = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word, freq in v_in.items():
        new_word = word.replace(bigram, replacement)
        v_out[new_word] = freq
    return v_out

print("Initial vocabulary:", vocab)

num_merges = 5
for i in range(num_merges):
    stats = get_stats(vocab)
    if not stats:
        break
    best_pair = max(stats, key=stats.get)
    vocab = merge_vocab(best_pair, vocab)
    print(f"\nIteration {i+1}: Merging {best_pair}")
    print("Updated vocabulary:", vocab)

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

frase = "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."

tokens = tokenizer.tokenize(frase)

print("\n--- Tarefa 3: WordPiece (BERT Multilingual) ---")
print(f"Frase original: {frase}")
print(f"Tokens gerados: {tokens}")