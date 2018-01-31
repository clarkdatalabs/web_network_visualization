

# Introduction

This tutorial will walk through the steps of building an interactive network visualization. The theme we visualize in the example is the web-network of different types of beer and their relationships to each other.

We used [Jose Christian&#39;s code](http://bl.ocks.org/jose187/4733747) to build our visualization. It&#39;s a great starting point if you&#39;re interested in better understanding how a very simple network is created in D3.

Click here to see how our final project looks and explore its functionality: [[INSERT LINK]](https://clarkdatalabs.github.io/web_network_visualization/Beer-Project/). The beer visualization illustrates how all beers are related from two common parents: Ales and Lagers. The nodes represent different beer families..

We&#39;ll start out with some code and work our way towards the final project.

You don&#39;t need to be an expert in web development to get started with a network visualization in D3 however, we do make some assumptions about our audience.

We assume that:

- You&#39;ve had experience with another programming such as Python, Java, or C++
- You have some working knowledge of HTML, CSS and Javascript regardless of skill level, our hope is to get you up and running with a simple network visualization and slowly build more complexity as we move forward.

# Download the Code

[Beer Project](https://github.com/clarkdatalabs/web_network_visualization/blob/master/Beer-Project.zip)

Inside the folder, we have 3 files and 3 folders:

1. html: The initial version where the dataset is just imported.
2. json: The dataset used by D3.
3. css: Our CSS file
4. Beer-glasses-icons: A folder containing icon images needed in the program.
5. Final Project: A folder containing all files and the final version of index.html where we have coded 4 functions to have interactive effects.
6. Data Generation: A folder containing the python script and CSV used to create our JSON file

Typically, you&#39;d be able to right click on the index.html file and open it with a web browser to render the webpage. If you try this, you&#39;ll likely notice that D3 doesn&#39;t render. This is because we need a server to run D3.

# Running a Local Server on your computer

1. Make sure you have python 3 or higher on your computer

- You can check what version of Python you have by following [these instructions](https://edu.google.com/openonline/course-builder/docs/1.10/set-up-course-builder/check-for-python.html)
- If you don&#39;t have Python3 or higher, download the [latest version](https://www.python.org/downloads/)

1. Open your terminal(Mac) or Command Prompt(Windows).
2. Cd into the dir your html is currently at. For example: `cd Desktop/Beer-Project`
3. Enter:`python -m SimpleHTTPServer 8000`

Now you&#39;re ready to render the HTML files. Click on [index.html](http://localhost:8000/0_initial_version.html) to render the initial file. Open up the index.html code in your preferred text editor. We&#39;ll be adding functions to this file throughout this tutorial.


# Functions

## mouseoverNodes()

With so many beers, it can be hard to read each label. Everytime we hover over a node on the network, we&#39;ll want to highlight it in green and enlarge the font to make the beer name more visible.


- Step 1: Mouseover to highlight the node itself
  - Step 1.1: Highlight the circle.      

In our mouseoverNodes() function we use the D3 selector to select the circle our cursor hovers on.
```javascript
// Step1: mouseover to highlight the node itself
  // Step1.1: highlight the circle
  d3.select(this).select("circle")
  .transition()
  .duration(50) //the amount of milliseconds the element transitions last
  .style("fill","#99fd17") //makes the circles of the nodes glow green on mouseover
  .attr("r", function(d) { //creates a function to return the radius (r) of the circle on mouseover

  //groups represent the hierarchy of the different beer types
    if (d.group == 1){ //group 1 represents the Ale or Lager, the earliest ancestor node
      return 52; // since group 1 is the our earliest ancestor, the radius should be the largest

    } else if (d.group == 2){
      return 15;

    } else if (d.group == 3){
      return 10;

    } else if (d.group == 4){
      return 8;

    } else if (d.group == 5){
      return 5;

    } else {
      return 1;
    }
  });
```
  - Step 1.2: Highlight the text

```javascript
//Step1.2: highlight the text
d3.select(this).select("text") //we can add effects to the text on mouseover too
.style("font-size","100%") //the '100%' changes the text to the default font-size. All labels are the same size.
```

## mouseout() - V1

You might have noticed that each node you hover over, stays highlighted when you mouse out. We want to return the nodes back to their original appearance each time we mouse away from them. To do this, we&#39;ll create the first version of the mouseout function.

- Step 2: Return nodes(circles and text) to original size and color
  - Step 2.1: Return circles
```javascript
// Step2: return nodes (circles and texts) to normal size and color
  // Step2.1: return circles to normal
  d3.select(".networkgraph").selectAll("circle") //selects all of the circles in the networkgraph class
  .style("fill","white") //makes all the circles go back to white
  .attr("r", function(d) { //makes the circles go back to their original size, depending on their group number (order in hierarchy)

    if (d.group == 1){
      return 50;

    } else if (d.group == 2){
      return 10;

    } else if (d.group == 3){
      return 6;

    } else if (d.group == 4){
      return 4;

    } else if (d.group == 5){
      return 2;

    } else if (d.group == 6){
      return 1;

    } else {
      return 4.5;

    }
  })
```

  - Step 2.2: Return text
```javascript
// Step2.2: return text to normal
d3.select(".networkgraph").selectAll(".nodeText") //selects all of text in the networkgraph class
.style("font-size","10px") //returns them to their original size, which is 10px
```

## mouseoverGlass()

We&#39;re going to be adding a mouse over effect to each beer glass icon so that they appear to fill up and so that they can highlight which beers in the network should be served in that particular glass. The mouseoverGlass function will also add the effect of filling the glass with beer each time we hover over it.

- Step 3: mouseover glass to highlight associated nodes
```javascript
//Step3: mouseover glass to highlight associated nodes
  var glass = d3.select(this).attr("id") //creates a variable 'glass' to store the id of the mouseovered glass (each glass has a unique id)
  d3.selectAll("g.node[glassTypes*="+ glass +" i]").select("circle") //selects all the circles from the nodes with the attribute "glassTypes" containing the id of the mouseovered glass
    .style("fill","#99fd17") //makes the circles of the nodes glow green
    .transition()
    .duration(50)
    .attr("r", 10) //changes the size of the circles
```
- Step 4: mouseover to fill the glass with beer
```javascript
//Step4: mouseover to fill the glass
  d3.select("#" + glass + "whiterect") //selects the white rectangle (each has a unique id that corresponds to the glass and related beer color, which it covers)
  .transition()
  .duration(900)
  .attr("height", "5px") //shrinks the height of the white rectangle, essentially hiding it from view. This gives the illusion that the glass fills up.
```

## mouseout() - V2

Similar to our first issue with the nodes, the glasses remain filled when we mouse away. Let&#39;s add functionality to our original mouseout function to also return the glasses to their pre-hovered state.

- Step 5: Return glasses to empty
```javascript
// Step5: return glasses to empty
  d3.selectAll(".transformableRect") //selects the white rectangle (class is named "transformableRect") that conceals the beer color of each glass
    .transition()
    .duration(900)
    .attr("height", "95px") //brings back the height of the white rectangle to the original size. This gives the illusion that the glass empties out
```

## clickNodes()

Now that we have a good amount of interactivity in our visualization, let&#39;s finish by adding a click function to the nodes that will both highlight ancestral nodes for easier visibility, and fill up the corresponding glasses.

- Step 6: Click to fill the related glass type(s) with beer
```javascript
//Step6: Click to highlight the related glass type(s)

  var glassesString = d3.select(this).attr("glassTypes"), //retrieves the attribute "glassTypes", which contains a string of concatenated glasses that correspond to that node
      beerGlassList = glassesString.split('|'); //creates an array from the glassesString using the pipe symbol ('|') as a delimiter

  for (beer in beerGlassList){ //loops through the beerGlassList
    d3.select("#"+ beerGlassList[beer].split(' ')[0].toLowerCase() + "whiterect") //for each beer, find the respective white rectangle
    .transition()
    .duration(900)
    .attr("height", "5px")
  }
```
- Step 7: Click to highlight all ancestral nodes
  - Step 7.1: get information about the clicked node
```javascript
//Step7: Click to highlight all ancestral nodes
  //Step7.1: get information about the clicked node
  var clickedId = d3.select(this)[0][0].__data__.index, //gets the ID of the clicked node
      clickedGroup = d3.select(this)[0][0].__data__.group; //gets the group number of the clicked nodes (groups represent the hierarchy of the different beer types)
```
  - Step 7.2: store its ancestral nodes to a list to highlight them in the next step
```javascript
//Step7.2: add its ancestral nodes to highlight into an array
var glowId = clickedId,
    glowIdList = [glowId]; //creates an array to store the IDs of the nodes that will glow, including the clicked node and its parental nodes

for(i = clickedGroup; i > 1; i --){ //loops through the group number (represents hierarchy) from the clicked node to its highest-level parent, whose group is 1
  glowId = json.links[glowId - 2].source_id; //based on how parental nodes are connected to the children nodes in the dataset, we get the ID of the parental node accordingly
  //console.log(json.links[glowId - 2]); //uncomment this if you're interested in better understanding how child nodes are connected to parent nodes
  glowIdList.push(glowId); //adds the ID of each parental node into the glowIdList
}
```
  - Step 7.3: highlight every ancestral node (circles and text) in the list
```javascript
//Step7.3: activate effect (color and size) on every node (circles and texts) in the array
for(var i = 0; i < glowIdList.length; i++){ //loops through the IDs in the glowIdList we built in step 7.2
  var selector = "[sourceID='" + glowIdList[i] + "']"; //creates a variable to store the ID of the node

  d3.select(selector).select("circle") //selects the node with the ID of the node stored in the selector variable
  .transition()
  .duration(50)
  .style("fill","#99fd17")
  .attr("r", function(d) { 
    if (d.group == 1){
      return 52;

    } else if (d.group == 2){
      return 15;

    } else if (d.group == 3){
      return 10;

    } else if (d.group == 4){
      return 8;

    } else if (d.group == 5){
      return 5;

    } else {
      return 1;
    }
  });

  d3.select(selector).select("text")
  .transition()
  .duration(50)
  .style("font-size","100%")
}
```
