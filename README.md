# Deep Gradient Learning for Efficient Camouflaged Object Detection

PyTorch implementation of our Deep Gradient Network (DGNet).

> **Authors:** 
> [Ge-Peng Ji](https://scholar.google.com/citations?user=oaxKYKUAAAAJ&hl=en),
> [Yu-Cheng Chou](https://scholar.google.com/citations?user=YVNRBTcAAAAJ&hl=en),
> [Deng-Ping Fan](https://dpfan.net/), 
> []

## 1. Preface

- **Introduction.** This repository contains the source code, prediction results, and evaluation toolbox of our Deep Gradient Network, also called DGNet ([arXiv](), [SuppMaterial]()).

> If you have any questions about our paper, feel free to contact me via e-mail (gepengai.ji@gmail.com). 
> And if you are using our our and evaluation toolbox for your research, please cite this paper ([BibTeX](#4-citation)).


## 2. :fire: NEWS :fire:

- [2021/11/17] Create repository.


## 3. Overview

<p align="center">
    <img src="./assest/FeatureVis.pdf"/> <br />
    <em> 
    Figure 1: Visualizations of learned texture features. We observe that the feature under the (a) boundary-based supervision contains diffused noises in the background. 
    In contrast, (b) gradient-based supervision enforces the network focus on the regions where the intensity change dramatically..
    </em>
</p>

<p align="center">
    <img src="./assest/DGNet-Framework.pdf"/> <br />
    <em> 
    Figure 2: Overall pipeline of the proposed DGNet. From the perspective in Figure 1, we present a deep gradient network via explicitly object-level gradient map supervision. The underlying hypothesis is that there is some intensity change inside the camouflaged objects. It consists of two connected learning branches, i.e., context encoder and texture encoder. Then, we introduce the gradient-induced transition (GIT) to collaboratively aggregate the feature that is derived from the above two encoders. Finally, a neighbor connected decoder (NCD) is adopted to generate the prediction.
    </em>
</p>

<p align="center">
    <img src="./assest/BubbleBarFig.pdf"/> <br />
    <em> 
    Figure 3: We present the scatter relationship between the performance weighted F-measure and parameters of all competitors on CAMO-Test.
    These scatters are in various colors for better visual recognition and are also corresponding to the histogram (Right).
    The larger size of the coloured scatter point, the heavier the model parameter.
    (Right) We also report the parallel histogram comparison of model's parameters, MACs, and performance.
    </em>
</p>


## 4. Proposed Framework

### 4.1. Training/Testing

The training and testing experiments are conducted using [PyTorch](https://github.com/pytorch/pytorch) with 
a single GeForce RTX TITAN GPU of 24 GB Memory.

> Note that our model also supports low memory GPU, which means you should lower the batch size.

1. Prerequisites:
  
    Note that DGNet is only tested on Ubuntu OS with the following environments. 
    It may work on other operating systems (i.e., Windows) as well but we do not guarantee that it will.
    
    + Creating a virtual environment in terminal: `conda create -n DGNet python=3.6`.
    
    + Installing necessary packages: [PyTorch > 1.1](https://pytorch.org/), [opencv-python](https://pypi.org/project/opencv-python/)

1. Prepare the data:

    + downloading testing dataset and move it into `./dataset/TestDataset/`, 
    which can be found in [Baidu Drive](https://pan.baidu.com/s/1Gg9zco1rt8314cuemqMFBg) (Password: 3wih), [Google Drive](https://drive.google.com/file/d/1LraHmnmgqibzqpqTi4E4l1O2MTusJjrZ/view?usp=sharing).
    + downloading training dataset and move it into `./dataset/TrainDataset/`, 
    which can be found in [Baidu Drive](https://pan.baidu.com/s/175Xx6SQbN2YE9A_ImtTM5A) (Password: dllm), [Google Drive](https://drive.google.com/file/d/1VLKI5pJdM6p4fW2cBZ_2EnoykbQeAHOe/view?usp=sharing).
    + downloading pretrained weights and move it into `./snapshot/DGNet/Net_epoch_best.pth`, 
    which can be found in this [Baidu Drive]() (Password: ), [Google Drive]().
    + downloading pretrained weights and move it into `./snapshot/DGNet-S/Net_epoch_best.pth`, 
    which can be found in this [Baidu Drive]() (Password: ), [Google Drive]()
    + downloading EfficientNet-B4 weights on ImageNet dataset [Baidu Drive](https://pan.baidu.com/s/1xBC6qiXjC4oSztQNy_1Cmg) (Password: 66so), [Google Drive](https://drive.google.com/file/d/1XrUOmgB86L84JefoNq0gq2scBZjGaTkm/view?usp=sharing).
    + downloading EfficientNet-B1 weights on ImageNet dataset [Baidu Drive](https://pan.baidu.com/s/1ORAVErkwvgqG0J3qX79pLw) (Password: 0wa9), [Google Drive](https://drive.google.com/file/d/1niq1xi5IMdBToyS8kUzoppFIqTYM9kRr/view?usp=sharing)
   
1. Training Configuration:

    + Assigning your costumed path, like `--save_path `, `--train_root` and `--val_root` in `MyTrain.py`.
    + Just enjoy it via run `python MyTrain.py` in your terminal.
    
1. Evaluation Configuration:

    + Assigning your costumed path, like `--gt_root `, `--pred_root`,`--data_lst` and `--model_lst` in `MyEval.py`.
    + Just enjoy it via run `python MyEval.py` in your terminal.

1. Testing Configuration:

    + After you download all the pre-trained model and testing dataset, just run `MyTesting.py` to generate the final prediction map: 
    replace your trained model directory (`--snap_path`).
    
    + Just enjoy it!

### 3.2 Evaluating your trained model:

One-key evaluation is written in MATLAB code `./eval/`, 
please follow this the instructions in `./eval/main.m` and just run it to generate the evaluation results in `./res/`.

### 3.3 Pre-computed maps: 
They can be found in [download link]().


## 4. Citation

Please cite our paper if you find the work useful: 

​    

---

**[⬆ back to top](#0-preface)**
