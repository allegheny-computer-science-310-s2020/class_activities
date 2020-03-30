# activity 12: Searching in AI, due April 6th, 2020

## Summary

Searching techniques are an important part of AI as they allow problem-solving goal-oriented agents to find solutions to given problems by achieving a certain goal with a specific input.
Searching is a step by step process to solve a search-problem in a given search space, where a search space represents a set of possible solutions.
In short, searching algorithms identify and find a specific value within a given data structure.
In searching, a problem is formulated first, where we decide what actions and states to consider, given a goal.
A problem can be defined formally by five components:

- _Initial (Start) State_: the state that the agent starts the search.
- _Actions_:  the description of the possible actions available to the agent.
- _Transition model_: the description of what each action does, for example,
it can tell us what state the agent will end up in after taking a specific action from
a particular state. Together, the initial state, actions, and transition model implicitly define the state space
of the problem -- the set of all states reachable from the initial state by any sequence of actions.
- _Goal test_: determines whether a given state is a goal state.
- _A path cost_: the function that assigns a numeric cost to each path. The problem-solving
agent chooses a cost function that reflects its own performance measure.

For example, in the vacuum cleaning example we discussed during week 2, shown below,
these components are defined as:

![vacuum cleaner example][vacuum.png]

- States: The state is determined by both the agent location and the dirt locations. The
agent is in one of two locations, each of which might or might not contain dirt. Thus,
there are 2 * 2^2 = 8 possible world states.
- Initial state: Any state can be designated as the initial state.
- Actions: In this simple environment, each state has just three actions: Left, Right, and
Suck. Larger environments might also include Up and Down.
- Transition model: The actions have their expected effects, except that moving Left in
the leftmost square, moving Right in the rightmost square, and Sucking in a clean square
have no effect. The complete state space is shown in the figure below.
![vacuum][state_space.png]
- Goal test: This checks whether all the squares are clean.
- Path cost: Each step costs 1, so the path cost is the number of steps in the path.

_Search tree_ is a tree representation of search problem, where the root of the search tree is the root node which is corresponding to the initial state.
_Solution_ is an action sequence which leads from the start node to the goal node, and an _Optimal Solution_ is a solution that has the lowest cost among all solutions.

Different categories of searching algorithms exist, as described below.

- _Uninformed search strategies (blind search)_:  strategies that have no additional  information about states beyond that provided in the problem definition. All they can do is
generate successors and distinguish a goal state from a non-goal state. All search strategies
are distinguished by the order in which nodes are expanded. Algorithms such as breadth-first search and depth-first search belong to this category. 
You are not required to learn how these specific algorithms work for this course, this content is covered in CMPSC 202.

- _Informed search (heuristic search)_:  strategies that know whether one non-goal state is "more promising" than another.
Informed strategies consider quantitative values such as heuristics while searching, and thus make more informed decisions regarding the next step to take.
A node's _heuristic value_ is an estimated cost of the cheapest path from the state at node n to a goal state.
While other algorithms guarantee to find a path from the initial node to a goal state, optimal search algorithms are the only ones that can guarantee to find a solution with the shortest path from start to goal. A* algorithm is one such algorithm and is the topic of your hands-on exploration.

### A* Algorithm
A* search (pronounced "A-star search") evaluates nodes by combining the cost to reach the node (denoted as g(n)) and the cost
to get from the node to the goal (denoted as h(n)).
Since g(n) (the cost to reach the node) gives the path cost from the start node to node n, and h(n)
(the cost to get from the node to the goal) is the estimated cost
of the cheapest path from n to the goal, we have an estimated cost of the cheapest solution through n, typically denoted by f(n).
Thus, if we are trying to find the cheapest solution, a reasonable thing to try first is the
node with the lowest value of g(n) + h(n).

## Tasks

1. Read the Summary above.

2. Read the README in the [A* search repository](https://github.com/LogicJake/A-star-search). Clone and run the example if possible.
This program uses _pygame_ to demonstrate an implementation of the A* algorithm on the problem of finding
a shortest path. Once launched you need to click on the blocks in the environment to set up the initial and goal states,
and the obstacles. You must enter the space button to proceed to the next step in this program.
Do not worry about how the cost (numbers inside the states) are calculated. Instead, pay attention
to the general working strategy of the algorithm via this visualization. If you are able to run this example,
try out different types of environment (easy, hard, ones with no path from start to goal) and see how
algorithm performs under each one.

3. Write a reflection on this activity in the `writing/reflection.md` following the prompts given in the reflection document template.

## Running example programs

### Locally Installed Python

After cloning the [A* search](https://github.com/LogicJake/A-star-search) repository, run `pip install -r requirements.txt` to install _pygame_. Then, to run the program type `python main.py`.

### Docker

Docker set up is not available for this visual demonstration. In addition to Python, you only need to have
_pygame_ installed, which can be done with `pip install pygame`.

### Deliverables

- `reflection.md` file with answers to the prompted questions and the output from the example code. If you are not able to run the example program, answer the questions the best you can from your observations of the example run of the program provided in the [A* search](https://github.com/LogicJake/A-star-search) repository.
