---
toc: true
title: Professional Reports and Papers with LaTEX

tags: ["article"]
date modified: 
date created: 
---
Writing Professional Reports and Papers at 2x speed - A LaTeX tutorial + tips

At some point in your study or career, you will be required to write a report or an article, perhaps even a research paper. You start writing your content down in Word or your favourite text editor. After a little while, some issues crop up. Maybe you don’t like how it looks, or you want to change the format to a two column layout. Maybe you moved an image and the entire document went crazy. Maybe you wrote a long article, but have to change your citations manually. Or heaven forbid, you need to create a table of contents. 
Ugh, you think. I don’t have time for this. Just let me work on the content. If only there was a better way.

Sounds familiar? Read on.

# LaTEX vs Word
At the heart of everything, what you are struggling with is the issue of change. If you had a small article, with barely any changes or styling, Word is great. But for anything more than 5 pages? Ouch.
LaTeX is a complete document preparation system, with the added advantage of a different “language” that makes your life a lot easier. It sounds and looks very strange at first. But once you get the hang of it, it will change the way you write content. Think of it as a more advanced template that is infinitely customisable. All you do is set things up once. Then you can focus on your content.
Oh no! Something changed? That’s okay. Add a few lines to your document and you are good to go.
I do all my reports, articles, homework, projects everything using it and it has saved me days of effort.
It looks professional right off the bat.

(Note: You do NOT need to be a programmer to use this. Just go with it. And google to your heart’s content.)

# Intro to Overleaf
So how do you use this magic mushroom? Well, luckily we have [Overleaf](https://www.overleaf.com/project). This website allows you to write anything you want, provides a lot of templates, live collaboration, and so much more. Mostly for free as well.
Just open the site and make an account. If your institution provides premium access, use your official email ID to register. (You don’t really need it for most use cases.)

(Note: This is not a sponsored post. I just use it everyday and want to make sure it helps more people.)

Everything I show can be viewed [at this link](https://www.overleaf.com/read/rdqngnhbprvr).

## Choosing A Template
Okay great, now it’s time to start working on a project. I will demonstrate with a small article : “Computer Vision in Pytorch - A Primer”. 
- Click “New project”
- Based on what kind of work you are writing this article for, pick a section. For this article, I picked Academic Journal. 
- Look around and find the look you are going for. Click on it, and then click “Use as template”. If you are a University, look for an official template, most of them have one.
- I picked this - [IEEE template](https://www.overleaf.com/latex/templates/ieee-conference-template/grfzhhncsfqn)
Perfect! You are halfway there. 

## Initial Setup
Before we start, let’s just get used to the interface. 
On the left you can see a sidebar with all your files and folders. 
To it’s right, there is the main editor window. If you look closely, the text seems a little strange? Don’t worry, more on that later.
After that you will see a preview of your article. Every time you hit save or “recompile”, this preview will update. You can latex export this as a PDF.
- In the sidebar, I like to make a folder for images by click the little icon that looks like a folder.
- Now, copy paste the first few lines until the line before “begin document”. Think of these as extra functionality. For example: highlighting your links, structuring your document etc.
- Make a new document toc: true
titled “main.tex” using the file icon. 
- Paste the contents there.

Great job! Now we can get to writing everything.

## Understanding The Components
Now the following might seem slightly too complicated. And you will probably feel like it’s not worth the effort. But, trust the process okay?
So far, you should have something like this.
```tex,latex_report_modules,latex_report_modules
\documentclass[conference]{IEEEtran}
\IEEEoverridecommandlockouts
% The preceding line is only needed to identify funding in the first footnote. If that is unneeded, please comment it out.
\usepackage{cite}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{algorithmic}
\usepackage{graphicx}
\usepackage{textcomp}
\usepackage{xcolor}
\def\BibTeX{{\rm B\kern-.05em{\sc i\kern-.025em b}\kern-.08em
    T\kern-.1667em\lower.7ex\hbox{E}\kern-.125emX}}
```
Now we define a basic template.
```tex,latex_report_template,latex_report_template
\begin{document}

\toc: true
title{Computer Vision in Pytorch - A Primer\\
\thanks{I thank Overleaf for this template}
}

\author{\IEEEauthorblockN{1\textsuperscript{st} Subhaditya Mukherjee}
\IEEEauthorblockA{\textit{Faculty of Science and Engineering } \\
\textit{University Of Groningen}\\
Groningen, Netherlands \\
msubhaditya@gmail.com}
}
\maketoc: true
title

\begin{abstract}
\end{abstract}

\begin{IEEEkeywords}

\end{IEEEkeywords}

\section*{}
\subsection*{}

\begin{thebibliography}{00}

\end{thebibliography}

\end{document}

```

You will only need to do this once to get a feel for what’s happening. It’s scary I am sure. But hold on. Keep trying. You’ve got this!
Look at the following code snippets twice. Do you see a pattern?

### Title, Abstract, Keywords
We now need a toc: true
title. So we put it in this line. If you notice the little {}, that is required by LaTeX to know where to start and end something.
```tex,latex_report_toc: true
title, latex_report_parts
\toc: true
title{Computer Vision in Pytorch - A Primer}
```
Are you required to write an abstract or a summary of sorts?
```tex,latex_report_abstract, latex_report_parts
\begin{abstract}
This paper is a short introduction to Pytorch, a deep learning framework. Special focus will be given to applications of Computer Vision. This is a demo paper, and has no particular significance.
\end{abstract}
```
Sometimes, a template will have keywords. You can just enter the ones you think are relevant.

### Authors
Every template you copy, will have a section for the author. Just fill it in the way you want.

### Sections and Subsections
Now for the actual content. Here we use the commands “section”, “subsection”, “subsubsection”. You do not need to bother about giving them numbers. LaTeX will take care of it.
Something like this is a good start.
```tex,latex_report_section, latex_report_parts
\section*{What is Computer Vision?}
A study of the techniques used to extract meaning from image or video related data. The applications are endless, starting from face recognition, to self driving cars.
\subsection*{Computer Vision in the field of Deep Learning}
Deep learning has revolutionised the field of Computer Vision by giving it superpowers. The ability to learn from billions of images come as a huge leap forward in the field.
\subsubsection*{A note}
Classicial CV is still very relevant today.
```

### Figures
Doesn’t seem too hard does it? Let’s add some figures. Woah. What is happening here??
We are defining how we want our figure to look! We tell the system where the image is, how want it to look - centered, fit inside the line, have a caption, and a label. Just change the text to what is relevant to you.
Think about it once. Makes sense right?
```tex,latex_report_fgure, latex_report_parts
\begin{figure}[h]
\includegraphics[width=\linewidth]{figures/2560px-PyTorch_logo_black.svg.png}
\centering
\caption{Representation in the Simulation}
\label{fig:colors}
\end{figure}
```

If you want to change the size, replace “\linewidth” with something like “0.2\linewidth” which makes the figure 0.2 times the size of the line.

### Formatting Text
Okay how about formatting such as bold italics and the like? Super simple. Look at these lines.

```tex,latex_report_form, latex_report_parts
\section{Formatting}
This \textbf{will be bold}, then \textit{italic}, and also \textcolor{red}{red}. 

To add a line break, simply add \\
this will be a new line
```
See? That was not too bad was it? Now we have colours as well!

### Code
If you are a programmer, or need to have any bits of code, this is how you can do it.
To the section where the packages were imported, add the following line.
```tex,latex_report_code,latex_report_code
\usepackage{listings}
```
Now wherever you want to add code, just use it like this. Change the language to what you need of course. Viola! Syntax highlighting!

```tex,latex_report_code_2, latex_report_parts
\begin{lstlisting}[language=Python]
import numpy as np
print(np.random.rand(10))
\end{lstlisting}
```

### Equations
Have you ever had to add equations in Word? I feel sorry for you. LaTeX lets you do it in a breeze. 
```tex,latex_report_equations, latex_report_parts
\section{Equations}
We can have three types of these - An inline equation : $2x+3 = 10$, or a proper block , $$2 \sin(x)+10 = 100$$ or a long form one such as this.
\begin{equation}
E[g^{2}]_{t}= 0.9E[g^{2}]_{t-1}+ 0.1g^{2}_{t}\\
\theta_{t+1}= \theta_{t}- \frac{\eta}{\sqrt{E[g^{2}])_{t}+\epsilon}}g_{t}
\end{equation}
```

It would be impossible to explain the intricacies of using these, but as you can see, it almost feels like writing the equation down as it is. And it looks gorgeous as well.
For more information, refer to [this nice page](https://en.wikibooks.org/wiki/LaTeX/Mathematics).

### Cover page
Hopefully you picked a template that already had one. But if you did not, add this before “\begin{document}”. Replace the text however you feel like. 
```tex,latex_report_cover, latex_report_parts
\begin{toc: true
titlepage}
   \begin{center}
       \vspace*{1cm}

       \textbf{Thesis Title}

       \vspace{0.5cm}
        Thesis Subtoc: true
title
            
       \vspace{1.5cm}

       \textbf{Author Name}

       \vfill
            
       A thesis presented for the degree of\\
       Doctor of Philosophy
            
       \vspace{0.8cm}
     
       \includegraphics[width=0.4\textwidth]{university}
            
       Department Name\\
       University Name\\
       Country\\
       Date
            
   \end{center}
\end{toc: true
titlepage}
```

### Table Of Contents
Adding a TOC is even easier. It also updates automatically. Just add.
```tex,latex_report_toc, latex_report_parts
\tableofcontents
```

### Appendix
Want a list of images and/or tables you have used throughout your document? With page numbers.
```tex,latex_report_appendix, latex_report_parts
%\newpage %add this if you want it to be on a separate page
\begin{appendix}
  \listoffigures
  \listoftables
\end{appendix}
```

### Tables
Tables are a bit complicated in LaTeX, but there is an easier way. Just open this website - [Table generator](https://www.tablesgenerator.com). 
This is a very user friendly UI, so just add whatever you want. And click generate. 
Copy paste that into your Overleaf editor. Done!
Notice the auto numbering? Cool right?

### Citations
Citations are one of the most powerful features of working in LaTeX. The best part? Only the ones you cited will show up in your bibliography! You do not need to worry if you missed any, or forgot to remove any. All you need to do is paste all your citations in a bib file.
- Create a file called references.bib
- Paste all your references in “BibTex” format in the file. Google scholar or any reference manager you use will have that option.
- Cite them like this
```tex,latex_report_cite, latex_report_parts
\section{Citation Example}
Two interesting libraries are Kornia \cite{riba2020kornia} and fast.ai \cite{howard2020fastai}. If you want it inline then : \citep{howard2020fastai}.
```

### Bibliography
Once you have added all your citations, you would need to have a Bibliography. The file “references.bib” you created? Remember the name. Right before “\end{document}” you can add these lines. (Change the first one to what you need. Your template mostly will define it already.)
```tex,latex_report_bib, latex_report_parts
\bibliographystyle{IEEEtran}
\bibliography{references}

\end{document}
```
Looking good!

## Comments
Want to make comments that you or a fellow author can refer to in the future? Just select any bit of text in the editor, you will get a pop up for adding a comment.

## Exporting
Congratulations! Looks like you made it to the end. Now how do you export your awesome document? 
See the little button that has a downward arrow? Click that. You can also click the “Menu” button and find more options there.

## Collaboration
Want to work with colleagues/teammates? Just hit Share and send them the link.

## General Principles and How To Get Help
That’s about it for the basics. Feel free to come back to this document for your reference. You will face problems. Just remember the following things.
- Google is your best friend.
- [This website](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) is a good place to start looking for what’s possible.
- It will take a few tries. But it is definitely worth it.
- If you can say what you want in English, you mostly know the commands already.
- There are a lot of commands. You do NOT need to remember them. You will passively pick them up. Overleaf also has autocomplete which helps.
- Give it some time, it will change your life.

# Fin

This article is in the hopes that it will help someone out. Maybe have the help that I did not. I do not know who it will reach. But to whoever it does, best of luck :)

You can contact me on [LinkedIn](https://www.linkedin.com/in/subhaditya-mukherjee-a36883100), drop me an [[mailto:msubhaditya@gmail.com|Email]]

Like my work? [Buy me a coffee](https://ko-fi.com/aiexistentialart) :) 



