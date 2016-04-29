# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:26:37 2016

@author: gbayomi
"""

import os, struct
from array import array as pyarray
from pylab import *
from numpy import *

def numberToVector(z):
    a = np.zeros(10)
    a[z] = 1
    return a

def load_mnist(dataset="training", digits=np.arange(10), path="."):
    """
    Loads MNIST files into 3D numpy arrays

    Adapted from: http://abel.ee.ucla.edu/cvxopt/_downloads/mnist.py
    """

    if dataset == "training":
        fname_img = os.path.join(path, 'data/train-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'data/train-labels-idx1-ubyte')
    elif dataset == "testing":
        fname_img = os.path.join(path, 'data/t10k-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'data/t10k-labels-idx1-ubyte')
    else:
        raise ValueError("dataset must be 'testing' or 'training'")

    flbl = open(fname_lbl, 'rb')
    magic_nr, size = struct.unpack(">II", flbl.read(8))
    lbl = pyarray("b", flbl.read())
    flbl.close()

    fimg = open(fname_img, 'rb')
    magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
    img = pyarray("B", fimg.read())
    fimg.close()

    ind = [ k for k in range(size) if lbl[k] in digits ]
    N = len(ind)

    images = zeros((N, rows, cols), dtype=uint8)
    labels = zeros((N, 1), dtype=int8)
    for i in range(len(ind)):
        images[i] = array(img[ ind[i]*rows*cols : (ind[i]+1)*rows*cols ]).reshape((rows, cols))
        labels[i] = lbl[ind[i]]

    return images, labels


def getSample(sample):
    images, labels = load_mnist('training')
    
    train_images = np.zeros(shape=(sample,784))
    train_labels = np.zeros(shape=(sample,10))
    for c in range(0, sample):
        train_images[c] = images[c].flatten()
        train_labels[c] = numberToVector(labels[c])
    return train_images, train_labels
    
def getTestingSample(sample):
    images, labels = load_mnist('testing')
    train_images = np.zeros(shape=(sample,784))
    train_labels = np.zeros(shape=(sample,10))
    for c in range(0, sample):
        train_images[c] = images[c].flatten()
        train_labels[c] = numberToVector(labels[c])
    return train_images, train_labels