
---
toc: true
title: Extracting Highlights from a PDF easily

tags: ["article"]
date modified: 
date created: 
---
How to get PDF Highlights to Notes in 3 steps 

Reading a research paper/lecture slides/book? Made a lot of highlights in a PDF? Now want to get them into your notes as text? Don’t want to have to type everything again? Here’s your way out.
Hey. Reading a research paper or a long document is itself a lot of effort. After that, I do not have the energy to again copy everything properly into my notes. I have been searching for a way to do that, but none of the options I found work for two-column layouts, or even maintain page order properly.

(Disclaimer: I am not sponsored by, or hold any affiliations to any of the products mentioned below. I share them because I use them every day and think they would be useful to you.)

## What we want to do
Convert highlights like in this document on the left to notes with minimal effort. 
I use a note application called [Obsidian](https://obsidian.md), but anything you use works here. As long as it supports text. 

## Existing Programs and… their flaws
Many PDF viewers offer the ability to export notes into text. Like [Skim](https://skim-app.sourceforge.io) for Mac, [Adobe Acrobat](https://get.adobe.com/uk/reader/), [OneNote](https://www.onenote.com/) etc 
But they have their fair share of issues
- Most of them are paid
- Two column layouts, like those in research papers are not handled very well
- The export option removes all page information which makes it super hard to format it
- They do not export comments or other annotations properly
- They get very confused when the word or line spacing differs a little

You get the point.

## pdfannots
After a lot of searching, I found a Python script on GitHub called [pdfannots](https://github.com/0xabu/pdfannots). Sadly their documentation makes it very hard for someone without experience to get it running. Hence this article.

## Installing the script
There are not many steps involved here. But it might sound a little complicated.
- Step 1: Install [Python](https://www.python.org/downloads/). If you are on Windows, select install ‘pip’ as well. If you are on Mac or Linux, you can skip this step as it already comes pre-installed with your system.
- Step 2: Open a terminal (Hit the Windows button -> Search/ Mac: Open Spotlight -> Search/Linux: You probably know how to)
- Step 3: Run (paste it and hit Enter) the following command
```
pip install pdfannots
```
(If you get an error, you probably did not install Python or pip. Try Step 1 again.)
PS: Don’t get annoyed at me for not counting these steps. This is a one-time install after all. Once it’s on your laptop, you can just proceed with the ones below every other time.

## Getting your highlights!
- Step 1: Once that completes, identify where the PDF with highlights is saved on your computer. You can open the location in your file manager. Note the location. Replace <filename> with this
As an example : (Windows: “C:\Users\Subha\Documents\paper.pdf)”,  Mac : “/Users/eragon/Documents/paper.pdf”)
- Step 2: Now go back to the terminal, and run the following 
```
pdfannots <filename>
```
- Step 3: Voila! Now just select all that output text, copy it, and paste it wherever. Easy right?
- Step 4: This is optional of course, but you can format your text however you want to. (I will write an article on how you can do that and update this blog later.)

## Specific Formatting
Maybe your document did not get read properly. Here is a little FAQ.
- Document not found: Check your file path properly. Maybe a little google search? Try dragging and dropping instead.
- Two column research paper, use this instead: pdfannots —cols=2 <filename>
- Spaces all weird? : pdfannots —word-margin=<anything> <filename>
- Weird technicalities? : Refer to the [original page](https://github.com/0xabu/pdfannots) of the script. You can also ask the developers questions.
- Want to automate common formatting, convert to markdown, etc? : (An article will come soon, but you can leave a comment in the meanwhile.)

## Fin
This article is in the hopes that it will help someone out. Maybe have the help that I did not. I do not know who it will reach. But to whoever it does, best of luck :)

Have any questions? Comment or shoot me an email.
Like these/Want more? Buy me a coffee! [Kofi](https://ko-fi.com/subhadityamukherjee)
Want articles on something specific? Just ask.
You can contact me on [LinkedIn](https://www.linkedin.com/in/subhaditya-mukherjee-a36883100), drop me an [[mailto:msubhaditya@gmail.com|Email]]



