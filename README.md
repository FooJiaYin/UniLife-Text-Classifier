# Unify-NPL-Classifier


## Input

- 請將文章文字直接丟入`input`

## Notebook
- `model_training.ipynb`: 訓練模型的jupyter notebook (google colab hosted)

## Models
- `Bert_pretrain`: 為還沒訓練過的`BERT pretrained embeddings`，可以輸入notebook訓練
- `saved_models`: 為訓練結果
    - `ver 3`: 多標籤模型，F1 score: 0.44
    - `ver 4`: 單一標籤模型， F1 score: 0.91

## Output
-  {title:[category]}
