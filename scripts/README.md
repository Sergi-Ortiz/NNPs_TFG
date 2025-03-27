# __Scripts (`scripts` directory)__
This directory provides the protocol on the several tests used to evaluate que physical adequacy of each model, as well as the code used to perform them. The directory includes:
- **`deformations`**. Tests used assess the qualitative correctness of the interactions via assessing the potential energy surface description for several bond, angle and dihedral deformations. The qualitative shape of the PES for diatomics has also been obtained and discussed.  

- **`gaussian`**. Contains scripts to convert Gaussian output `.log` files to `.xyz` used if a reference structure has been optimized using *ab initio* methods.  

- **`symmetry`**. Tests used to evaluate the physical knowledge of the models, as motivated in the project. These include a variety of systems where translational and rotational invariance has been assessed. Additional systems such as cyclobutadiene and COSAN have been used as a more nuanced systems where a correct description of both interactions and system symmetries is important.   
