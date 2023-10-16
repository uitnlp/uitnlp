# UITNLP: A Python NLP Library for Vietnamese

## Installation

You can install this package from PyPI using [pip](http://www.pip-installer.org):

```
$ pip install uitnlp
```

## Example

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
from uitnlp import load_word_segmenter
word_segmenter = load_word_segmenter(feature_name='base_sep_sfx')
word_segmenter.segment(texts=['Chào mừng bạn đến với Trường Đại học Công nghệ Thông tin, ĐHQG-HCM.'], pre_tokenized=False, batch_size=4)
```

## Note
This version is currently only for experimental purposes. We will extend it in future work. We have just wrapped the Vietnamese word segmentation method published in the following [our paper](https://link.springer.com/chapter/10.1007/978-981-15-6168-9_33):

    @InProceedings{10.1007/978-981-15-6168-9_33,
      author    = "Nguyen, Duc-Vu and Van Thin, Dang and Van Nguyen, Kiet and Nguyen, Ngan Luu-Thuy",
      editor    = "Nguyen, Le-Minh and Phan, Xuan-Hieu and Hasida, K{\^o}iti and Tojo, Satoshi",
      title     = "Vietnamese Word Segmentation with SVM: Ambiguity Reduction and Suffix Capture",
      booktitle = "Computational Linguistics",
      year      = "2020",
      publisher = "Springer Singapore",
      address   = "Singapore",
      pages     = "400--413",
      abstract  = "In this paper, we approach Vietnamese word segmentation as a binary classification by using the Support Vector Machine classifier. We inherit features from prior works such as n-gram of syllables, n-gram of syllable types, and checking conjunction of adjacent syllables in the dictionary. We propose two novel ways to feature extraction, one to reduce the overlap ambiguity and the other to increase the ability to predict unknown words containing suffixes. Different from UETsegmenter and RDRsegmenter, two state-of-the-art Vietnamese word segmentation methods, we do not employ the longest matching algorithm as an initial processing step or any post-processing technique. According to experimental results on benchmark Vietnamese datasets, our proposed method obtained a better {\$}{\$}{\backslash}text {\{}F{\}}{\_}{\{}1{\}}{\backslash}text {\{}-score{\}}{\$}{\$}F1-scorethan the prior state-of-the-art methods UETsegmenter, and RDRsegmenter.",
      isbn      = "978-981-15-6168-9"
    }