---
toc: true
title: Interpretability vs Neuroscience

tags: ['cognitivemodel']
date modified: Monday, October 10th 2022, 2:02:25 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Interpretability Vs Neuroscience
- [Interpretability vs Neuroscience (rough note) -- colah's blog](rough%20note)%20--%20colah's%20blog)%20--%20colah's%20blog)

## You Can Get the Responses of All Neurons for Arbitrarily Many Stimuli
- In neuroscience, one is limited in the number of neurons they can record from, their ability to select the neurons they record, and the number of stimuli they can record responses to.
- For artificial neural networks, we can record the responses of all neurons to arbitrarily many stimuli
- Turn arounds are much faster than biological experiments
- There's no recording noise, No synaptic fatigue.

## Not Only Do You Have the [Connectome](Connectome.md), You Have the Weights!
- A major undertaking in neuroscience is the attempt to access the [Connectome](Connectome.md)
- Even if they succeed, they won’t know the weights of those connections
- With artificial neural networks, all the connections and weights are simply there for us to look at.
- And since we also know how these artificial neurons are computed, in principle we have everything we need to just reason through and understand the neural network.

## Weight-tying Massively Reduces the Number of Unique Neurons!
- weight-tying,
- [Force](Force.md) many neurons to have the same weights
- he most common use of this is in convolutional neural networks, where each neuron has translated copies of itself with the same weights.
- in ImageNet [Conv](Conv.md) nets, weight-tying often reduces the number of unique neurons in early vision by 10,000x or even more
- This results in artificial neural networks having many fewer neurons for early vision than their biological counterparts
- This means we can just literally study every single neuron.

## Establishing Causality by Optimizing the Input
- one of the thorniest issues in understanding neurons in artificial networks is separating [Correlation](Correlation.md) from causation.
- Does a neuron detect a dog head? Or does it just detect part of a dog head?
- There's a second very closely related problem: we don't know what the space of likely functions a neuron might perform is.
- this is also a challenge in neuroscience.
- We create stimuli “from scratch” to strongly activate neurons (or combinations of neurons) in artificial neural networks, by starting with random noise and optimizing the input.
- The key property of feature [visualization](visualization.md) is that anything in the resulting [visualization](visualization.md) there because it caused the neuron to fire more
- If feature [visualization](visualization.md) gives you a fully formed dog head with eyes and ears arranged appropriately, it must be detecting an entire dog head
- If it just gives an eye, it's probably only (or at least primarily) responding to that.
- Recent efforts in neuroscience have tried to develop similar methods [], by using an artificial neural network as a proxy for a biological one.
- unclear they give you the same ability to establish a causal link.
- It seems hard to exclude the possibility that the resulting stimulus might have content which causes the artificial neurons predicting the [Biological Neuron](Biological%20Neuron.md) to fire more, but aren't causally necessary for the [Biological Neuron](Biological%20Neuron.md) to fire.

## Interventions, Ablations, and Edits
- [Optogenetics](Optogenetics.md) has been a major methodological advance for neuroscience in allowing neuroscientists to temporarily ablate neurons, or to [Force](Force.md) them to activate.
- Artificial neural networks are trivial to manipulate at the level of neurons
- One can easily ablate neurons or set them to particular activations
- But one can also do more powerful "circuit editing" where one modifies parameters at a finer grained level.
- In image generation, [Bau et al., 2018](https://gandissect.csail.mit.edu/) show that you can ablate neurons to remove objects like tress and windows from generated images
- In RL, [Hilton et al., 2020](https://distill.pub/2020/understanding-rl-vision/) show that you can ablate [Features](Features.md) to blind an agent to a particular enemy while leaving other competencies in tact
- More recently, [Cammarata et al, 2021](https://distill.pub/2020/circuits/curve-circuits/) reimplements a large chunk of neural network from scratch, and then splices it into a model.

## We Can Study the Exact Same Model.
- Neuroscientists might study a model organism species, but each brain they study has different neurons
- If one neuroscientist reports on an interesting neuron they found, other neuroscientists can't directly study that same neuron
- In fact, the neuroscientists studying the original neuron will quickly lose access to it: probes can't be left in indefinitely, organisms die, human subjects leave, and even setting that aside neurons change over time.
- Studying artificial networks, we can collaboratively reverse engineer the same “brain", building on each other.
- we have a shared web of thousands of "footholds" into InceptionV1, consisting of neurons we understand fairly well and know the connections between, which makes it massively easier to explore



