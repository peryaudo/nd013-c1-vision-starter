# Object Detection in an Urban Environment

### Project overview

In this project, we try to detect objects in images from Waymo Open Dataset. Object detection is an important component of self driving car systems, because it is the component which allows such systems to understand vehicle surroundings, such as pedestrians and other vehicles from camera observations.

### Set up

I used the Dockerfile in build came with the course material. I built the image with

    docker build -t project-dev -f Dockerfile .

then ran

    docker run --gpus all -v <PATH TO LOCAL PROJECT FOLDER>:/app/project/ --network=host -ti project-dev bash

Some libraries had to be downgraded due to library update, etc. These steps are reflected in Dockerfile.

In the Docker image, I ran the following to download the dataset:

    python download_process.py --data_dir /app/project/data

Then after implementing create_splits.py, I ran the following to split data.

    mkdir /app/project/split
    python create_splits.py --source /app/project/data /app/project/split

For training and evaluation, I followed the instruction of the course material.

### Dataset

#### Dataset analysis

In `Exploratory Data Analysis.ipynb`, I first visualized annotations in 10 random images in the dataset:

![visualization of annotations](eda1.png)

From visualized annotations, I could tell the following:

* The majority of objects are cars.
* There are many small objects in the images.
* There are many overlapping objects in the images.
* I didn't see any bicycles in the visualization of 10 images.

Then I visualized distribution of classes of 50 random images:

![visualization of class distributions](eda2.png)

From the pie chart, I could confirm quantitatively that the impressions are correct: the majority of objects are cars and bicycles are very rare.

Then I visualized the distribution of bounding box sizes:

![visualization of bounding box sizes](eda3.png)

From the histogram, it became clear that actually the majority of bounding boxes has less than 5% area of the entire image.

#### Cross validation

With `create_splits.py`, I split the dataset into three: training (train), validation (val), test (test). The train set was used for training. The val set was used to compare models.

### Training

#### Reference experiment



| Metrics Name                          | Value    |
| ------------------------------------- | -------- |
| DetectionBoxes_Precision/mAP          | 0.049726 |
| DetectionBoxes_Precision/mAP@.50IOU   | 0.105540 |
| DetectionBoxes_Precision/mAP@.75IOU   | 0.042007 |
| DetectionBoxes_Precision/mAP (small)  | 0.021489 |
| DetectionBoxes_Precision/mAP (medium) | 0.130668 |
| DetectionBoxes_Precision/mAP (large)  | 0.271001 |
| DetectionBoxes_Recall/AR@1            | 0.016680 |
| DetectionBoxes_Recall/AR@10           | 0.058279 |
| DetectionBoxes_Recall/AR@100          | 0.110761 |
| DetectionBoxes_Recall/AR@100 (small)  | 0.068510 |
| DetectionBoxes_Recall/AR@100 (medium) | 0.236955 |
| DetectionBoxes_Recall/AR@100 (large)  | 0.432967 |
| Loss/localization_loss                | 0.533029 |
| Loss/classification_loss              | 0.546793 |
| Loss/regularization_loss              | 0.453309 |
| Loss/total_loss                       | 1.533131 |

#### Improve on the reference

experiment1:

| Metrics Name                          | Value    |
| ------------------------------------- | -------- |
| DetectionBoxes_Precision/mAP | 0.001881 |
| DetectionBoxes_Precision/mAP@.50IOU | 0.008643 |
| DetectionBoxes_Precision/mAP@.75IOU | 0.000076 |
| DetectionBoxes_Precision/mAP (small) | 0.000609 |
| DetectionBoxes_Precision/mAP (medium) | 0.006674 |
| DetectionBoxes_Precision/mAP (large) | 0.027453 |
| DetectionBoxes_Recall/AR@1 | 0.002331 |
| DetectionBoxes_Recall/AR@10 | 0.007844 |
| DetectionBoxes_Recall/AR@100 | 0.032448 |
| DetectionBoxes_Recall/AR@100 (small) | 0.020147 |
| DetectionBoxes_Recall/AR@100 (medium) | 0.070295 |
| DetectionBoxes_Recall/AR@100 (large) | 0.109890 |
| Loss/localization_loss | 0.897523 |
| Loss/classification_loss | 0.710646 |
| Loss/regularization_loss | 0.048756 |
| Loss/total_loss | 1.656925 |

experiment2:

| Metrics Name                          | Value    |
| ------------------------------------- | -------- |
| DetectionBoxes_Precision/mAP | 0.183033 |
| DetectionBoxes_Precision/mAP@.50IOU | 0.357934 |
| DetectionBoxes_Precision/mAP@.75IOU | 0.159025 |
| DetectionBoxes_Precision/mAP (small) | 0.096755 |
| DetectionBoxes_Precision/mAP (medium) | 0.463644 |
| DetectionBoxes_Precision/mAP (large) | 0.818684 |
| DetectionBoxes_Recall/AR@1 | 0.041746 |
| DetectionBoxes_Recall/AR@10 | 0.175257 |
| DetectionBoxes_Recall/AR@100 | 0.257493 |
| DetectionBoxes_Recall/AR@100 (small) | 0.180164 |
| DetectionBoxes_Recall/AR@100 (medium) | 0.539461 |
| DetectionBoxes_Recall/AR@100 (large) | 0.843956 |
| Loss/localization_loss | 0.317194 |
| Loss/classification_loss | 0.235581 |
| Loss/regularization_loss | 0.237745 |
| Loss/total_loss | 0.790520 |