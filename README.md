# Laboratório 6 - P2: Tokenizador BPE e WordPiece

Implementação do algoritmo Byte Pair Encoding (BPE) do zero e exploração do WordPiece com a biblioteca HuggingFace Transformers.

## Estrutura

- `bpe_tokenizer.py` — Implementação completa das 3 tarefas do laboratório.

## Como Executar
```bash
pip install transformers torch
python3 bpe_tokenizer.py
```

## Tarefas Implementadas

### Tarefa 1 — Motor de Frequências (`get_stats`)
Função que varre o vocabulário inicial e conta a frequência de todos os pares adjacentes de símbolos. Validação: o par `('e', 's')` retorna contagem máxima de 9, pois aparece 6 vezes em *newest* e 3 vezes em *widest*.

### Tarefa 2 — Loop de Fusão (`merge_vocab`)
Função que substitui o par mais frequente pela versão unificada. O loop principal executa 5 iterações, imprimindo o par fundido e o vocabulário atualizado a cada rodada. Ao final das iterações, tokens morfológicos como `est</w>` são formados, comprovando a eficácia do algoritmo.

### Tarefa 3 — WordPiece com BERT Multilingual
Uso do tokenizador `bert-base-multilingual-cased` da HuggingFace para segmentar a frase:
> "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."

## Sobre os Sinais `##` no WordPiece

Nos tokens gerados pelo BERT, o prefixo `##` indica que aquele sub-token é uma **sub-palavra de continuação** — ele não ocorre no início de uma palavra, mas sim dá sequência ao token anterior. Por exemplo, a palavra "inconstitucionalmente" é segmentada em múltiplos pedaços, onde tokens como `##ional` e `##mente` sinalizam que são sufixos anexados ao fragmento precedente.

Essa estratégia é fundamental porque **impede o travamento do modelo diante de vocabulário desconhecido (OOV — Out-of-Vocabulary)**. Em vez de substituir palavras raras ou novas por um único token genérico `[UNK]` — o que causaria perda total de informação —, o WordPiece decompõe qualquer palavra em sub-palavras já presentes no vocabulário. Assim, o modelo consegue capturar padrões morfológicos como sufixos (`-mente`, `-ção`) e prefixos, generalizando para palavras nunca vistas durante o treinamento.

## Uso de IA Generativa

Durante o desenvolvimento, utilizei o Claude (Anthropic) como ferramenta de revisão e apoio. O código foi escrito e estruturado pelo autor, com uso de IA para revisar a lógica da função `merge_vocab`, identificar possíveis erros e sugerir melhorias pontuais. O conteúdo deste README também passou por revisão com auxílio de IA.

Conforme exigido pelas diretrizes de integridade acadêmica da disciplina, esta citação declara o uso de IA generativa no processo de desenvolvimento.