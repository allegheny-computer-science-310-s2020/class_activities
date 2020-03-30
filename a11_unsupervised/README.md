# activity 11: Unsupervised Learning, due April 6th, 2020

## Summary

So far in this course we have discussed only supervised learning scenarios, where labeled data
is provided to the learning process. However, when such training data is unavailable, since as we
now realize it is hard to collect adequate data, we can employ other types of learning algorithms.

### Self-supervised learning

Although slightly different definitions exist depend on context, generally self-supervised learning is a technique in
machine learning where the training data is labelled automatically labelled,
removing the requirement for the data to be manually labelled by humans. Autonomous labeling of data is typically
done by using the relationship between different input parameters. Once labels are created, all typical
supervised learning techniques can be applied. Self-supervised learning allows for a fully online learning
process to take place, where models can be trained from scratch and it is well suited for stochastic environments.

For those who are interested to learn more, there is a curated list of [self-learning applications](https://github.com/jason718/awesome-self-supervised-learning). There is also a nice blog about [self-supervised learning in computer vision](https://amitness.com/2020/02/illustrated-self-supervised-learning/).

### Unsupervised learning algorithms

Unsupervised learning is a machine learning technique that does not require one
to supervise the model (no labelled data), instead, it aims to discover information on its own.
Unsupervised  learning is useful to find unknown patterns in data, to find features which can be useful for categorization,
and it largely works with unlabelled data, which is easier to obtain.

There are different types of unsupervised learning. Clustering is a common technique
 when it comes to unsupervised learning. Its goal is to find a pattern or a structure in a collection of uncategorized data.
 After processing the data, clustering algorithms find natural groups, known as clusters, if they exist in the data.
 Each cluster is assigned a number called a `cluster ID`, thus allowing us to represent an entire feature set into its cluster ID. The number of
 clusters is a parameter that can be set in the algorithm. There are various applications for clustering, including
social network analysis, anomaly detection, market segmentation, medical imaging, image segmentation, etc.

## Tasks

1. Readme the Summary above.

2. Read and follow coding examples in the [k_means Clustering](https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html) Chapter.

3. Create `clustering.py` program consisting of programming examples from the chapter above, store this program in the `a9_clustering/src`.

4. Write a reflection on this activity in the `writing/reflection.md` following the prompts given in the reflection document template.
Include the output from the programming examples above inside your reflection document.

## Running example programs

### Colab

You can run the example programs in Colab (click on  "Open in Colab" link), "File", "Download .py"

### Locally Installed scikit learn

If you have scikit learn installed locally on your machine, you can run the Python program directly
from the terminal. You must be inside the `src` directory.

### Docker

Once you have Docker Desktop running on your machine, you can use Docker to run given
Python programs that use OpenCV.  You must be inside `a9_unsupervised` directory.

*Building*

First run:

`docker build -t unsupervised .`

*Running*

Then, to run the program in a docker container, enter the following command in the terminal.

`docker run --rm -v $(pwd)/src:/root unsupervised python clustering.py`

### Deliverables

- `clustering.py` program with all example code from [k-Means Clustering Chapter](https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html).
- `reflection.md` file with answers to the prompted questions and the output from the example code.
