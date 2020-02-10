# activity 1: Starting with OpenCV

## Locally Installed OpenCV

If you have OpenCV installed locally on your machine, you can run Python programs directly
from the terminal, as specified in each sample program. You must be inside the `src` directory.


## Docker 

Once you have Docker Desktop running on your machine, you can use Docker to run given
Python programs that use OpenCV.  You must be inside `a2_opencv` directory.

### Building
First run:

`docker build -t opencv .`

### Running

To run each program in a docker container, run the following command, where `program.py` 
is the name of the program.
   
`docker run --rm -v $(pwd)/src:/root opencv python program.py`


### Output

The output of each program is stored in the `images/output` directory.
