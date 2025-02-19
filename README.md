[![DOI](https://zenodo.org/badge/306959618.svg)](https://zenodo.org/badge/latestdoi/306959618)
# Nicholson-Prinz-JOV-DNNs-bio-vis

Code for the paper:    
"Could simplified stimuli change how the brain performs visual search tasks? A deep neural network study"
https://jov.arvojournals.org/article.aspx?articleid=2778890  

## Installation
Experiments were run in an environment created with [`conda`](https://docs.conda.io/en/latest/) on Ubuntu 16.04.

There are two main dependencies:  
* the [`visual-search-nets` package](https://github.com/NickleDave/visual-search-nets)
* [`jupyterlab`](http://jupyterlab.io/)

A similar environment can be created with `conda` on Ubuntu using the `spec-file.txt` in this repository as follows:

```console
$ git clone https://github.com/NickleDave/Nicholson-Prinz-2021.git
$ cd Nicholson-Prinz-2021
$ conda create --name Nicholson-Prinz-2021 --file spec-file.txt
```

You may also be able to create a suitable environment on other linux platforms using the `environment.yml` file.

```console
$ git clone https://github.com/NickleDave/Nicholson-Prinz-JOV-DNNs-bio-vis
$ cd Nicholson-Prinz-JOV-DNNs-bio-vis
$ conda env create -f environment.yml

```

## Acknowledgements
- Research funded by the Lifelong Learning Machines program, 
DARPA/Microsystems Technology Office, 
DARPA cooperative agreement HR0011-18-2-0019
- David Nicholson was partially supported by the 
2017 William K. and Katherine W. Estes Fund to F. Pestilli, 
R. Goldstone and L. Smith, Indiana University Bloomington.

## Citation
If you use / adapt this code, please cite its DOI:  
[![DOI](https://zenodo.org/badge/306959618.svg)](https://zenodo.org/badge/latestdoi/306959618)
