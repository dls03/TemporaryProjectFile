# DeepIsoFun

DeepIsoFun: A deep domain adaptation approach to predict isoform functions
Dipan Shaw, Hao Chen, and Tao Jiang

Isoforms are mRNAs produced from the same gene locus by alternative splicing and may have different functions. Although gene functions have been studied extensively, little is known about the specific functions of isoforms. Recently, some computational approaches based on multiple instance learning have been proposed to predict isoform functions from annotated gene functions and expression data, but their performance is far from being desirable primarily due to the lack of labeled training data. To improve the performance on this problem, we propose a novel deep learning method, DeepIsoFun, that combines multiple instance learning with domain adaptation. The latter technique helps to transfer the knowledge of gene functions to the prediction of isoform functions and provides additional labeled training data. Our model is trained on a deep neural network architecture so that it can adapt to different expression distributions associated with different gene ontology terms.
