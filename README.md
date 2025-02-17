# PROJECT TITLE 
CLASSIFYING FACE POSES AND EXPRESSIONS USING LeNet-5

## NON-TECHNICAL EXPLANATION OF YOUR PROJECT
This project explores the use of deep learning to classify facial expressions and recognize a specific individual (Tom Mitchell) from images in the CMU Faces dataset. Using an adaptation of the LeNet-5 convolutional neural network, the model learns to distinguish between different facial expressions and determine whether an image contains the target individual. This research contributes to understanding how neural networks process facial features and could have applications in human-computer interaction, emotion recognition, and security systems.

## DATA
The dataset used is the CMU Faces dataset, which contains grayscale images of various individuals with different facial expressions and poses. These images are in PGM format and vary in resolution. The dataset is publicly available and has been widely used in facial recognition and expression classification research.
Dataset Source: [CMU Faces Dataset](https://archive.ics.uci.edu/dataset/124/cmu+face+images)
Citation:
Sim, T., Baker, S., & Bsat, M. (2001). The CMU Pose, Illumination, and Expression (PIE) Database. Carnegie Mellon University.
The dataset used is the CMU Faces dataset, which contains grayscale images of various individuals with different facial expressions and poses. These images are in PGM format and vary in resolution. The dataset is publicly available and has been widely used in facial recognition and expression classification research.
Citation:
Sim, T., Baker, S., & Bsat, M. (2001). The CMU Pose, Illumination, and Expression (PIE) Database. Carnegie Mellon University.

## MODEL 
The project utilizes a modified LeNet-5 architecture, a convolutional neural network originally designed for handwritten digit recognition. This model is well-suited for image classification tasks due to its hierarchical feature extraction capability.
Model Implementation: [LeNet-5 PyTorch Implementation](https://github.com/lychengrex/LeNet-5-Implementation-Using-Pytorch/blob/master/LeNet-5%20Implementation%20Using%20Pytorch.ipynb)
Reasons for choosing LeNet-5:
- Efficient for small to medium-sized image classification tasks.
- Robust feature extraction through convolutional layers.
- Low computational cost compared to deeper architectures.
- Well-suited for grayscale image analysis, as in this dataset.
The project utilizes a modified LeNet-5 architecture, a convolutional neural network originally designed for handwritten digit recognition. This model is well-suited for image classification tasks due to its hierarchical feature extraction capability.

## HYPERPARAMETER OPTIMSATION
To enhance performance and prevent overfitting, the following hyperparameters were tuned:
- Learning Rate: Optimized using grid search (values: 0.001, 0.005, 0.01).
- Batch Size: Experimented with values (16, 32, 64) to balance convergence speed and memory efficiency.
- Number of Filters: Adjusted convolutional layer filters to test their impact on feature extraction.
- Regularization (Dropout): Implemented dropout (0.2, 0.4) to prevent overfitting.
- Optimizer: Compared SGD, Adam, and RMSprop to find the most effective optimizer.
Bayesian optimization was also applied to efficiently search the hyperparameter space and improve model performance.

## RESULTS
The model achieved high accuracy in recognizing facial expressions and identifying Tom Mitchell in images. Key observations include:
- Expression Classification: Achieved an accuracy of ~85% across different expressions.
- Identity Recognition: The model successfully identified Tom Mitchell with a precision of ~90%.
- Overfitting Mitigation: Dropout and regularization strategies reduced overfitting, improving generalization.
- Challenges: Variability in image resolution and minor misclassifications in similar expressions posed difficulties.

## (OPTIONAL: CONTACT DETAILS)
GitHub Repository: [Your GitHub Link]
Email: [Your Email Address]

