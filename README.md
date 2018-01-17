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

### Download the Code
[Beer Project](../../blob/master/Beer-Project.zip)

Inside the folder, we have:
1. **0_initial_version.html**: The initial version where the dataset is just imported. Will be at "http://localhost:8000/0_initial_version.html"
2. **1_final_version.html**: The final version where we have coded 4 functions to have interactive effects. Will be at "http://localhost:8000/1_final_version.html"
3. **index.html**: The comparison between the 2 versions. Will be at "http://localhost:8000"
4. **beerglassData.csv**: The original dataset.
5. **parse-beerdata.py**: To transform the dataset from csv into json.
6. **graphFile3.json**: The dataset used by D3.
7. **beer-glasses-icons** folder: Icon imaged needed in the program.

Typically, you’d be able to right click on the index.html file and open it with a web browser to render the webpage. If you try this, you’ll likely notice that D3 doesn’t render. This is because we need a server to run D3.

### Running a Local Server on your computer
1. Make sure you have python 3 or higher on your computer
- You can check what version of Python you have by following [these instructions](https://edu.google.com/openonline/course-builder/docs/1.10/set-up-course-builder/check-for-python.html)
- If you don’t have Python3 or higher, download the [latest version](https://www.python.org/downloads/)
2. Open your **terminal**(Mac) or **Command Prompt**(Windows).
3. Cd into the dir your html is currently at. For example: `cd Desktop/Beer-Project`
4. Enter:`python -m SimpleHTTPServer`
5. You're good to go at your local host to see the [the initial version](http://localhost:8000/0_initial_version.html), [the final version](http://localhost:8000/1_final_version.html) and [the comparison between them](http://localhost:8000). (it's the same on any computer that's gone through the process)


### Code Explanation
In this section, we will interpret the codes of both versions. Since **0_initial_version.html** is the result of "0_Importing Dataset", feel free use this code to follow steps in "1_Interactive Functions" to practice and get something similar to **1_final_version.html**.

#### 0_Importing Dataset

#### 1_Interactive Functions





