FROM python:3.10.6-buster
FROM tensorflow/tensorflow:2.10.0

COPY requirements_docker.txt /requirements_docker.txt
COPY fastapi_sketchy.py /fastapi_sketchy.py
COPY ResNet_sketch_full_sketchy_baseline_data_aug.h5 /ResNet_sketch_full_sketchy_baseline_data_aug.h5
COPY sketch_embedding_ep_cycle_6_triplet_64_resnet_fully_trainable_batch_1000_steps_weights_no_class_layer_c1_50_margin_15_decay.h5 /sketch_embedding_ep_cycle_6_triplet_64_resnet_fully_trainable_batch_1000_steps_weights_no_class_layer_c1_50_margin_15_decay.h5
COPY photo_features.pkl /photo_features.pkl

RUN pip install --upgrade pip
RUN pip install -r requirements_docker.txt

CMD uvicorn fastapi_sketchy:app --host 0.0.0.0
