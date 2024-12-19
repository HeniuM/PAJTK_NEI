## Project Overview

This project consists of four separate tasks, each addressing a different machine learning problem using neural networks. The tasks are implemented in Python and make use of TensorFlow and Keras for model creation and training. The tasks are structured as follows:

1. **Task 1: Data Classification (CSV-based)** - A neural network model classifies data from a CSV file.
2. **Task 2: Animal Recognition** - A convolutional neural network (CNN) distinguishes between images of a dog and a cat.
3. **Task 3: Clothing Recognition** - A CNN classifies images of clothing items (jacket and trousers).
4. **Task 4: Data Augmentation** - Demonstrates data augmentation techniques to enhance training, with real-time visualization and optional saving of augmented images.

## File Structure

- `task1_csv_classification.py`: Implements Task 1.
- `task2_animal_recognition.py`: Implements Task 2.
- `task3_clothing_recognition.py`: Implements Task 3.
- `task4_data_augmentation.py`: Implements Task 4.
- `seeds_dataset.csv`: CSV file used in Task 1.
- `dog.png`: Image of a dog used in Task 2 and Task 4.
- `cat.png`: Image of a cat used in Task 2.
- `jacket.png`: Image of a jacket used in Task 3.
- `trausers.png`: Image of trousers used in Task 3.
- `image.png`: Example image file used for Task 4 (required for data augmentation).

## Environment Setup

Follow the steps below to set up the environment and run the project:

### Step 1: Install Python

Ensure you have Python 3.8 or later installed on your system. You can download Python from [python.org](https://www.python.org/).

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Required Libraries

Install the necessary Python packages using pip:

```bash
pip install tensorflow numpy pandas scikit-learn matplotlib
```

### Step 4: Verify Installation

Run the following command to verify TensorFlow installation:

```bash
python -c "import tensorflow as tf; print(tf.__version__)"
```

Ensure the output shows the installed TensorFlow version.

### Step 5: Prepare Dataset and Images

Place the following files in the project directory:

- `seeds_dataset.csv`
- `dog.png`
- `cat.png`
- `jacket.png`
- `trausers.png`
- `image.png` (for Task 4)

## Running the Project

Each task can be executed independently by running the respective Python script:

### Task 1: Data Classification

```bash
python task1_csv_classification.py
```

This script trains a neural network to classify data in `seeds_dataset.csv`.

### Task 2: Animal Recognition

```bash
python task2_animal_recognition.py
```

This script trains a CNN to distinguish between images of a dog and a cat and outputs predictions for both images.

### Task 3: Clothing Recognition

```bash
python task3_clothing_recognition.py
```

This script trains a CNN to classify clothing images (jacket and trousers) and outputs predictions for both images.

### Task 4: Data Augmentation

```bash
python task4_data_augmentation.py
```

This script demonstrates data augmentation by generating, displaying, and saving augmented versions of the input image (`image.png`). Make sure the file `image.png` is present in the project directory.

## Notes

- Ensure the `seeds_dataset.csv` file and all images are in the same directory as the scripts.
- Adjust the file paths in the scripts if the files are stored elsewhere.
- Use GPUs if available to speed up training.

## Authors

- Henryk Mudlaff, s26071  
  GitHub: [HeniuM](https://github.com/HeniuM)

- Benedykt Borowski, s20685  
  GitHub: [BenedyktB](https://github.com/BenedyktB)
## Contact

For questions or suggestions, please contact the authors.