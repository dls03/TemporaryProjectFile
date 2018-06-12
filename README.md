# DeepIsoFun

DeepIsoFun: A deep domain adaptation approach to predict isoform functions

Isoforms are mRNAs produced from the same gene locus by alternative splicing and may have different functions. Although gene functions have been studied extensively, little is known about the specific functions of isoforms. Recently, some computational approaches based on multiple instance learning have been proposed to predict isoform functions from annotated gene functions and expression data, but their performance is far from being desirable primarily due to the lack of labeled training data. To improve the performance on this problem, we propose a novel deep learning method, DeepIsoFun, that combines multiple instance learning with domain adaptation. The latter technique helps to transfer the knowledge of gene functions to the prediction of isoform functions and provides additional labeled training data. Our model is trained on a deep neural network architecture so that it can adapt to different expression distributions associated with different gene ontology terms.


### Step0: Install Caffe 
Download the master branch of [Caffe](http://caffe.berkeleyvision.org/) and compile it in your machine. See here for the [installation](http://caffe.berkeleyvision.org/installation.html) guide. </br>  
For some systems current version of caffe might not work. You can try older [release](https://github.com/BVLC/caffe/releases).
### Step1: Prerquired tools
[CUDA](https://developer.nvidia.com/cuda-zone) </br> 
[OpenBLAS](http://www.openblas.net/) </br> 
[OpenCV](https://opencv.org/) </br> 
[Boost](https://www.boost.org/) </br> 
[Python and pycaffe](http://caffe.berkeleyvision.org/tutorial/interfaces.html) </br>  
CPU-only Caffe: Chage CPU_ONLY := 1 flag in Makefile.config </br>  


### Step2: Prepare Dataset
Get the expression profile of isoforms and genes.</br>
Get GO annotation for gene. </br>
Get go-basic.obo file to get DAG of GO terms. 

### Step3: Run DeepIsoFun
Run the script file ./run.sh
