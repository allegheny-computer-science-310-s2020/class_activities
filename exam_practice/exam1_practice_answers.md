# CMPSC 310 Exam 1 Information and Practice Answers To Some Questions
# Name:

## Exam Information
The first exam will be held during the class session on Monday, March 2 at 11:00 am.
The exam will be available via GitHub Classroom and must be submitted through each student's `exam1` repository.
The exam will be open book and notes, including your class notes, my class notes and hand outs, but you can not use anything that has been printed from the Web or access anything through the Web during the exam, other than the course Website and the course GitHub repositories.

This exam may include questions on the material covered since the beginning of the semester through February 26. The slides should be a good study guide for the material that you are responsible for. In the addition to the content covered on the slides, you should also be comfortable using the tools and programs explored in class and labs 1-2.

## Exam Format
The exam will consist of ten questions consisting of a mixture of the following types of questions:
* Multiple choice
* Short answer (provide 2-3 sentence explanation and give an example)
* Problem solving (given a stated problem, find a solution)
* Output analysis (given an output of a program, explain its meaning)

## Material (aka Things to Know)
* What is AI? Connections to other disciplines and philosophical implications behind AI.
* What is an agent? A rational agent?
* Different types of agents.
* Types of environments.
* PEAS.
* Overview of Computer Vision.
* OpenCV: basic image operations.
* Learning Overview.
* Classification problem: SVM, Decision Trees, Random Forests. 
* General understanding of cascades.
* Object/face detection/recognition.
* Probability terminology and basic probability problems.
* Bayes Rule and Naive Bayes algorithm.

## Note: The remainder of this document contains practice questions for the first exam. It does not represent questions over all concepts that maybe covered during the exam. You are responsible for all material covered in class so far. Some answers are provided below.


### Question 1 (put X inside the appropriate brackets)

A reflex agent is an agent that:
- [ ] Builds a model of the environment and uses it to map percepts to actions
- [ ] Builds a model of the environment and uses it to reach a desirable state towards the goal
- [ X] Simply maps percepts to actions
- [ ] Builds a model of the environment and adapts it through learning


### Question 2

RoboCup is an annual international robotics competition that aims to promote robotics and AI research by offering a publicly appealing, but formidable challenge.

1. Consider a task of designing autonomous soccer playing robot. Specify the PEAS description of this task environment.

*Sample answer*:

Performance Measure - Number of goals, possession, number of fouls made, tackling capability
Environment - Indoor soccer arena, humans, robots
Actuators - vision, limb movement (walking / running), kicking, hearing, speaking
Sensors - vision sensors, depth sensor, sound sensors, speed sensors

2. Classify the task environment of this robot (e.g., observable, multi-agent, stochastic, sequential, dynamic, discrete). State any assumptions you are making.

Answer will largely depend on the assumptions made.

### Question 3

Based on the class discussions, readings and your preliminary understanding of "intelligence", provide one argument with justification (1-2 sentences) for and one argument against the following statement: "Intelligent machines can be ethical".


### Question 4

When an alligator is hungry, the probability that it will eat is 0.9 (why not 1? it depends on the food - alligators don't care for, e.g., warmed-over tuna casserole). On the other hand, if the gator is not hungry, there is still a 0.3 probability that it will eat (some foods are irresistible - gators are particularly fond of hot fudge sundaes). At any given time there is a 50% chance that an alligator will be hungry. Final numerical answer is not required, show the steps is sufficient.

1. What is a sample space for this problem?

The sample space for this problem is whether the alligator eats or not and whether its hungry or not.

2. What is the probability of gator being not hungry?

P(Gator not hungry) = 1 - P(gator hungry) = 1 - 0.5 = 0.5

3. You have just observed a gator eating lunch (it devoured a Big Mac and some fries). What is the probability that it was hungry before it ate?

Let E stand for "Alligator eats", let H stand for "Alligator
was hungry." We know:
P(E | H) = 0.9
P(E | not H) = 0.3
P(H) = 0.5

We wish to compute P(H | E). By Bayes' rule, this is:
P(H | E) = (P(H) * P(E | H)) / (P(H) * P(E | H) + P(not H) * P(E | not H)) = 0.5 * 0.9 / (0.5*0.9 + 0.5*0.3) = 0.75

### Question 5

Describe a sequence of computer vision functions one may utilize on images before applying some "intelligent" task (e.g., learning) on them. You must describe at least two functions. Provide explanation of and justification for the need of each one.

### Question 6

Consider the problem faced by a person learning to play tennis (or some other sport that you are familiar with). Explain how this process fits into the learning model. Describe the percepts and actions of the person, and the types of learning the person must do. What type of learning is it (supervised, unsupervised, reinforcement)?

The requisite skills can be divided into movement, playing strokes, and strategy. The environment consists of the court, ball, opponent, and one?s own body. The relevant sensors are the visual system and the sense of forces on and position of one?s own body parts. The actuators are the muscles involved in moving to the ball and hitting the stroke. The learning process could involve both supervised learning and reinforcement learning. Supervised learning occurs in acquiring the predictive transition models, e.g., where the opponent will hit the ball, where the ball will land, and what trajectory the ball will have after one?s own stroke (e.g., if I hit a half-volley this way, it goes into the net, but if I hit it that way, it clears the net). Reinforcement learning occurs when points are won and lost?this is particularly important for strategic aspects of play such as shot placement and positioning (e.g., in 60% of the points where I hit a lob in response to a cross-court shot, I end up losing the point). In the early stages, reinforcement also occurs when a shot succeeds in clearing the net and landing in the opponent?s court. Achieving this small success is itself a sequential process involving many motor control commands, and there is no teacher available to tell the learner?s motor cortex which motor control commands to issue.

### Question 7

Assume we are using `hog.detectMultiScale` function of OpenCV.

1. What is `hog`? How is it used in computer vision learning?

HOG stands for Histogram of Oriented Gradients. It is a feature extractor which can be used to get different features from an image based on the gradients present in a picture. It can be used in combination with a classifier for image recognition.

2. One of the parameters of the `detectMultiScale` function is `winStride`. What does this parameter represent? Comment on the effect of the value of this parameter on the performance of the learning task.

`winStride` represents a square window that slides through the image. The portion of the image that falls under that window has its features extracted and classified. If we use a smaller window, the performance takes a hit since it takes a longer time for the window to slide through the entire image. However, with a smaller window, more features can be detected properly, improving the accuracy. Conversely, with a larger winStride, the performance increases but the accuracy falls. 

### Question 8

Identify *two* model performance metrics in the `metrics` subpackage in scikit-learn. Explain what each of these metrics is evaluating.


### Question 9

In 5-fold cross validation, what does the number 5 represent?


### Question 10

What can you tell about the performance of Naive Bayes Classifier from the image below?
![alt text](heatmap.png)
