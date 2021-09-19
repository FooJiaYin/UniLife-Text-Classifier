# Import pacakges
from kashgari.tasks.classification import BiGRU_Model
import os 


def BertPredict(pwd, txt, model):
  input = open(f'{pwd}/input/{txt}').read()
  txtSTR = input.replace('\u3000', '').replace(' ',"")
  output = model.predict([list(txtSTR)],multi_label_threshold=0.5)
  return output



if __name__ == "__main__":
  pwd = os.getcwd()
  bert_model = BiGRU_Model.load_model(f'{pwd}/model/saved_models/bert_model_ver4')

  output = BertPredict(pwd, 'test.txt', bert_model)[0]
  print(output)
