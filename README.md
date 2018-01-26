

#Introduction

This tutorial will walk through the steps of building an interactive network visualization. The theme we visualize in the example is the web-network of different types of beer and their relationships to each other.

We used [Jose Christian&#39;s code](http://bl.ocks.org/jose187/4733747) to build our visualization. It&#39;s a great starting point if you&#39;re interested in better understanding how a very simple network is created in D3.

Click here to see how our final project looks and explore its functionality: [[INSERT LINK]](https://clarkdatalabs.github.io/web_network_visualization/Beer-Project/). The beer visualization illustrates how all beers are related from two common parents: Ales and Lagers. The nodes represent different beer families..

We&#39;ll start out with some code and work our way towards the final project.

You don&#39;t need to be an expert in web development to get started with a network visualization in D3 however, we do make some assumptions about our audience.

We assume that:

- You&#39;ve had experience with another programming such as Python, Java, or C++
- You have some working knowledge of HTML, CSS and Javascript regardless of skill level, our hope is to get you up and running with a simple network visualization and slowly build more complexity as we move forward.

#Download the Code

[Beer Project](https://github.com/clarkdatalabs/web_network_visualization/blob/master/Beer-Project.zip)

Inside the folder, we have 3 files and 3 folders:

1. html: The initial version where the dataset is just imported.
2. json: The dataset used by D3.
3. css: Our CSS file
4. Beer-glasses-icons: A folder containing icon images needed in the program.
5. Final Project: A folder containing all files and the final version of index.html where we have coded 4 functions to have interactive effects.
6. Data Generation: A folder containing the python script and CSV used to create our JSON file

Typically, you&#39;d be able to right click on the index.html file and open it with a web browser to render the webpage. If you try this, you&#39;ll likely notice that D3 doesn&#39;t render. This is because we need a server to run D3.

#Running a Local Server on your computer

1. Make sure you have python 3 or higher on your computer

- You can check what version of Python you have by following [these instructions](https://edu.google.com/openonline/course-builder/docs/1.10/set-up-course-builder/check-for-python.html)
- If you don&#39;t have Python3 or higher, download the [latest version](https://www.python.org/downloads/)

1. Open your terminal(Mac) or Command Prompt(Windows).
2. Cd into the dir your html is currently at. For example: cd Desktop/Beer-Project
3. Enter:`python -m SimpleHTTPServer 8000`

Now you&#39;re ready to render the HTML files. Click on [index.html](http://localhost:8000/0_initial_version.html) to render the initial file. Open up the index.html code in your preferred text editor. We&#39;ll be adding functions to this file throughout this tutorial.

##Mouse Over Nodes

With so many beers, it can be hard to read each label. Everytime we hover over a node on the network, we&#39;ll want to highlight it in green and enlarge the font to make the beer name more visible.

-  Step 1: mouseover to highlight the node itself
  -  Step 1.1: highlight the circle
  -  Step 1.2: highlight the text

**Mouse Out V1**

You might have noticed that each node you hover over, stays highlighted when you mouse out. We want to return the nodes back to their original appearance each time we mouse away from them. To do this, we&#39;ll create the first version of the mouseout function.

- Step 2: Return nodes(circles and text) to original size and color
  - Step 2.1: Return circles
  - Step 2.2: Return text

**Mouse Over Glass**

We&#39;re going to be adding a mouse over effect to each beer glass icon so that they appear to fill up and so that they can highlight which beers in the network should be served in that particular glass. The mouseoverGlass function will also add the effect of filling the glass with beer each time we hover over it.

- Step 3: mouseover glass to highlight associated nodes
- Step 4: mouseover to fill the glass with beer

**Mouse Out V2**

Similar to our first issue with the nodes, the glasses remain filled when we mouse away. Let&#39;s add functionality to our original mouseout function to also return the glasses to their pre-hovered state.

- Step 5: Return glasses to empty

**Click Nodes**

Now that we have a good amount of interactivity in our visualization, let&#39;s finish by adding a click function to the nodes that will both highlight ancestral nodes for easier visibility, and fill up the corresponding glasses.

- Step 6: Click to fill the related glass type(s) with beer
- Step 7: Click to highlight all ancestral nodes
  - Step 7.1: get information about the clicked node
  - Step 7.2: store its ancestral nodes to a list to highlight them in the next step
  - Step 7.3: highlight every ancestral node (circles and text) in the list
