import argparse
from glob import glob
import os
import random

import numpy as np

from utils import get_module_logger


def create_symlinks(sources, destination):
    """
    Create symbolic links for files in the specified directory.

    args:
        - sources: a list of file names which the symbolic links will point at
        - destination: destination directory
    """
    os.makedirs(destination, exist_ok=True)

    for source in sources:
        os.symlink(
                os.path.abspath(source),
                os.path.join(destination, os.path.basename(source)))


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved
    to new folders in the same directory. This folder should be named train,
    val and test.

    args:
        - source [str]: source data directory, contains the processed tf
          records
        - destination [str]: destination data directory, contains 3 sub
          folders: train / val / test
    """
    tfrecords = glob(source + '/*.tfrecord')

    train_cnt = int(len(tfrecords) * 0.8)
    val_cnt = min(int(len(tfrecords) * 0.1), len(tfrecords) - train_cnt)

    trains = tfrecords[0:train_cnt]
    vals = tfrecords[train_cnt:train_cnt+val_cnt]
    tests = tfrecords[train_cnt+val_cnt:]

    create_symlinks(trains, os.path.join(destination, 'train'))
    create_symlinks(vals, os.path.join(destination, 'val'))
    create_symlinks(tests, os.path.join(destination, 'test'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)
