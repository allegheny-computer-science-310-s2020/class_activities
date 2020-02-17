# activity 5: Plant Classification using Random Forest Classifier

## This program is incomplete. The implementation of training and testing are missing and to be 
completed as a guided programming activity in class. 

## Locally Installed OpenCV

If you have OpenCV installed locally on your machine, you can run Python programs directly
from the terminal, as specified in each sample program. You must be inside the `src` directory.


## Docker 

Once you have Docker Desktop running on your machine, you can use Docker to run given
Python programs that use OpenCV.  You must be inside `a5_plant-classification` directory.


### Building
First run:

`docker build -t opencv .`


### Running

To run the *plant classification* program in a docker container, run the following command, where `dataset` directory contains plant images and their masks.
   
`docker run --rm -v $(pwd)/src:/root opencv python classify.py --images dataset/images --masks dataset/masks`

### Output

The output of this program is stored in the `src` directory.
