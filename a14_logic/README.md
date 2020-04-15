# activity 14: Logic and Future of AI, due April 22nd, 2020 by midnight

## Summary

So far in this course, we discussed concepts surrounding agents, their environments and types,
looked at problem solving and planning, use of probability, and learning from data and modeling.
This activity covers a brief look into a subfield of AI called knowledge representation and reasoning (also known as *symbolic AI*).
The goal of the activity is to make you aware of this subfield and what potential it might have for the future of AI.

Most of the work in AI until 1980s involved logic (rule-based reasoning). This is a way researchers have represented human reasoning in AI.
Although learning from data (machine learning) is "hot" today it lacks aspects that were "easy" in the logic-based
systems (for example, allowing the developer to easily communicate their knowledge to the AI system).

### Background

The goals of logic are to represent the knowledge about the world and to reason with that knowledge.
For example, in a natural language, **knowledge** might be:
- A *dollar* is better than a *quarter*.
- A *quarter* is better than a *dime*.

Then, **reasoning** might be:
- Therefore, a *dollar* is better than a *dime*.

A logical system typically comprises of syntax, semantics and reasoning. Propositional logic is one way
to represent reasoning in AI, where symbols are connected by logical connectives (AND, OR, NOT, etc.) to form rules.
Syntax provides symbols (variables), semantics is produced by a model (not the same as "model" in machine learning), and propositional
logic is simply an assignment to all variables.

For example, let's say we have variables "Rainy", "Sunny" and "Cloudy". And, the
knowledge base is:
- Rainy OR Sunny OR Cloudy
- Rainy implies Cloudy AND NOT Sunny
- Cloudy implies NOT Sunny

The developer has the power of adding the knowledge into the knowledge base.  
Then, various models for this knowledge base exist, for example one model is {R=1, S=0, C=1} indicating a rule that it can be rainy and cloudy but not sunny at the same time. Then, questions can be answered using this knowledge base and certain statements can be proven or disproven. Obviously, this is a primitive example, with more rules the system can become more realistic but very complex.

Two types of reasoning have been commonly used to make conclusions based on the information in the knowledge base: inductive and deductive reasoning. Besides these two types, other types of reasoning exist as well.

*Deductive reasoning* deduces new information from logically related known information. It is also known as a top-down reasoning, contradictory to inductive reasoning. In deductive reasoning, the argument's conclusion must be true when the premises are true.
Deductive reasoning is a type of propositional logic in AI, it requires various rules and facts.  Deductive reasoning mostly starts from the general premises to the specific conclusion. For example, premises could be:
- All computer science faculty wear glasses.
- JJ is a computer science faculty.

Then, the conclusion would be: JJ wears glasses.

Unlike, deductive reasoning, *inductive reasoning* arrives at a conclusion using limited sets of facts by the process of generalization. It starts with the series of facts/data and reaches a general statement/conclusion. Inductive reasoning is a type of propositional logic, which is also referred to as bottom-up reasoning or cause-effect reasoning.
In inductive reasoning, premises provide probable supports to the conclusion, so the truth of premises does not guarantee the truth of the conclusion.
For example, a premise could be: All of the Uber drivers we have seen/used are male. Then, the conclusion would be: Therefore, we expect all Uber drivers to be male.

Using the ideas of logic and reasoning, more complicated models can be built with large knowledge bases. Various automated reasoning systems have been built since 1980s including theorem provers, retrieval systems, semantic networks, etc. The ideas of theoretical computer science and AI concepts such as decision networks are built on the concepts of logical reasoning.  Some researchers argue now that logical reasoning is poised for a comeback.

### Reasoning in Future AI? A step toward a general AI?

Right now, we can easily use machine learning to make predictions. However, machine learning itself does not make deductions through reasoning, as we would do as humans.
Using deductive reasoning, humans can analyze information and come to conclusions even when faced with a lack of knowledge of the subject. Some researchers have proposed recently that bringing back logic and reasoning to AI is the way to move towards a strong AI and build systems that can reason and discover new facts about their world.
One [study by Google's DeepMind](http://proceedings.mlr.press/v80/santoro18a/santoro18a.pdf) has explored trying reasoning in neural networks inspired by IQ tests. They found that their model is  proficient at certain forms of generalization, while being notably weak at others.

In this activity, you are invited to explore downsides of current AI trends and  possibilities of enhancing current AI with logical reasoning as the next big step in generalizing AI.

## Tasks

1. Read the Summary above.

2. Read articles below:
- https://techcrunch.com/2017/07/25/artificial-intelligence-is-not-as-smart-as-you-or-elon-musk-think/
- https://futureoflife.org/2018/07/27/machine-reasoning-and-the-rise-of-artificial-general-intelligences-an-interview-with-bart-selman/?cn-reloaded=1
- https://venturebeat.com/2018/07/11/googles-deepmind-developed-an-iq-test-for-ai-models/
- https://www.ibm.com/watson/advantage-reports/future-of-artificial-intelligence/ai-innovation-equation.html

3. Write a reflection on this activity in the `writing/reflection.md` following the prompts given in the reflection document template.


### Deliverables

- `reflection.md` file with answers to the prompted questions.
