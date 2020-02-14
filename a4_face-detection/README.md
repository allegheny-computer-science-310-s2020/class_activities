# activity 4: Face and Eye Detection HAAR and Cascade Classifier

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

To run the *face recognition* program in a docker container, run the following command, where `image.png` 
is the image used for detection.
   
`docker run --rm -v $(pwd)/src:/root opencv python FaceRecognition.py --face cascades/haarcascade_frontalface_default.xml --image images/image.png`


To run the *eye tracking* program in a docker container, run the following command, where `video.mov` 
is the video used for tracking.

`docker run --rm -v $(pwd)/src:/root opencv python EyeTracking.py --face cascades/haarcascade_frontalface_default.xml --eye cascades/haarcascade_eye.xml --video video/movie.mov`

### Output

The output of each program is stored in the `images/output` directory.
