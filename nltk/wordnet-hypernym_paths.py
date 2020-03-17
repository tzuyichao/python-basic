from nltk.corpus import wordnet as wn

motorcar = wn.synset('car.n.01')
motorcar_hypernym_paths = motorcar.hypernym_paths()
print('hypernym paths size: ', len(motorcar_hypernym_paths))
for motorcar_hypernym_path in motorcar_hypernym_paths:
    print(motorcar_hypernym_path)