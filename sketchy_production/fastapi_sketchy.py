import os
from tensorflow.keras.models import load_model
import numpy as np
import time
from tensorflow.keras.applications.resnet50 import preprocess_input
from fastapi import FastAPI, File
from io import BytesIO
import pandas as pd

app = FastAPI()

app.state.classifier = load_model('ResNet_sketch_full_sketchy_baseline_data_aug.h5')
app.state.match = load_model('sketch_embedding_ep_cycle_6_triplet_64_resnet_fully_trainable_batch_1000_steps_weights_no_class_layer_c1_50_margin_15_decay.h5')
model = app.state.classifier
siamese = app.state.match
labels = ['airplane', 'alarm_clock', 'ant', 'ape', 'apple', 'armor', 'axe',
        'banana', 'bat', 'bear', 'bee', 'beetle', 'bell', 'bench', 'bicycle',
        'blimp', 'bread', 'butterfly', 'cabin', 'camel', 'candle', 'cannon',
        'car_(sedan)', 'castle', 'cat', 'chair', 'chicken', 'church', 'couch',
        'cow', 'crab', 'crocodilian', 'cup', 'deer', 'dog', 'dolphin', 'door',
        'duck', 'elephant', 'eyeglasses', 'fan', 'fish', 'flower', 'frog',
        'geyser', 'giraffe', 'guitar', 'hamburger', 'hammer', 'harp', 'hat',
        'hedgehog', 'helicopter', 'hermit_crab', 'horse', 'hot-air_balloon',
        'hotdog', 'hourglass', 'jack-o-lantern', 'jellyfish', 'kangaroo',
        'knife', 'lion', 'lizard', 'lobster', 'motorcycle', 'mouse', 'mushroom',
        'owl', 'parrot', 'pear', 'penguin', 'piano', 'pickup_truck', 'pig',
        'pineapple', 'pistol', 'pizza', 'pretzel', 'rabbit', 'raccoon',
        'racket', 'ray', 'rhinoceros', 'rifle', 'rocket', 'sailboat', 'saw',
        'saxophone', 'scissors', 'scorpion', 'sea_turtle', 'seagull', 'seal',
        'shark', 'sheep', 'shoe', 'skyscraper', 'snail', 'snake', 'songbird',
        'spider', 'spoon', 'squirrel', 'starfish', 'strawberry', 'swan',
        'sword', 'table', 'tank', 'teapot', 'teddy_bear', 'tiger', 'tree',
        'trumpet', 'turtle', 'umbrella', 'violin', 'volcano', 'wading_bird',
        'wheelchair', 'windmill', 'window', 'wine_bottle', 'zebra']


@app.get('/')
def root():
    return {'OK?': 'Indeed'}


@app.post('/classify')
async def classify(sketch: bytes = File(...)):

    sketch_list = list(sketch)
    num = 8
    sketch_array = np.array(sketch_list).reshape((224,224,3))
    sketch_processd = preprocess_input(sketch_array)
    prediction = model.predict(np.expand_dims(sketch_processd, axis = 0))
    response = {'prediction': prediction.tolist()}

    sketch_features = siamese.predict(np.expand_dims(sketch_processd/255, axis = 0))[0]
    feature_space = pd.read_pickle('photo_features.pkl')
    
    prediction = np.array(response['prediction'])

    df = pd.DataFrame({'label': labels,
    'proba': prediction[0]}).sort_values(
        'proba',
        ascending = False,
        ignore_index = True
        )  
    label_list = df.label[:3]
    print(label_list)
    for label in label_list:

        best_photos = []
        label_features = feature_space[feature_space['cat'] == label].reset_index()
        dist_vec = [np.sum((photo[1]['feat_vec_sketch_avg_list']-sketch_features)**2) for photo in label_features.iterrows()]

        label_features['distances'] = dist_vec
        label_features = label_features.sort_values('distances').reset_index()

        best_photos.append(label_features.name[:num])

        response[label] = best_photos

    return response

# @app.post('/match')
# async def match(label1, choice: str, num: int = 8, sketch: bytes = File(...)):

#     sketch_list = list(sketch)

#     sketch_array = np.array(sketch_list).reshape((224,224,3))
#     sketch_preprocessed = preprocess_input(sketch_array)

#     sketch_features = siamese.predict(sketch_preprocessed)

#     response = {}

#     if choice == 'sketch':

#         feature_space = pd.read_pickle('sketch_features.pickle')
        
#         for label in labels_list:

#             best_photos = []

#             label_features = feature_space[feature_space['cat'] == label].reset_index()
#             dist_vec = [np.sum((photo[1]['feature_vec']-sketch_features)**2) for photo in label_features.itterows()]
#             label_features['distances'] = dist_vec
#             label_features = label_features.sort_values('distances').reset_index()
#             best_photos.append(label_features.name[:num])

#             response[label] = best_photos

#         print(response)
#         return response


#     elif choice == 'photo':

#         feature_space = pd.read_pickle('photo_features.pickle')

#         for label in labels_list:

#             best_photos = []

#             label_features = feature_space[feature_space['cat'] == label].reset_index()
#             dist_vec = [np.sum((photo[1]['feature_vec']-sketch_features)**2) for photo in label_features.itterows()]
#             label_features['distances'] = dist_vec
#             label_features = label_features.sort_values('distances').reset_index()
#             best_photos.append(label_features.name[:num])
#             response[label] = best_photos

#         return response

#     else:
#         return None
