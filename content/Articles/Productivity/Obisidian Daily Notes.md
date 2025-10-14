
---
toc: true
title: Obisidian Daily Notes

tags: ["article"]
date modified: 
date created: 
---
# Daily Notes in Obsidian

Obsidian is one of my favorite productivity tools, but there are some things that I don't fully like about it. One of them that being the daily notes feature. I use Obsidian for journaling and getting an overview of my day while making notes and so being able to use this function efficiently would be very helpful to me.
In this article, I talk about how I use daily notes in Obsidian, the tweaks I have made, the plugins I use, and the hotkeys I have set up. 

Note: None of the plugins I discuss are sponsored and I am sharing them only because I use almost them every day.

## A Disclaimer
This article is about the way I like to work. If it does not work for you, take what you want from it and modify the workflow to fit your style. There are no “rules”. I wanted to write this article as I did not find too many of them on using Daily notes more efficiently.

## Why use Daily notes?
Daily notes help me track my daily activities in a structured way. This way, I can easily find what I did on a particular day and see if I'm progressing toward my goals. It helps me keep track of my time and allows me to see if I am spending too much or too little time on certain tasks, enabling me to make adjustments where needed.

Furthermore, by keeping a record of my daily work, I can get a quick overview of my weekly work. This overview also helps me to find topics that I have recently worked on, which is useful when I want to continue working on them or refer to them later. 
Having a place to temporarily store ideas before turning them into proper notes removes the pressure of having to write something perfect from the start. This way, I can record my thoughts without worrying about the format or accurately writing something, which reduces the chance of breaking my flow.

An example of what a daily note for me might look like is as follows.

## My issues with Daily notes

One of the main areas for improvement of the daily notes feature in Obsidian is the need for an overview. The lack of one makes it difficult to quickly see all of the notes I have created on a specific date or within a certain range of dates. 

It can also be hard to navigate between different dates, making it time-consuming to find the note I am looking for.
Another issue that I wanted to tackle was the ability to record time. The lack of this means I don't have any record of the exact time I created or edited something, making it challenging to track how much time I spent on a particular task or activity.
Additionally, getting to the daily notes page requires too many clicks and can be frustrating, especially because I use this feature frequently and need to access my daily notes quickly. These shortcomings make it less convenient for me to use the daily notes feature, making my workflow less efficient.

## Some solutions
Plugins are a great way to solve specific problems in my workflow. Some of the plugins that I have mentioned in this article, such as the Daily Notes Plugin and the Time Stamper Plugin, have greatly improved my experience with the daily notes feature in Obsidian. They provide an overview of all my daily notes, make it easy to navigate between them, and easily add timestamps to my notes. These plugins have helped me stay organized, find my notes quickly, and make the most of my time.
In addition to using plugins, I also use shortcuts to make my workflow more efficient. I use shortcuts to navigate between pages quickly, create new notes and add timestamps without breaking my flow while working. These shortcuts help me focus on the task by reducing the time I would otherwise spend navigating through pages or menus.

### Templater Plugin
The Templater plugin is a useful tool that I use to streamline the process of creating new notes in Obsidian. It allows me to insert a predefined template with a shortcut every time I start a new note. This template contains the date and time I created the note and when it was last modified. The modified time is automatically updated as I make changes to the note. It also has tags and headers, which makes it easy for me to organize my notes and find the ones I need more easily. This plugin saves me time and effort by providing a consistent and standardized format for all my notes. It also provides me with important information about when the note was created and last modified, which is useful for me to track the progress of my work. This helps me to stay organized and make the most of my time by making it easy to find and refer to my notes.

The template I use is as follows. It uses the Liquid syntax to insert entries automatically. Note that I have configured the plugin to ignore the folder where I save these templates to prevent Obsidian from auto-converting the template into text. 

```MD
---
toc: true
title: <% tp.file.toc: true
title %>
tags: ['temp']
date modified: <% tp.date.now("dddd Do MMMM YYYY, ddd") %>
date created: <% tp.date.now("dddd Do MMMM YYYY, ddd") %>
---
# <% tp.file.toc: true
title %>
```

### Daily Notes Plugin
The Daily Notes Plugin is a great solution to improve my daily note-taking experience. It provides a single-page overview of my daily notes, making it easy to navigate between them. Instead of hunting for something I wrote, I can scroll through the notes and find it quickly. Additionally, each date is editable directly, so I can skip opening multiple pages or searching for the note I want to edit. This makes it much more convenient and efficient for me to review, update or organize my daily notes.
Another advantage of using this plugin is how simple it is to create new daily notes. Instead of navigating multiple pages or menus, I can click a button to create a new note for the day. This feature is incredibly useful for quickly capturing new ideas, thoughts, or information that comes up during the day and helps me to keep track of my daily activities and efficiently.

The picture shows what this plugin looks like.

### Time Stamper
The Time Stamper Plugin is another very useful plugin in my note-taking process. It enables me to use a custom time stamp format, which gives me the hour and minute time as a new bullet point. This plugin makes it easy for me to track time and is an efficient way to keep track of what I do during the day. Not having to enter the time manually saves me time and makes my note-taking process more streamlined.
I use this plugin mostly when I start a new topic. This way, I can quickly see when I began working on it. This plugin does not replace manually tracking time spent on a note which can be useful when I want a rough idea of the duration of a topic or task. 

The template I use to generate my timestamps is.
```MD
- **hh:mm** 
```

This picture shows what it looks like.

### Useful Shortcuts
I use some custom shortcuts to navigate between different pages in Obsidian quickly. These shortcuts save me time and effort by allowing me to jump between pages with a single keystroke. These shortcuts are essential to keep my work efficient and streamline my note-taking process.

(Note that if you are on Windows or Linux, Command is replaced by Control and Option by the Alt key.)

One shortcut I often use is Command+Shift+G, which takes me directly to the daily notes page. This shortcut allows me to quickly access my daily notes and start working on them without navigating through different menus or pages.

Another shortcut that I use frequently is Command+Shift+T. This shortcut creates a timestamp quickly and helps me keep track of time when I start a new topic or task, making it easier to track the time spent on each task.

For navigation between notes, I use Command+Option+Left Arrow to access the previous note quickly and Command+Option+Right Arrow to quickly access the next note. These shortcuts help me stay organized by allowing me to easily switch between notes without manually navigating through different pages.



