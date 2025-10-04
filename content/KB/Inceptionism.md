---
toc: true
title: Inceptionism

tags: ['visualization']
date modified: Monday, October 10th 2022, 2:02:25 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Inceptionism
- [Google AI Blog: Inceptionism: Going Deeper into Neural Networks](https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html) #[Roam-Highlights](Roam-Highlights)
- [Le Net](Le%20Net.md)
- ![](../images/Pasted%20image%2020220711201721.png)
- ![](../images/Pasted%20image%2020220711201740.png)
- ![](../images/Pasted%20image%2020220711201745.png)
- ![](../images/Pasted%20image%2020220711201750.png)
- ![](../images/Pasted%20image%2020220711201754.png)
- ![](../images/Pasted%20image%2020220711201758.png)
- ![](../images/Pasted%20image%2020220711201804.png)
- One of the challenges of neural networks is understanding what exactly goes on at each layer
- We know that after training, each layer progressively extracts higher and higher-level [Features](Features.md) of the image, until the final layer essentially makes a decision on what the image shows
- For example, the first layer maybe looks for edges or corners
- Intermediate [Layers](Layers.md) interpret the basic [Features](Features.md) to look for overall shapes or components, like a door or a leaf
- The final few [Layers](Layers.md) assemble those into complete interpretations—these neurons activate in response to very complex things such as entire buildings or [Trees](Trees.md).
- One way to visualize what goes on is to turn the network upside down and ask it to enhance an input image in such a way as to elicit a particular interpretation.
- Why is this important? Well, we train networks by simply showing them many examples of what we want them to learn, hoping they extract the essence of the matter at hand (e.g., a fork needs a handle and 2-4 tines), and learn to ignore what doesn’t matter (a fork can be any shape, size, color or orientation)
- But how do you check that the network has correctly learned the right [Features](Features.md)? It can help to visualize the network’s representation of a fork.
- Indeed, in some cases, this reveals that the neural net isn’t quite looking for the thing we thought it was.
- Instead of exactly prescribing which feature we want the network to amplify, we can also let the network make that decision
- In this case we simply feed the network an arbitrary image or photo and let the network analyze the picture
- We then pick a layer and ask the network to enhance whatever it detected.
- If we choose higher-level [Layers](Layers.md), which identify more sophisticated [Features](Features.md) in images, complex [Features](Features.md) or even whole objects tend to emerge
- Again, we just start with an existing image and give it to our neural net.
- We ask the network: “Whatever you see there, I want more of it!” This creates a [feedback loop](feedback loop.md): if a cloud looks a little bit like a bird, the network will make it look more like a bird
- This in turn will make the network recognize the bird even more strongly on the next pass and so forth, until a highly detailed bird appears, seemingly out of nowhere.
- The results are intriguing—even a relatively simple neural network can be used to over-interpret an image, just like as children we enjoyed watching clouds and interpreting the random shapes
- This network was trained mostly on images of animals, so naturally it tends to interpret shapes as animals
- But because the data is stored at such a high abstraction, the results are an interesting remix of these learned [Features](Features.md).
- Of course, we can do more than cloud watching with this technique
- We can apply it to any kind of image
- The results vary quite a bit with the kind of image, because the [Features](Features.md) that are entered bias the network towards certain interpretations
- For example, horizon lines tend to get filled with towers and pagodas
- Rocks and [Trees](Trees.md) turn into buildings
- Birds and insects appear in images of leaves.
- We must go deeper: Iterations If we apply the algorithm iteratively on its own outputs and apply some zooming after each iteration, we get an endless stream of new impressions, exploring the set of things the network knows about
- We can even start this process from a random-noise image, so that the result becomes purely the result of the neural network, as seen in the following images:
- The techniques presented here help us understand and visualize how neural networks are able to carry out difficult classification tasks, improve network architecture, and check what the network has learned during training
- It also makes us wonder whether neural networks could become a tool for artists—a new way to remix visual concepts—or perhaps even shed a little light on the roots of the creative process in general.



