# activity 3: Person Detection with HOG and SVM

## Locally Installed OpenCV

If you have OpenCV installed locally on your machine, you can run Python programs directly
from the terminal, as specified in each sample program. You must be inside the `src` directory.


## Docker 

Once you have Docker Desktop running on your machine, you can use Docker to run given
Python programs that use OpenCV.  You must be inside `a3_person-detection` directory.

### Building
First run:

`docker build -t opencv .`

### Running

To run the program in a docker container, run the following command, where `image.png` 
is the image used for detection.
   
`docker run --rm -v $(pwd)/src:/root opencv python detect_multiscale.py --image images/image.png`


### Output

The output of each program is stored in the `images/output` directory.
