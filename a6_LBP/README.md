# activity 6: Pattern Classification with Local Binary Patterns

## Locally Installed OpenCV

If you have OpenCV installed locally on your machine, you can run Python programs directly
from the terminal, as specified in each sample program. You must be inside the `src` directory.


## Docker

Once you have Docker Desktop running on your machine, you can use Docker to run given
Python programs that use OpenCV.  You must be inside `a6_LBP` directory.


### Building
First run:

`docker build -t opencv .`


### Running

To run the program in a docker container, run the following command.

`docker run --rm -v $(pwd)/src:/root opencv python recognize.py --training images/training --testing images/testing`

### Output

The output of this program is stored in the `src` directory.
