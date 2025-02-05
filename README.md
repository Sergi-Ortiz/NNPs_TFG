# __Machine Learning Neural Network Potentials__
This repo contains all the documentation, protocol, models and code regarding the study of different ML-NNP models in the context of Chemistry and Physics for the physics bachelor's thesis project (Treball de Fi de Grau de Física). For any questions, feel free to reach out at sergi.ortizr@autonoma.cat. 

The aim of this project is to use different pretrained ML-based interatomic potentials to assess what physics a Neural Network Potential (NNP) has learnt during training, examining the molecular descriptors, dataset and model architecture used to gain insight on the predictions, hopefully making these models more interpretable and transparent. 

# __Project structure__
The project is structured in four different parts, each building on the concepts stated in previous parts. First, a general introduction provides context regarding atomic modeling, electronic structure and general deep learning, which are key concepts to understand the bulk of the project. Next, the NNP models (objects of study) will be presented in detail, as well as the tests, systems and protocols used to compare and assess the physics learnt by each NNP. The results of each test will be interpreted and discussed. Thidrly, a motivated showcase of the NNP models will be presented with different key examples, to support the bulk of the project and give a more practical view on the topic. Finally, the future perspectives on the state-of-the-art will be discussed to provide a bit of context on this rapidly moving field. 

## __Introduction__
The introduction is organized in three related sections, including atomic modeling basics, a deep learning introduction and a motivation for this project based on Physics Informed Neural Networks (PINNs).  
- **Atomic modeling basicss**
  - *From the Schrödinger equation to classical interatomic potentials.*  Overview of how to model systems and the level of detail tradeoff. Schrödinger equation and electronic structure methods. Necessity of a simple functional form to represent atomic interactions. Classical FFs and how ML could provide more accurate FFs (of potentially *ab initio* quality) at classical FF cost. 
- **Deep learning introduction**
  - *Structure of a DL model*. Importance of the dataset, dataset preprocessing, model definition and training (optimization, regularization techniques). Importance of generalization of an ML model. Introduction to the fully-connected multi-layer perceptron (MLP) and Message Passing Neural Networks (MPNNs) in the context of graph neural networks (GNNs). 
- **PINNs**
  - Motivational example on how a model can learn the basic physics behind a system from a trajectory, and how these models have been used to infer the physics of a system which trajectory has been observed but the interactions have not been modeled. 

Check `introduction` directory for more info. 

## __Bulk of the project__
The main chunk of the project is organized in three distinct sections, including a model selection, an experimental procedure and an interpretation and dicussion sections. 
- **Model selection**
  - *Introduction to the NNP models*. Atomic descriptors and approximations used in model input. Architecture choices. Model comparison.
- **Experimental procedure**
  -  *Understanding the basic physics learnt*. Construction of tests to assess translational, rotational and permutation invariance.  Assessment of chemical environment description quality: effect of cutoff distance and molecular descriptors used. Tests of many-body correlation between $N$-neighbors. Lack of long-range interactions.
  -  *Model systems*. List and motivation of the systems used for each test
  -  *Protocol*. Code used to fairly compare each model systematically within the ASE (atomic simulation environment) package. 
- **Interpretation and discussion**
  -  Interpretation of the results in the context of the the model selection. Discussion.
 
Models, the installation procedure, its properties and relevant references can be found at `models` directory. Note that each model is implemented as a calculator in `ASE`. 

## __Example showcase__
This section provides simple applications of NNPs which allows to discuss the adventages of NNPs and motive the interpretation and discussion of the previous section. 
- **Biaryl torsional barriers**. Example to prove the usefulness of NNPs.
- **[Problematic example]**. Example to prove the dangers of not checking the physical foundation of a system and use a NNP as a *black box*.  
- **[Extra 1]**. TODO

Check `examples` directory for more info. 

## __State of the art and future of the field__
This last section provides an end to the project explaining what implications NNPs will have in areas such as medicinal chemistry, computational chemistry of biological systems, and materials science.

Check the `SOTA` directory for more info. 
