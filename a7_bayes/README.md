# activity 7: Naive Bayes Classifier

## Locally Installed scikit learn

If you have scikit learn installed locally on your machine, you can run Python programs directly
from the terminal, as specified in the sample program. You must be inside the `src` directory.


## Docker

Once you have Docker Desktop running on your machine, you can use Docker to run given
Python programs that use OpenCV.  You must be inside `a7_bayes` directory.


### Building
First run:

`docker build -t sklearn .`


### Running

To run the program in a docker container, run the following command.

`docker run --rm -v $(pwd)/src:/root sklearn python bayes_classifier.py`

### Output

The output of this program is stored in the `src` directory.
