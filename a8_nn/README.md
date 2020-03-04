# activity 8: Neural Network

## Locally Installed Python

If you have Python installed locally on your machine, you can run this Python program directly
from the terminal, as `python nn.py`. You must be inside the `src` directory.


## Docker

Once you have Docker Desktop running on your machine, you can use Docker to run given
Python programs.  You must be inside `a8_nn` directory.


### Building
First run:

`docker build -t nn .`


### Running

To run the program in a docker container, run the following command.

`docker run --rm -v $(pwd)/src:/root nn python nn.py`

### Output

The output of this program is displayed in the terminal.
