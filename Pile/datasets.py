   
import abc
import os
import json

import gdown
import lm_dataformat as lmd
from tqdm import tqdm

from .utils import *

class Dataset(abc.ABC):
    @abc.abstractmethod
    def name(self):
        """ Human-readable name of the dataset """
        pass

    @abc.abstractmethod
    def documents(self):
        """ A generator producing all documents in the dataset. """
        pass

    @abc.abstractmethod
    def clean(self):
        """ Remove any dataset files. """
        pass
    
    def size(self):
        """ Return an estimate of the dataset size. Implementations may use a faster, less accurate estimate. """

        size = sum(map(utf8len, tqdm(self.documents())))
        print('size', self.name(), size)
        return size
    
    def num_docs(self):
        """ Return an estimate of the number of documents in the dataset. Implementations may use a faster, less accurate estimate. """

        size = len(list(map(lambda x: None, tqdm(self.documents()))))
        print('docs', self.name(), size)
        return size
    
    def already_shuffled(self):
        """ Datasets where the source is already shuffled should override this to return True so that it isn't shuffled again. """
        return False
