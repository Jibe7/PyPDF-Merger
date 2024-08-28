# Project Motivation
I usually used online PDF mergers but I don't like doing that when working with all of my PDFs (especially the ones that are private) as we don't know what is done with our data on these websites.
## Project Goals
1. Be able to merge several PDFs together ✅
2. Create a user interface where we can drag and drop the PDFs to merge as well as choosing the name and location of the output file. ❌🎯❌ dropped goal = project failed
## Requirements
Use a different Python GUI library that what I used in my previous project (password manager, with customtkinter).
I want to try out https://sciter.com/ which allow to use HTML/CSS/JS. Moreover it is used by famous softwares (Norton, Bitfender, Comodo...).
## Project State
Why dropped the goal of having a UI ? It has been 2 months since I started working as an SDE and stopped working on this pdf merger project. I just use the pdfMerger.py file to merge my pdfs when I need and that is enough. 
I didn't enjoy learning about Sciter technology that much (does not have all recent CSS features, need to learn the other type of JS which is Tiscript). I will surely not finish the UI of this project but in case I want to, or someone else would like to take on the challenge to try a 'new' technology I'll just explain the repository's structure and files / folders role at the end of this readme.
 

**pdfMerger.py** -> script to merge pdf

**main.py** -> basic script to merge pdf

**TryingFolder** -> the actual folder where I was trying to create the app with pysciter. I wrote in its todo.md the steps I thought would allow me to develop the application.

**RunPyScript** -> mix of examples found in the documentation and tryout where I was trying to get the PySciter app (the UI) to call a Python script (the one that has the merge pdf capabilities)

**ExampleFolder** -> Contained example from documentation of PySciter app.

  **handler** -> contains an example where the UI calls script defined in Python
  
  **FirstExampleOpenFolder** -> contains an example supposed to open folders and naviguate in the file system. The use in the project was that I wanted to be able in the UI of merge pdf app to select from the UI the files I wanted to merge and also the output destination folder.
  
