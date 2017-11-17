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

Once you have your HTML file( along with its related CSS or <style>, JS and D3 or <script>) done, the next step to do is to **"show it off"**!!!

"But wait, where's my fancy visualization??? I clicked the HTML and it just opens a dumb plain grey-backgrounded page..."

Calm down, that's just because the "show it off" is in fact the step after the "practical next step", **setting up your local server**.

To make it simple:
1. Open your terminal.
2. Cd into the dir your html is currently at.
3. Type (copy/paste) and enter:
```javascript
python -m SimpleHTTPServer
```
4. You're good to go at http://localhost:8000

### the Code
1. HTML:
```javascript

<!-- IDEAS
	-SHOW WHICH BEER GOES IN WHICH GLASS AND WHY
	-INTERACTIVITY WITH FLAVOR AND AROMAS
	-HOVER EFFECTS
		-MAKE TEXT BIGGER
		-HIGHLIGHT TEXT
		-SHOW EXAMPLES OF BEER
 -->

<!DOCTYPE html>
<meta charset="utf-8">
<script src="http://d3js.org/d3.v2.min.js?2.9.3"></script>
<style>

  body {
      background-color: #555;
  }

  h1 {
      color: #aa9663;
  }

  .link {
    stroke: #aaa;
  }

  .node text {
  fill:#fff;
  /*cursos:pointer;*/
  }

  .node text:hover {
  fill:#000000;
  font-size: 250%;
  cursos:pointer;
  }

  .node circle{
  stroke:#5d5338;
  stroke-width:1px;
  fill:#aa9663;
  }

  .node circle:hover{
  stroke:#5d5338;
  stroke-width:1px;
  fill:#99fd17;

  }

</style>



<head>
  <title>The Very Many Varieties of Beer</title>
</head>


<body>
<!-- <h1>The Very Many Varieties of Beer</h1> -->

  <script>

    var width = 1260,
        height = 900

    var svg = d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height);

    var force = d3.layout.force()
        .gravity(.04)
        .distance(90)
        .charge(-200)
        .size([width, height]);

    d3.json("graphFile.json", function(json) {

    	json.links.forEach(function(d){
        d.source = d.source_id;    
        d.target = d.target_id;
      });

    	
      force
          .nodes(json.nodes)
          .links(json.links)
          .start();


      var link = svg.selectAll(".link")
          .data(json.links)
        .enter().append("line")
          .attr("class", "link")
        .style("stroke-width", function(d) { return Math.sqrt(d.weight); });

      var node = svg.selectAll(".node")
          .data(json.nodes)
        .enter().append("g")
          .attr("class", "node")
          .on("mouseover", mouseover)
          .on("mouseout", mouseout)
          // .on("click",click)
          .call(force.drag);


      function mouseover(){
      	d3.select(this).select("circle").transition()
      	.duration(450)
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
      }

      function mouseout(){
      	d3.select(this).select("circle").transition()
      	.duration(450)
      	.attr("r", function(d) { 

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

          	} else {
          		return 1;

          	}

          });
      }

      node.append("circle")
      //DEPENDING ON 'GROUP' SIZE, THE RADIUS OF THE CIRCLE IS LARGER
          .attr("r", function(d) { 

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

          	} else {
          		return 1;

          	}

          });

      node.append("text")
          // PLACEMENT OF THE TEXT IN RELATION TO THE NODE
          .attr("dx",function(d) {
          	if (d.name == "Lager"){
          		return -18;

          	} else if (d.name == "Ale"){
          		return -12;
          	}
          		else {
          		return 12;

          	}})

          .attr("dy", ".35em")
          .text(function(d) { return d.name });

      force.on("tick", function() {
        link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
      });
    });

  </script>
</body>
```
2. json file in the same dir save as "graphFile.json":
```javascript
{
  "nodes":[
    {"source_id":0,"name":"Ale","group":1},
    {"source_id":1,"name":"Lager","group":1},
    {"source_id":2,"name":"Irish Ale","group":2},
    {"source_id":3,"name":"Pale Ale","group":2},
    {"source_id":4,"name":"Brown Ale","group":2},
    {"source_id":5,"name":"Mild Ale","group":2},
    {"source_id":6,"name":"Pumpkin Ale","group":2},
    {"source_id":7,"name":"American Wild Ale","group":2},
    {"source_id":8,"name":"Lambic","group":2},
    {"source_id":9,"name":"Sahti","group":2},
    {"source_id":10,"name":"Belgian/French Ale","group":2},
    {"source_id":11,"name":"Stout/Porter","group":2},
    {"source_id":12,"name":"Cream Ale","group":2},
    {"source_id":13,"name":"California Common","group":2},
    {"source_id":14,"name":"German Ale","group":2},
    {"source_id":15,"name":"German Lager","group":2},
    {"source_id":16,"name":"European Lager","group":2},
    {"source_id":17,"name":"Pilsner","group":2},
    {"source_id":18,"name":"American Lager","group":2},
    {"source_id":19,"name":"American Pale Ale","group":3},
    {"source_id":20,"name":"Strong Pale Ale","group":3},
    {"source_id":21,"name":"India Pale Ale","group":3},
    {"source_id":22,"name":"English Pale Ale/Bitter","group":3},
    {"source_id":23,"name":"Faro","group":3},
    {"source_id":24,"name":"Gueuze","group":3},
    {"source_id":25,"name":"Fruit","group":3},
    {"source_id":26,"name":"Unblended","group":3},
    {"source_id":27,"name":"Witbier","group":3},
    {"source_id":28,"name":"Oud Bruin","group":3},
    {"source_id":29,"name":"Saison","group":3},
    {"source_id":30,"name":"Biere De Garde","group":3},
    {"source_id":31,"name":"Biere De Champagne","group":3},
    {"source_id":32,"name":"Belgian Pale Ale","group":3},
    {"source_id":33,"name":"Belgian Dark Ale","group":3},
    {"source_id":34,"name":"Flanders Red Ale","group":3},
    {"source_id":35,"name":"American Porter","group":3},
    {"source_id":36,"name":"American Stout","group":3},
    {"source_id":37,"name":"English Porter","group":3},
    {"source_id":38,"name":"Irish Stout","group":3},
    {"source_id":39,"name":"Imperial Stout","group":3},
    {"source_id":40,"name":"Flavored Stout","group":3},
    {"source_id":41,"name":"Oatmeal Stout","group":3},
    {"source_id":42,"name":"Baltic Porter","group":3},
    {"source_id":43,"name":"Sweet Stout","group":3},
    {"source_id":44,"name":"Roggenbier","group":3},
    {"source_id":45,"name":"Kolsch","group":3},
    {"source_id":46,"name":"Altbier","group":3},
    {"source_id":47,"name":"Weissbier","group":3},
    {"source_id":48,"name":"Dortmunder","group":3},
    {"source_id":49,"name":"Bock","group":3},
    {"source_id":50,"name":"Keller Bier","group":3},
    {"source_id":51,"name":"Marzen","group":3},
    {"source_id":52,"name":"Schwarzbier","group":3},
    {"source_id":53,"name":"Munich Lager","group":3},
    {"source_id":54,"name":"Vienna Lager","group":3},
    {"source_id":55,"name":"Rauchbier","group":3},
    {"source_id":56,"name":"European Pale Lager","group":3},
    {"source_id":57,"name":"Eurpoean Strong Lager","group":3},
    {"source_id":58,"name":"American Imperial Pilsner","group":3},
    {"source_id":59,"name":"American Pilsner","group":3},
    {"source_id":60,"name":"German Pilsener","group":3},
    {"source_id":61,"name":"Bohemian Pilsner","group":3},
    {"source_id":62,"name":"American Pale Lager","group":3},
    {"source_id":63,"name":"American Dark/Amber Lager","group":3},
    {"source_id":64,"name":"American Adjunct Lager","group":3},
    {"source_id":65,"name":"Blonde Ale","group":4},
    {"source_id":66,"name":"American Wheat Ale","group":4},
    {"source_id":67,"name":"Amber Ale","group":4},
    {"source_id":68,"name":"English Strong Ale","group":4},
    {"source_id":69,"name":"Old Ale","group":4},
    {"source_id":70,"name":"American Strong Ale","group":4},
    {"source_id":71,"name":"Wheat Wine","group":4},
    {"source_id":72,"name":"Barely Wine","group":4},
    {"source_id":73,"name":"Scotch Ale","group":4},
    {"source_id":74,"name":"Double IPA","group":4},
    {"source_id":75,"name":"Black IPA","group":4},
    {"source_id":76,"name":"Light Ale","group":4},
    {"source_id":77,"name":"Premium Bitter/ESB","group":4},
    {"source_id":78,"name":"Burton Pale Ale","group":4},
    {"source_id":79,"name":"Belgian Strong Pale Ale","group":4},
    {"source_id":80,"name":"Belgian Strong Dark Ale","group":4},
    {"source_id":81,"name":"Foreign Stout","group":4},
    {"source_id":82,"name":"Hefeweizen","group":4},
    {"source_id":83,"name":"Gose","group":4},
    {"source_id":84,"name":"Berliner Weisse","group":4},
    {"source_id":85,"name":"Kristall-Weizen","group":4},
    {"source_id":86,"name":"Weizenbock","group":4},
    {"source_id":87,"name":"Dunkel-Weizen","group":4},
    {"source_id":88,"name":"Maibock/Helles","group":4},
    {"source_id":89,"name":"Doppelbock","group":4},
    {"source_id":90,"name":"Eisbock","group":4},
    {"source_id":91,"name":"Dunkler Bock","group":4},
    {"source_id":92,"name":"Munich Helles","group":4},
    {"source_id":93,"name":"Munich Dunkel","group":4},
    {"source_id":94,"name":"European Dark Lager","group":4},
    {"source_id":95,"name":"Light Beer","group":4},
    {"source_id":96,"name":"Malt Liquor","group":4},
    {"source_id":97,"name":"Dry Beer","group":4},
    {"source_id":98,"name":"Ice Beer","group":4},
    {"source_id":99,"name":"Japanese Rice Lager","group":4},
    {"source_id":100,"name":"Winter Warmer","group":5},
    {"source_id":101,"name":"Tripel","group":5},
    {"source_id":102,"name":"Dubbel","group":5},
    {"source_id":103,"name":"Quadrupel","group":5}
  ],
  "links":[
    {"source_id":0,"target_id":2,"weight":1},
    {"source_id":0,"target_id":3,"weight":1},
    {"source_id":0,"target_id":4,"weight":1},
    {"source_id":0,"target_id":5,"weight":1},
    {"source_id":0,"target_id":6,"weight":1},
    {"source_id":0,"target_id":7,"weight":1},
    {"source_id":0,"target_id":8,"weight":1},
    {"source_id":0,"target_id":9,"weight":1},
    {"source_id":0,"target_id":10,"weight":1},
    {"source_id":0,"target_id":11,"weight":1},
    {"source_id":0,"target_id":12,"weight":1},
    {"source_id":0,"target_id":13,"weight":1},
    {"source_id":0,"target_id":14,"weight":1},
    {"source_id":1,"target_id":15,"weight":1},
    {"source_id":1,"target_id":16,"weight":1},
    {"source_id":1,"target_id":17,"weight":1},
    {"source_id":1,"target_id":18,"weight":1},

    {"source_id":3,"target_id":19,"weight":1},
    {"source_id":3,"target_id":20,"weight":1},
    {"source_id":3,"target_id":21,"weight":1},
    {"source_id":3,"target_id":22,"weight":1},
    {"source_id":8,"target_id":23,"weight":1},
    {"source_id":8,"target_id":24,"weight":1},
    {"source_id":8,"target_id":25,"weight":1},
    {"source_id":8,"target_id":26,"weight":1},
    {"source_id":10,"target_id":27,"weight":1},
    {"source_id":10,"target_id":28,"weight":1},
    {"source_id":10,"target_id":29,"weight":1},
    {"source_id":10,"target_id":30,"weight":1},
    {"source_id":10,"target_id":31,"weight":1},
    {"source_id":10,"target_id":32,"weight":1},
    {"source_id":10,"target_id":33,"weight":1},
    {"source_id":10,"target_id":34,"weight":1},
    {"source_id":11,"target_id":35,"weight":1},
    {"source_id":11,"target_id":36,"weight":1},
    {"source_id":11,"target_id":37,"weight":1},
    {"source_id":11,"target_id":38,"weight":1},
    {"source_id":11,"target_id":39,"weight":1},
    {"source_id":11,"target_id":40,"weight":1},
    {"source_id":11,"target_id":41,"weight":1},
    {"source_id":11,"target_id":42,"weight":1},
    {"source_id":11,"target_id":43,"weight":1},
    {"source_id":14,"target_id":44,"weight":1},
    {"source_id":14,"target_id":45,"weight":1},
    {"source_id":14,"target_id":46,"weight":1},
    {"source_id":14,"target_id":47,"weight":1},
    {"source_id":15,"target_id":48,"weight":1},
    {"source_id":15,"target_id":49,"weight":1},
    {"source_id":15,"target_id":50,"weight":1},
    {"source_id":15,"target_id":51,"weight":1},
    {"source_id":15,"target_id":52,"weight":1},
    {"source_id":15,"target_id":53,"weight":1},
    {"source_id":15,"target_id":54,"weight":1},
    {"source_id":15,"target_id":55,"weight":1},
    {"source_id":16,"target_id":56,"weight":1},
    {"source_id":16,"target_id":57,"weight":1},
    {"source_id":17,"target_id":58,"weight":1},
    {"source_id":17,"target_id":59,"weight":1},
    {"source_id":17,"target_id":60,"weight":1},
    {"source_id":17,"target_id":61,"weight":1},
    {"source_id":18,"target_id":62,"weight":1},
    {"source_id":18,"target_id":63,"weight":1},
    {"source_id":18,"target_id":64,"weight":1},

    {"source_id":19,"target_id":65,"weight":1},
    {"source_id":19,"target_id":66,"weight":1},
    {"source_id":19,"target_id":67,"weight":1},
    {"source_id":20,"target_id":68,"weight":1},
    {"source_id":20,"target_id":69,"weight":1},
    {"source_id":20,"target_id":70,"weight":1},
    {"source_id":20,"target_id":71,"weight":1},
    {"source_id":20,"target_id":72,"weight":1},
    {"source_id":20,"target_id":73,"weight":1},
    {"source_id":20,"target_id":74,"weight":1},
    {"source_id":21,"target_id":75,"weight":1},
    {"source_id":22,"target_id":76,"weight":1},
    {"source_id":22,"target_id":77,"weight":1},
    {"source_id":22,"target_id":78,"weight":1},
    {"source_id":32,"target_id":79,"weight":1},
    {"source_id":33,"target_id":80,"weight":1},
    {"source_id":38,"target_id":81,"weight":1},
    {"source_id":47,"target_id":82,"weight":1},
    {"source_id":47,"target_id":83,"weight":1},
    {"source_id":47,"target_id":84,"weight":1},
    {"source_id":47,"target_id":85,"weight":1},
    {"source_id":47,"target_id":86,"weight":1},
    {"source_id":47,"target_id":87,"weight":1},
    {"source_id":49,"target_id":88,"weight":1},
    {"source_id":49,"target_id":89,"weight":1},
    {"source_id":49,"target_id":90,"weight":1},
    {"source_id":49,"target_id":91,"weight":1},
    {"source_id":53,"target_id":92,"weight":1},
    {"source_id":53,"target_id":93,"weight":1},
    {"source_id":57,"target_id":94,"weight":1},
    {"source_id":64,"target_id":95,"weight":1},
    {"source_id":64,"target_id":96,"weight":1},
    {"source_id":64,"target_id":97,"weight":1},
    {"source_id":64,"target_id":98,"weight":1},
    {"source_id":64,"target_id":99,"weight":1},

    {"source_id":68,"target_id":100,"weight":1},
    {"source_id":79,"target_id":101,"weight":1},
    {"source_id":80,"target_id":102,"weight":1},
    {"source_id":80,"target_id":103,"weight":1}

  ]
}
```
