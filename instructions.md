# Web_network_visualization

## Introduction

  This tutorial will show how to build a web-network visulization. The theme we visualize in the example is the web-network of different types of beer. To read this tutorial, the audience should have basic knowledge about HTML, CSS and Javascript. 
  Conceptually, we have divided the tutorial into three difficulty levels: Beginner, Moderate, and Advanced. 
  - For Beginner, we'll introduce a simple way to set up your local server to check the effect of the code. We'll provide the code, with simple and clear explenation accordingly, for you to copy/paste on your own computer to further play with. 
  - For Moderate, we'll talk about how to manipulate your own data in D3 from csv file. And related D3 events, like mouseover/out and clicks, will be introduced in this section.
  - For advanced, we'd like to explore more interesting possibilities that can be realized by D3. If you're interested in fancy and innovated data visualization, come check it out!

***
## Beginner

### Simple Server

######Once you have your HTML file( along with its related CSS or <style>, JS and D3 or <script>) done, the next step to do is to "show it off"!!!

######"But wait, where's my fancy visualization??? I clicked the HTML and it just opens a dumb plain grey-backgrounded page..."

######Calm down, that's just because the "show it off" is in fact the step after the "practical next step", setting up your local server.

To make it simple:
1. Open your terminal.
2. Cd into the dir your html is currently at.
3. Type (copy/paste) and enter:
```javascript
python -m SimpleHTTPServer
```
4. You're good to go at http://localhost:8000

### the Codes
1. HTML:<br>
[check this HTML](code/index.html)

2. JSON file in the same dir save as "graphFile.json":<br>
[check this JSON](code/graphFile.json)

3. Simple Explanation of the code:
![code explaination diagram]()
