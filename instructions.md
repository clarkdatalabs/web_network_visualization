# Web_network_visualization

## Introduction
  This tutorial will show how to build a web-network visulization. The theme we visualize in the example is the web-network of different types of beer.
  You don’t need to be an expert in web development to get started with a network visualization in D3 however we do make some assumptions about our audience.
  We assume that:
  - You’ve had experience with another programming such as Python, Java, or C++
  - You have some working knowledge of HTML, CSS and Javascript
  Regardless of skill level, our hope is to get you up and running with a simple network visualization and slowly build more complexity as we move forward.
  
  Conceptually, we have three difficulty levels: Beginner, Moderate, and Advanced. 
  - For **Beginner**, we'll introduce a simple way to set up your local server to check the effect of the code. We'll provide the code, with simple and clear explanation accordingly, for you to copy/paste on your own computer to further play with. 
  - For **Moderate**, we'll talk about how to manipulate your own data in D3 from csv file. And related D3 events, like mouseover/out and clicks, will be introduced in this section.
  - For **advanced**, we'd like to explore more interesting possibilities that can be realized by D3. If you're interested in fancy and innovated data visualization, come check it out!

***
## Beginner

### Doneload the Code
<a href = "Beer Project" download> Beer-Project </a>
1. [Save this HTML as "index.html" on your computer](code/index.html)
2. [Save this JSON in the same dir with HTML as "graphFile.json"](code/graphFile.json)

Typically, you’d be able to right click on the index.html file and open it with a web browser to render the webpage. If you try this, you’ll likely notice that D3 doesn’t render. This is because we need a server to run D3.

### Running a Local Server on your computer
1. Make sure you have python 3 or higher on your computer
###### - You can check what version of Python you have by following these instructions:https://edu.google.com/openonline/course-builder/docs/1.10/set-up-course-builder/check-for-python.html
###### - If you don’t have Python3 or higher, download the latest version here: https://www.python.org/downloads/
2. Open your **terminal**(Mac) or **Command Prompt**(Windows).
3. Cd into the dir your html is currently at. For example: `cd Desktop/Beer-Project`
4. Enter:`python -m SimpleHTTPServer`
5. You're good to go at http://localhost:8000 (it's the same on any computer that's gone through the process)

### Code Explanation

![code explaination diagram](https://github.com/clarkdatalabs/web_network_visualization/blob/master/img/Code_Explain%20Diagram.png)
