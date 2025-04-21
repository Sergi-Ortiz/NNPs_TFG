# __Machine Learning Neural Network Potentials__
This repository contains all the documentation, protocol, models and code regarding the study of different Machine Learning Neural Network Potential (ML-NNP) models in the context of Chemistry and Physics for the physics bachelor's thesis project at Universitat Autònoma de Barcelona (Treball de Fi de Grau de Física). For inquiries regarding the project, feel free to reach out at sergi.ortizr@autonoma.cat. 

The aim of this project is two-fold and involves the use of several pretrained ML-based interatomic potentials to assess how the fundamental physics knowledge of each model affects its predictions. First, we aim to study the qualitative description of the interactions for several systems. Second, the models' limitations in the prediction of atomic interactions are discussed according to what physics are understood by the models, the training dataset, molecular descriptors and architecture used, hopefully providing a solid foundation and the necessary insight to interpret their predictions, ultimately making the models more transparent and interpretable. 

# __Project structure__
The project is structured in four different parts, with each part building on the concepts from the previous ones. First, a general introduction provides context regarding atomic modeling, electronic structure and general deep learning, which are key concepts to understand the bulk of the project. Next, the NNP models (object of study) are presented in detail. Thirdly, a set of tests especially motivated to assess the physical adequacy of the models are introduced, and the results are discussed and compared. Finally, the future perspectives on the state-of-the-art are discussed to provide an overview on this rapidly moving field. 

## __Introduction__
The introduction is organized in three related sections, including atomic modeling basics, a deep learning introduction and a motivation for this project based on Physics Informed Neural Networks (PINNs).  
- **Atomic modeling basics**
  - *From the Schrödinger equation to classical interatomic potentials.*  Overview of how to model systems and the level of detail tradeoff. Schrödinger equation and electronic structure methods. Necessity of a simple functional form to represent atomic interactions. Classical Force Fields (FFs) and how ML could provide *ab initio* quality at cheaper computational cost. 
- **Deep learning introduction**
  - *Structure of a DL model*. Basic Deep Learning concepts, an introduction to the fully-connected multi-layer perceptron (MLP), Graph Neural Networks (GNNs) (and Message Passing Neural Networks). 
- **PINNs**
  - Motivational example on how the physical adequacy is imperative when using ML to model for a physical task. 

## __Models studied__
A practical introduction to all the models used, regarding how to install and use them within `ASE` is provided in the `models` directory, as well as a brief introduction to using `ASE`. A theoretical introduction regarding model architecture and more technical aspects can be found in the paper `project_v0.pdf`, especially in the several appendices included. Three main aspects are considered.
- **Model selection**
  - *Introduction to the NNP models*. Atomic descriptors and approximations used in model input. Architecture choices. Model comparison.


## __Assessing physical adequacy__
Once the models have been introduced, a computational protocol consisting of a series of tests have been designed to evaluate the qualitative correctness of the predicted interactions and their limitations regarding the physics contemplated by each model. The tests and discussion can be found in the `project_v0.pdf` provided, with the code and exact protocol in `scripts` directory.
- **Experimental procedure**
  -  *Understanding the physical adequacy*. Construction of tests to assess translational, rotational and permutation invariance.  Assessment of chemical environment description quality: effect of cutoff distance and molecular descriptors used. Many-body correlations and lack of long-range interactions.
  -  *Model systems*. List and motivation of the systems used for each test.
  -  *Protocol*. Code used to compare all models systematically within the `ASE`.
- **Interpretation and discussion**
  -  Interpretation of the results in the context of the the model selection. Discussion and interpretation of results.
 
## __State of the art and future of the field__
A brief last section provides an end to the project explaining what implications NNPs have in areas such as medicinal chemistry, computational chemistry of biological systems, and materials science and the aspects that require still some work to further increase the applicability of these models in science. 


# __Citation__
If you use or want to reference this work, use 
```bibtex
@phdthesis{NNPs_TFG,
  title        = {Study of the physical adequacy of Machine Learning Potentials},
  author       = {Sergi {Ortiz Ropero}},
  year         = 2025,
  month        = {July},
  note         = {Available at \url{https://github.com/Sergi-Ortiz/NNPs_TFG/project.pdf}},
  school       = {Universitat Autònoma de Barcelona},
  type         = {BSc Thesis}
}
```
