# ML baseline scripts

A collection of example jupyter notebooks to showcase how to establish quick baseline models for various problem types in the context of Kaggle competition datasets.
Some problem examples include adverserial attacks, classification, regression, word embeddings, etc. using image, text, and tabular data.  


## Get Started

Clone this repo:
```
git clone https://github.com/smellslikeml/simple_ML_baselines.git
```

Accept rules for contests in the ```competition_lst.txt``` list found in the donwload directory.


Set up the [Kaggle API](https://github.com/Kaggle/kaggle-api), descend into the download directory, and run:
```
python get_kaggle_data.py competition_lst.txt
```
to download the datasets used in these notebooks. This script will create a directory for each competition dataset in the directory where the repo was cloned to.


