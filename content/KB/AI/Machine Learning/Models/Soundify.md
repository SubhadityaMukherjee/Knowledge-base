---
toc: true
title: Soundify
tags: ['architecture']
---

## Soundify
- In video editing, sound in half of the story
- for professional video editing, the problems come from finding suitable sounds, aligning sounds, video and tuning parameters
- matches sound efects to video - uses quality sound efects libraries and CLIP - Concretely, the system has three parts: classification, synchronization, and mix
- The classification matches efects to a video by classifying sound emitters within - To reduce the distinct sound emitters, the video is split based on absolute color histogram distances
- In the synchronization part, intervals are identified comparing efects label with each frame and pinpointing consecutive matches above a threshold
- In the mix part, efects are split into around one-second chunks - chunks are stitched via crossfades.



