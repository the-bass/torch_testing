FROM continuumio/anaconda3:5.1.0

RUN conda install twine
RUN conda install pytorch-cpu torchvision-cpu -c pytorch
