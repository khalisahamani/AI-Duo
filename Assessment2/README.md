# Assessment 2

This folder contains all files and documentation for Assessment 2.

Model: Qwen2.5-Math-1.5B on Hendrycks Math Dataset

This project focuses on the `Qwen/Qwen2.5-Math-1.5B` large language model using the `EleutherAI/hendrycks_math` dataset from Hugging Face. The objective of this project is to improve the model’s mathematical reasoning capability in solving olympiad-style math problems through parameter-efficient fine-tuning techniques.

The project combines multiple mathematical subjects including algebra, geometry, number theory, prealgebra, precalculus, intermediate algebra and counting & probability into a single dataset for training. The dataset was preprocessed into a structured prompt-and-solution format to help the model learn step-by-step mathematical reasoning.

To reduce GPU memory usage and enable efficient training, 4-bit quantization using BitsAndBytes was implemented together with LoRA (Low-Rank Adaptation) fine-tuning. The model was trained using Hugging Face Transformers and PEFT libraries on Google Colab.

The trained model was evaluated using unseen test questions from the Hendrycks Math dataset. The evaluation focused on the model’s ability to generate logical step-by-step solutions and accurate final answers.

## Features
- Multi-subject mathematical dataset combination
- Dataset preprocessing and formatting
- 4-bit quantized model loading
- LoRA parameter-efficient fine-tuning
- Step-by-step mathematical reasoning generation
- Automatic answer extraction and evaluation
- Training and validation performance tracking

## Technologies Used
- Python
- PyTorch
- Hugging Face Transformers
- PEFT (LoRA)
- BitsAndBytes
- Google Colab

## Dataset
Dataset source:
```python
EleutherAI/hendrycks_math
