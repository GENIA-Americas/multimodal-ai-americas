# Models

Registry of models planned or built in this project.

**No model in this registry has released weights.** Every entry is a plan. An entry moves to "Released" only when weights, config, tokenizer (or equivalent), a model card, and evaluation code are public and linked here. Weights are hosted on the Hugging Face Hub, not in this repository.

## Registry

| Model | Task | Languages / coverage | Status |
|-------|------|----------------------|--------|
| AmeriXLM | Multilingual masked language model | es-LA, pt-BR, en, qu, gn, nah | Planned. Placeholder on the [Hub](https://huggingface.co/genia-americas/ameri-xlm). |
| CorridorNER | Named entity recognition | es-LA, pt-BR | Planned |
| IndigenousLM | Language modeling | qu, gn, nah | Planned |
| HarvestNet | Crop yield prediction | Brazil, Argentina, Mexico | Planned |
| CropHealthViT | Crop disease detection | Tropical crops | Planned |
| CorridorRoute | Logistics optimization | Americas | Planned |
| TradeFlowLSTM | Trade volume forecasting | Latin America and the Caribbean | Planned |
| CivicIntent | Intent classification | es-LA | Planned |

## AmeriXLM

Planned multilingual encoder, aimed at Latin American Spanish, Brazilian Portuguese, English, Quechua, Guarani, and Nahuatl.

Motivation: XLM-R and mBERT split training compute roughly by how much text exists per language, which likely leaves regional varieties underweighted. Whether a regionally weighted corpus helps is the open question, and it has not been measured.

Design targets (all subject to change): RoBERTa-style encoder, masked language modeling, 512-token context, regional tokenizer. Size, vocabulary, corpus, and compute budget are undecided.

Evaluation plan: [AmeriNLI](../datasets/amerinli/) and RegioNER, see [research/benchmarks](../research/benchmarks/). There are no AmeriXLM results. Do not cite it as a released model.

## Model card requirements

Every released model needs a model card covering:

- Description and intended use
- Training data: sources, size, licenses, known limitations
- Evaluation results with the code and data to reproduce them
- Failure modes and out-of-distribution behavior
- Prohibited uses
- License
- Contact

## Contributing a model

1. Open an issue describing the model, its data, and how it will be evaluated.
2. Share evaluation results on at least one benchmark from [research/benchmarks](../research/benchmarks/), with scripts and logs.
3. Publish the weights and model card on the Hugging Face Hub.
4. Add or update the registry row here with links.

Contact: admin@genia.ai
