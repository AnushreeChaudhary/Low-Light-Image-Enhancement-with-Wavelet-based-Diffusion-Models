# Low-light Image Enhancement with Wavelet-based Diffusion Models [[Paper]](https://arxiv.org/pdf/2306.00306.pdf).
<h4 align="center">Anushree Chaudhary</center>

## Pipeline
![](./Figures/pipeline.png)

## Dependencies
These dependencies should show no error for python=3.12.4. You may try to loosen the version constraints if compatibility issues arise.
```
pip install -r requirements.txt
````

## Download the raw training and evaluation dataset
### Paired dataset
You can find the dataset used here. Some modifications might have to be made according to your environment.
LOLv1 dataset: Chen Wei, Wenjing Wang, Wenhan Yang, and Jiaying Liu. "Deep Retinex Decomposition for Low-Light Enhancement", BMVC, 2018.  [[Google Drive]](https://drive.google.com/file/d/1It291IA2DVi8k2YZ-G0d1cGm301Tsi7r/view?usp=sharing)


## Pre-trained Model
Pre-trained model is available for download here: [[Google Drive]](https://drive.google.com/file/d/1f4zDvPsWKrID33OJdeHwc5VOBILkm0KW/view?usp=sharing)

## How can you train the model?
Ensure that the file paths are mentioned correctly in the configuration file.
```
python train.py  
```

## How can you test the model?
```
python evaluate.py
```


## Acknowledgement
The code is mainly adapted from the official work on this paper: [DiffLL](https://github.com/JianghaiSCU/Diffusion-Low-Light). I thank the authors for their contributions.
