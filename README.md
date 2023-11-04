# Code for KTC2023 EIT challenge (Plug&Play approach + post-processing)


## Brief description of the algorithm
This repository contains the Python files required by the organisers of the EIT Kuopio challenge 2023 which implements a Plug&Play approach with a post-processing step where synthetic (data-independent) masks are superimposed on the obtained reconstruction to improve results.
Training was performed with GT simulated data with random polygons of different shapes and postive/negative contrast to simulate resistive/conductive inclusions.
Associated noisy versions were computed running a regularised Gauss-Newton algorithm (on meshes) for few (5) iterations on the corresponding measurements simulated using the forward model provided.


## Authors:
- Tatiana Bubba, University of Bath, UK, tab73'at'bath.ac.uk
- Luca Calatroni, CNRS, FR, calatroni'at'i3s.unice.fr
- Damiana Lazzaro, University of Bologna, IT, damiana.lazzaro'at'unibo.it 
- Serena Morigi, University of Bologna, IT, serena.morigi'at'unibo.it 
- Luca Ratti, University of Bologna, IT, luca.ratti5'at'unibo.it
- Matteo Santacesaria, University of Genoa, IT, matteo.Santacesaria'at'unige.it 
- Julian Tachella, CNRS, FR, julian.tachella'at'ens-lyon.fr

## Installation instructions and requirements

For installation and required environment see the environment_pnp.yml to restore the conda enviroment used for the submission. 
You can create the enviroment using the following command:

```conda env create -f environment.yml```

We created a script main.py to reconstruct the inclusions provided for training from voltage measurements:

```python main.py /path_to_input_folder /path_to_ouput_folder difficulty_level```

For the denoiser, the learned weights are stored in the file
``` weights_denoiser.pth```


## Reference work: 
* Francesco Colibazzi, Damiana Lazzaro, Serena Morigi, Andrea Samoré. Deep-plug-and-play proximal Gauss-Newton method with applications to nonlinear, ill-posed inverse problems. Inverse Problems and Imaging, 2023, 17(6): 1226-1248. doi: 10.3934/ipi.2023014
* Francesco Colibazzi, Damiana Lazzaro, Serena Morigi, Andrea Samoré. Learning Nonlinear Electrical Impedance Tomography. J Sci Comput, 2022, 90(58). https://doi.org/10.1007/s10915-021-01716-4
