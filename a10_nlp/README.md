# activity 8: NLP Tasks

## Locally Installed NLTK

If you have `nltk` installed locally on your machine, you can run these Python programs directly
from the terminal, as `python sentiment.py`. You must be inside the `src` directory.


## Docker

Once you have Docker Desktop running on your machine, you can use Docker to run given
Python programs.  You must be inside `a10_nlp` directory.


### Building
First run:

`docker build -t nlp .`


### Running

To run the program in a docker container, run the following command.

`docker run --rm -v $(pwd)/src:/root nlp python sentiment.py`

OR

`docker run --rm -v $(pwd)/src:/root nlp python parsing.py`

### Output

The output of this program is displayed in the terminal.
