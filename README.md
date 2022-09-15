# Object Detection in an Urban Environment

### Project overview

In this project, we try to detect objects in images from Waymo Open Dataset. Object detection is an important component of self driving car systems, because it is the component which allows such systems to understand vehicle surroundings, such as pedestrians and other vehicles from camera observations.

### Set up

I used the Dockerfile in build came with the project material. I built the image with

    docker build -t project-dev -f Dockerfile .

then ran

    docker run --gpus all -v <PATH TO LOCAL PROJECT FOLDER>:/app/project/ --network=host -ti project-dev bash

Some libraries had to be downgraded due to library update, etc. These steps are reflected in Dockerfile.

### Dataset

#### Dataset analysis

From `Exploratory Data Analysis.ipynb`, I noticed the following:

* There are many small objects in the images.
* There are many overlapping objects in the images.
* Bicycles are rare and annotated objects mostly consist of other cars and pedestrians.

#### Cross validation

With `create_splits.py`, I split the dataset into three: training (train), validation (val), test (test). The train set was used for training. The val set was used to compare models.

### Training

#### Reference experiment

    INFO:tensorflow:Eval metrics at step 6000
    I0914 04:49:03.254420 140533609854784 model_lib_v2.py:1015] Eval metrics at step 6000
    INFO:tensorflow:	+ DetectionBoxes_Precision/mAP: 0.000185
    INFO:tensorflow:	+ DetectionBoxes_Precision/mAP@.50IOU: 0.000793
    INFO:tensorflow:	+ DetectionBoxes_Precision/mAP@.75IOU: 0.000033
    INFO:tensorflow:	+ DetectionBoxes_Precision/mAP (small): 0.000021
    INFO:tensorflow:	+ DetectionBoxes_Precision/mAP (medium): 0.003142
    INFO:tensorflow:	+ DetectionBoxes_Precision/mAP (large): 0.005817
    INFO:tensorflow:	+ DetectionBoxes_Recall/AR@1: 0.001257
    INFO:tensorflow:	+ DetectionBoxes_Recall/AR@10: 0.004094
    INFO:tensorflow:	+ DetectionBoxes_Recall/AR@100: 0.015505
    INFO:tensorflow:	+ DetectionBoxes_Recall/AR@100 (small): 0.004171
    INFO:tensorflow:	+ DetectionBoxes_Recall/AR@100 (medium): 0.036900
    INFO:tensorflow:	+ DetectionBoxes_Recall/AR@100 (large): 0.232967
    INFO:tensorflow:	+ Loss/localization_loss: 0.793256
    INFO:tensorflow:	+ Loss/classification_loss: 0.846861
    INFO:tensorflow:	+ Loss/regularization_loss: 1.790260
    INFO:tensorflow:	+ Loss/total_loss: 3.430376

#### Improve on the reference

experiment1:

    INFO:tensorflow:Eval metrics at step 24000
    INFO:tensorflow:	+ DetectionBoxes_Precision/mAP: 0.001881
    INFO:tensorflow:	+ DetectionBoxes_Precision/mAP@.50IOU: 0.008643
    INFO:tensorflow:	+ DetectionBoxes_Precision/mAP@.75IOU: 0.000076
    INFO:tensorflow:	+ DetectionBoxes_Precision/mAP (small): 0.000609
    INFO:tensorflow:	+ DetectionBoxes_Precision/mAP (medium): 0.006674
    INFO:tensorflow:	+ DetectionBoxes_Precision/mAP (large): 0.027453
    INFO:tensorflow:	+ DetectionBoxes_Recall/AR@1: 0.002331
    INFO:tensorflow:	+ DetectionBoxes_Recall/AR@10: 0.007844
    INFO:tensorflow:	+ DetectionBoxes_Recall/AR@100: 0.032448
    INFO:tensorflow:	+ DetectionBoxes_Recall/AR@100 (small): 0.020147
    INFO:tensorflow:	+ DetectionBoxes_Recall/AR@100 (medium): 0.070295
    INFO:tensorflow:	+ DetectionBoxes_Recall/AR@100 (large): 0.109890
    INFO:tensorflow:	+ Loss/localization_loss: 0.897523
    INFO:tensorflow:	+ Loss/classification_loss: 0.710646
    INFO:tensorflow:	+ Loss/regularization_loss: 0.048756
    INFO:tensorflow:	+ Loss/total_loss: 1.656925

experiment2:

    INFO:tensorflow:Eval metrics at step 24000
    INFO:tensorflow:        + DetectionBoxes_Precision/mAP: 0.183033
    INFO:tensorflow:        + DetectionBoxes_Precision/mAP@.50IOU: 0.357934
    INFO:tensorflow:        + DetectionBoxes_Precision/mAP@.75IOU: 0.159025
    INFO:tensorflow:        + DetectionBoxes_Precision/mAP (small): 0.096755
    INFO:tensorflow:        + DetectionBoxes_Precision/mAP (medium): 0.463644
    INFO:tensorflow:        + DetectionBoxes_Precision/mAP (large): 0.818684
    INFO:tensorflow:        + DetectionBoxes_Recall/AR@1: 0.041746
    INFO:tensorflow:        + DetectionBoxes_Recall/AR@10: 0.175257
    INFO:tensorflow:        + DetectionBoxes_Recall/AR@100: 0.257493
    INFO:tensorflow:        + DetectionBoxes_Recall/AR@100 (small): 0.180164
    INFO:tensorflow:        + DetectionBoxes_Recall/AR@100 (medium): 0.539461
    INFO:tensorflow:        + DetectionBoxes_Recall/AR@100 (large): 0.843956
    INFO:tensorflow:        + Loss/localization_loss: 0.317194
    INFO:tensorflow:        + Loss/classification_loss: 0.235581
    INFO:tensorflow:        + Loss/regularization_loss: 0.237745
    INFO:tensorflow:        + Loss/total_loss: 0.790520
