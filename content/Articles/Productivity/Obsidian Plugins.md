
---
toc: true
title: Obsidian Plugins

tags: ["article"]
date modified: 
date created: 
---
# My Favourite Obsidian Plugins for Research Notes + 2 Bonus Tips 
Obsidian is my favourite program for taking notes. Be it for research, general things I learn, summaries from papers, lecture notes and the like. Out of the box, it does so many things really well.
But, its real power lies in the vast number of plugins it has. Most of these are user created, and you can even make your own (or hack one together)! In this sea of functionality, these are the top few that I use. Grouped by the type of task for easier lookup.

(Disclaimer : I am not sponsored by either Obsidian or any of the authors of the plugins mentioned here. These are personal preferences.)

## The use case 
I am a student, researcher and programmer. I take lecture notes, read a lot of research papers, articles and books. These come down to a lot of information. Of course, there’s no way I can remember all of these bits of fragmented information. 
Therefore, drumroll…, I use Obsidian to help me put these bits of information in a place I can easily access. Since I use this almost everyday, I want taking notes to be as painless and efficient as possible. 
These plugins are a huge help in doing exactly that. (Ordered by the type of task)

## How to install these plugins?
This is a simple step. Simple open Obsidian Settings, Scroll down a bit and select “Community plugins”. Disable Restrictive mode, and then browse to your hearts content!

### Writing
Writing notes is the major objective here. So how do we make it extra painless? Plugins of course!
- Dynamic Table of Contents : Many times, I take notes for a long form text. Sometimes these notes end up pretty huge, and it becomes slightly harder to find something. What about adding a Table Of Contents to the start? Sounds great, but what if we update the note? In comes this plugin, with an automatically updating TOC.
- Tags : Super simple, also built in. Adding “#topic1, #topic2 etc” to a file to make it easier to search and organise.
- Frontmatter Tag Suggest : Tags are great, but who remembers which ones they used before? Nobody. This plugin autocompletes tags based on ones you have used in previous notes. You can create new ones the normal way of course. 
- Note Refactor : Made a huge note with a lot of headings? Why not split them into individual topics and maintain links to them? This makes it easier for you to have one major idea per note. Here I have a bunch of test headings, you can see how after applying them they become new notes that link to the current file.
- Paste URL into selection : The name says it all doesn’t it?
- Templater : Another plugin I use daily. I like starting my notes with “date_created”, “date_modified”, “tags”, “toc: true
title” and insert the file name as the header. Since I do this for every single note, why not automate it? This plugin lets you create blocks of dynamic text to be inserted with a keyboard shortcut. I use “Cmd+Shift+I” (“Control+Shift+I” for Windows)
- Typewriter Scroll : Zen Mode is a way of life. This lets me focus on what I am writing by automatically scrolling the page, and dimming the rest of the text apart from the line I am currently writing. I do disable it while reading though.
- Command Palette : This one is pretty obvious, but this built in plugin is just a text search. You can quickly open files with a (Cmd/Control + O) that brings up a searchable menu, or use (Cmd/Control + P) to bring up a searchable list of quick actions.
- Vim Mode : This little option is not for everyone honestly. If you have never heard of Vim, just skip this point. I use vim as my default text editor for everything else. And I can’t live without its keybindings. This just lets me use the vim keys for everything.

### Research
For research (AI research in my case), we have three main objectives : 
- Merge important information from a large number of sources.
- Find links between ideas that you did not see.
- Maintain a daily log as something of a lab notebook.
There are 5 plugins that fulfil these criteria pretty decently. 
- Daily Notes : This is a Core plugin and comes with Obsidian. Essentially it’s a journal. You can add whatever you want to it and it is created every day. I use it to keep a time stamped log of what I did that day. It is also useful if you just want to dump a bunch of information but don’t want to format and organise it just yet.
- TimeStamper : In my daily notes, I like having timestamps (eg - 9:30 : I did xyz). This plugin lets me set a custom format and a keyboard shortcut. I have set it to “Cmd+T” (for Mac or Control+T for Windows)
- Backlinks : A real game changer and another built in plugin. This shows you every file that either is linked in the current file, or refers to the current one. Identifying links between concepts, and finding more of them is absolutely invaluable in research.
- Quick LaTEX for Obsidian : LaTEX is probably the easiest way of writing professional looking math-y stuff, be it equations or formulae or anything similar. This plugin has a lot of options for autocomplete, formatting, and makes my job almost ridiculously easy. Here’s how it looks. (Just typing a random equation)

### Organising
What do you do once you have a lot of files, you organise them of course! Now Obsidian by default makes it pretty easy to do this. But these plugins make organising less of a chore and much more of a fun thing to do.
- Local Images : To make my notes more informative, I sometimes paste images. Now many times these are links from some website, which makes it a little risky, because what if the website stops working? This plugin automatically downloads image links in your notes and saves them locally. (It also links to the correct downloaded file.)
- Graph view : Oh the gift and curse of a pretty graph. I sometimes use this to navigate between my links either to or from a file. It also gives me a very useful overview of what I have. I generally use the “Local graph” that shows me a graph for the current note, rather than the “Global” full one which shows me everything. (It’s pretty, but unhelpful)
- Linter : Maybe I have a bunch of empty lines, empty list items, my headers are not in sentence case, my text is not formatted, my paragraphs are weird. Or anything like that. I am lazy, so I use the Linter plugin to automatically perform a bunch of processing and clean up my files. 
- Tag Wrangler : Have a lot of tags? View/Edit/Change them across every file that uses them in one place. Also useful for finding files that match a few criteria.
- File Cleaner : Remove empty files, unreferenced images etc. Keeping your “Digital Garden” pruned and bug free.
- Obsidian Link Converter : Because I host my Obsidian Vault on a [personal website](https://subhadityamukherjee.github.io/AI-knowledge-base/), sometimes the links that Obsidian uses don’t work, this plugin lets me mass convert them to a format that does.

## Bonus tips!!
- Make sure every file has a single major idea. If you have too many, use the “Note Refactor” to put them in their own files. This will make it extremely easy to refer to the “Ideas” in the text somewhere else instead of linking to the whole text. 
- Want pages that consolidate all the notes that have a particular tag together and save them automatically to a single file? Say you want a file that has links to all the notes that have the tag “#apple”. Here is [a little script](https://gist.github.com/SubhadityaMukherjee/24cad590043f1a2dc0d264251c0a7ef3) that I wrote which does just that.

## Fin
This article is in the hopes that it will help someone out. Maybe have the help that I did not. I do not know who it will reach. But to whoever it does, best of luck :)

Like these/Want more? Buy me a coffee! [Kofi](https://ko-fi.com/subhadityamukherjee)

Want articles on something specific? Just ask!

You can always contact me on [LinkedIn](https://www.linkedin.com/in/subhaditya-mukherjee-a36883100), or drop me an [[mailto:msubhaditya@gmail.com|Email]]



