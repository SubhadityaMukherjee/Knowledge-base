---
toc: true
title: data2vec

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:12 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# data2vec
- [data2vec: a General Framework for Self-supervised Learning in Speech, Vision and Language](https://scontent-sjc3-1.xx.fbcdn.net/v/t39.8562-6/271974914_483120576492438_4239522333319653600_n.pdf?_nc_cat=107&ccb=1-5&_nc_sid=ae5e01&_nc_ohc=9HtSivaeiYUAX9jHaO2&_nc_ht=scontent-sjc3-1.xx&oh=00_AT9A4fyBtoZh-73HXRQHNsSsnEVWyBnxrsprVVPwSvkVIg&oe=61F9E691)
- closer to general self-supervised learning
- framework that uses the same learning method for either speech, NLP or computer vision
- predict latent representations of the full input data based on a masked view of the input in a [self distillation](self distillation.md) setup using a standard Transformer architecture
- Instead of predicting [Modality](Modality.md)-specific targets such as words, visual tokens or units of human speech which are local in nature, data2vec predicts contextualized latent representations that contain information from the entire inpu
- Today’s self-supervised learning research almost typically focuses on a single [Modality](Modality.md)
- As a result, researchers specializing in one [Modality](Modality.md) often adopt a totally different strategy than those specializing in another.
- For each [Modality](Modality.md), algorithms anticipate distinct units: pixels or visual tokens for images, words for the text, and learned sound inventories for voice
- teaching models to anticipate their own representations of the incoming data, regardless of mode
- Instead of predicting visual tokens, phrases, or sounds, a single algorithm may work with completely different sorts of input by focusing on these representations — the [Layers](Layers.md) of a neural network
- robust normalization of the [Features](Features.md) for the job that would be trustworthy in different modalities to directly predict representations.
- The method starts by computing target representations from an image, a piece of text, or a voice utterance using a teacher network
- After that, a portion of the input was masked and repeated with a student network, which predicts the teacher’s latent representations
- Even though it only has a partial view of the data, the student model must predict accurate input data
- The instructor network is identical to the student network, except with somewhat out-of-date weights.
- ImageNet
- surpassed wav2vec 2.0 and HuBERT
- [GLUE](GLUE.md)
- Method:
- data2vec is trained by predicting the model representations of the full input data given a partial view of the input
- They first encode a masked version of the training sample (model in student mode) and then construct training targets by encoding the unmasked version of the input sample with the same model but when parameterized as an exponentially moving average of the model weights (model in teacher mode)
- The target representations encode all of the information in the training sample and the learning task is for the student to predict these representations given a partial view of the input.
- [Modality](Modality.md) encoding:
- The model architecture used is the standard Transformer architecture with a [Modality](Modality.md)-specific encoding of the input data borrowed from prior work:
- For computer vision, they have used the ViT-strategy of encoding an image as a sequence of patches, each spanning 16x16 pixels, input to a linear transformation.
- Speech data is encoded using a multi-layer 1-D convolutional neural network that maps 16 kHz waveform to 50 Hz representations.
- Text is pre-processed to obtain sub-word units, which are then embedded in distributional space via learned [Embedding](Embedding.md) vectors.



