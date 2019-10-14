# Lizard Cellular Automata modeling
By Danny Kang, Jeremy Ryan, and Nick Sherman

## **Abstract**

In ocellated lizards, patterns can be observed on their skin due to green and black labyrinthine patterns created by their lizard scale color. We wish to analyze how such patterns can form through using data gathered from ocellated lizards as they mature and mimic the pattern produced through cellular automaton. <br />
We developed manukyan model based on cellular automata to simulate changes in lizard network. The manukyan model contains table of probability values that determines the likeliness of color change of each scale in network. We extended our model by adding brown and white state to green and black state. Furthermore, we experimented with deterministic behaviour in cellular automata to see difference in behavior of model. Pygame was used to visualize the simulation of our model and networkx and matplotlib were used to transform our model to graphs to conduct deeper graphical analysis.
---
## **Annotated bibliography**

### A living mesoscopic cellular automaton made of skin scales
Liana Manukyan, Sophie A. Montandon, Anamarija Fofonjka, Stanislav  Smirnov, Michel C. Milinkovitch <br />
https://www.nature.com/articles/nature22031#extended-data<br />
This paper proposes a cellular automata model to replicate patterns in ocellated lizards as they age. Their model, which used hexagonal scales that were either green or black in color, produced results with similar scale distributions and results visually closer to real lizards than a random distribution, suggesting that scale color is actually affected by the color of nearby scales.

### How animals get their skin patterns: fish pigment pattern as a live Turing wave
Kondo S, Iwashita M, Yamaguchi M.<br />
https://www.ncbi.nlm.nih.gov/pubmed/19557690?dopt=Abstract&holding=npg<br />
This paper analyzed Turing’s idea that spatial patterns autonomously made in the embryo are generated by a stationary wave of cellular reactions. This paper was able to strongly correlate specific genes attributed to at least part of the cellular reactions driving this by analyzing zebrafish’s patterns over the course of their first few weeks of life after identifying mutants in the zebrafish’s population and comparing them to the original fish. They also compared these mutants to normal zebrafish whose stripes were erased via laser light in other work.

### Reaction-diffusion model as a framework for understanding biological pattern formation
Liana Manukyan, Sophie A. Montandon, Anamarija Fofonjka, Stanislav Smirnov, Michel C. Milinokovitch<br />
https://science.sciencemag.org/content/sci/329/5999/1616.full.pdf<br />
This paper explains about the reaction-diffusion model or Turing model and emphasizes its role in understanding spatial skin pattern formation of vertebrates and suggests possible applications of this model. The paper acknowledges the difficulty of applying two dimensional Turing model to complex biological system and mentions a few discoveries that made possible the application of Turing model. According to paper, Gierer and Meinhardt showed that a system needs only to include a network that combines “”a short-range positive feedback with a long-range negative feedback” to generate a Turing pattern, which is now accepted as the basic requirement for Turing pattern formation. Modern genetic and molecular techniques makes it possible to identify such elements of interactive networks in living organisms. Further analysis is possible by predicting dynamic properties of the pattern using computer simulation. Also according to paper, observation of the dynamic properties of Turing patterns in nature was made by Kondo and Asai in a study of horizontal stripes in the tropical fish, Pomacanthus imperator. Paper ends in a positive note about applying Turing model by saying that artificial generation of Turing patterns in cell culture should be possible in the near future as the result of synthetic biology.

---
## **Experiments**

For our experiments, we replicated and extended the cellular automaton model from the Manukyan paper and performed some analysis. We used Pygame to visualize the model, and were able to simulate it over time.
![CA model](https://raw.githubusercontent.com/kdy304g/ComplexLizards-CA/master/images/visual.png)

### 1. Manukyan model for green black states

Our first-pass model was a direct implementation of the model used in the Manukyan paper.

For each cell color, based on its number of like-colored neighbors, there is a probability of changing state before the next time step, copied from the Manukyan paper using Logger Pro. For instance, if a green cell has exclusively black neighbors, there is a 0% chance of changing state. This increases as the number of like-colored cells increases.

The original paper, having built the model from graphs of actual lizard scales, has probabilities that may be slightly skewed from our own. Actual scales are not perfectly hexagonal, and sometimes there are scales with more or fewer than six neighbors. As such, there were entries in the original paper for probability with seven like-colored neighbors which were not used in our model.

 Following is the average probability mass function graph for both green and black scales after this model stabilizes.

![Plot of stabilized PMF](https://raw.githubusercontent.com/kdy304g/ComplexLizards-CA/master/images/lizard_plot.png)

*The above plot shows the probability mass function of differently colored neighbors for each cell type. The solid lines represent our simulated cellular automata model (CA). The dotted line represents a random distribution (RD) as an initial state, with cell color chosen at random between black and green. The dotted and dashed line represents the distribution observed in the Manukyan paper (M) from observation of real ocellated lizards.*

### 2. Adding brown white states

One of the interesting observations about the ocellated lizard is the change in color of their scales from white/brown to green/black. As part of this, we conjectured that the change in color over time could be modelled one of two ways: either as cellular automata with discrete color values that can flip after a specified amount of time steps or as fluid values that change dynamically over time.

The first (and easier) experiment that we implemented was the set possible states of colors. We wanted to see how the color distribution changed over time and see if we can visually mimic what the ocellated lizards do while maintaining similar black:green ratios at the end of the simulation (the papers did not give a brown:white ratio to compare to). What we observed was that visually it looks similar to the ocellated lizards’ skin over time, with the major difference being that the colors change suddenly (as is expected). A view of the beginning of the transition period can be seen in the below image.

 <p align="center">
    <img src="https://github.com/kdy304g/ComplexLizards-CA/blob/master/images/color_change.png"  width="700" height="350" />
 </p>

For the end color distribution, we found that the colors don’t seem to differentiate greatly from the stabilized image of the original experiment. This can be seen in the below image.

 <p align="center">
    <img src="https://github.com/kdy304g/ComplexLizards-CA/blob/master/images/end_time.png"  width="700" height="350" />
 </p>

### 3. Deterministic model

Manukyan model is based on probability of change depending on the number of neighbors. What if the cellular automata model were to evolve deterministically according to set of rules? In this experiment, we intend to define and use rules in the new model to produce similar behavior.

 <p align="center">
    <img src="https://github.com/kdy304g/ComplexLizards-CA/blob/master/images/deterministic_graph.png" width="350" height="350" />
 </p>

For the deterministic model of lizard, two rules for cellular automata is applied. First rule is to convert green scale to black scale when there are more than 3 black neighbors. The second rule is to convert black scale to green scale when there are more than 2 green neighbors. To our disappointment, running the model based on these two rules produce extreme behavior, which is all scales except for few scales at corner turning to green in less than 10 steps. Future steps would be to create a more complicated system of rules to closely mimic patterns in real lizard.

### 4. Graphical Analysis
 In the above experiments, we validate our model with pmf distribution of number of neighbors for four different scales. While the number of neighbors is a solid metric to validate our model, we intend to convert our model to graph to do further analysis of the model in terms of connectedness. <br />

 <p align="center">
   <img src="https://github.com/kdy304g/ComplexLizards-CA/blob/master/images/graph_analysis.png" width="400" height="300" alt><br>
   <em><Model converted to graph using networkx></em>
 </p>

The graph is converted from our model using the library NetworkX with two simple rules. Color of the nodes are represented correspondingly in green, black, white, and brown. Also, there are edges between all the same color nodes. For this experiment, we focus on green and black nodes’ initial and final state after stabilization.  We consider a model of both height and width of 100, total number of scales being 10,000. <br />

| ![PmfInitial](https://github.com/kdy304g/ComplexLizards-CA/blob/master/images/PMF_initial.png)  |
![CdfInitial](https://github.com/kdy304g/ComplexLizards-CA/blob/master/images/CDF_initial.png)|
|:---:|:---:|

Graphs were drawn in log scale for both axes for pmf in order to include a high proportion of graphs with single node in y-axis and the maximum number of nodes in x-axis within a reasonable frame. Two graphs above show the initial state of the model. Pmf graph is heavy tailed with high proportion of small graphs (connected graphs with less than 10 nodes). Similarly, cdf graph on the right shows that most graphs have less than 100 nodes in this model.

| ![Pmf300steps](https://github.com/kdy304g/ComplexLizards-CA/blob/master/images/PMF_300steps.png) | ![Cdf300steps](https://github.com/kdy304g/ComplexLizards-CA/blob/master/images/CDF_300steps.png) |
|:---:|:---:|

As shown in graphs after running the model 300steps, general trend in both pmf and cdf remain similar. There are some notable changes, however. After model stabilizes, gap between small graphs reduces in pmf. Also, the number of nodes in the largest connected subgraph almost doubles to 5,490 from 2,500. This is interesting but not too surprising as the number of green scales dominates after stabilization.

The final way we wanted to show this data was through an overview of what the boxplots look of connected subgraphs over time. Through this, we were able to ascertain how far away from different percentiles the maximally sized subgraphs were. In the situation we were looking at (100 nodes x 100 nodes), the biggest subgraph is the only subgraph that’s above 1000 nodes large after 10 time steps, and over time the smaller subgraphs slowly seem to condense to between 20-90 nodes per subgraph. This gives helps us also better interpret the PMF and CDFs, and demonstrates that there really are a lot of nodes who are alone in their connected subgraphs.

 <p align="center">
    <img src="https://github.com/kdy304g/ComplexLizards-CA/blob/master/images/boxplots.png" width="700" height="350" />
 </p>