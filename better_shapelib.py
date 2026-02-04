<!DOCTYPE html>
<html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
      <title>Project03ScenesWithinScenes</title>

    <link rel="stylesheet" href="better_shapelib_files/code.css">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="better_shapelib_files/bootstrap.css">
    <link rel="stylesheet" href="better_shapelib_files/bootstrap-theme.css">
    <link rel="stylesheet" href="better_shapelib_files/course.css">
    <script src="better_shapelib_files/jquery.js"></script>
    <script src="better_shapelib_files/dir.js" type="text/javascript"></script> 
  </head>

<body for="html-export">

<div class="container">
<div class="page-header" style="text-align: center;">
<h1><a href="https://cs.colby.edu/">CS</a> 151 Fall 2021 &nbsp; &nbsp; <a href="https://cs.colby.edu/courses/F21/cs151a/index.html">Syllabus</a> &nbsp; &nbsp; <a href="https://cs.colby.edu/courses/F21/cs151a/projects/index.html">Labs/Projects</a> </h1>
</div>
<div style="text-align: center;">
<h2 class="mume-header" id="project-3-scenes-within-scenes">Project 3: Scenes within scenes</h2>
</div>

<p align="center"><img src="better_shapelib_files/titleImage.png" width="300"></p>
<p>In this project, you will practice using functions to make scenes with more <em>hierarchical complexity</em>.
 So far, you have made scenes as collections of compound shapes, which 
are collections of simple shapes. Now you will take this one step 
further and create a scene within a scene that will incorporate 
miniature versions of your previous scenes in it, inspired by the <a href="https://cs.colby.edu/hewolfe/courses/cs151/f21/projects/art.html#p3">Surrealist Art Movement</a>.</p>
<p>The goals of this project are:</p>
<ul>
<li><strong>Encapsulation</strong>: making each shape and scene function work as independent units that you can re-use at any time.</li>
<li>Use conditionals randomness to add nuance to your scenes.</li>
<li>Use keyword parameters to add extra structure.</li>
<li>Use best practices for code organization.</li>
</ul>
<p><em>Extension points are awarded for complex scenes, especially those
 that show me that you can integrate concepts from lecture into making 
your scenes and take things to the next level!</em></p>
<hr>
<h2 class="mume-header" id="tasks">Tasks</h2>

<ul>
<li><a href="#project-3-scenes-within-scenes">Project 3: Scenes within scenes</a>
<ul>
<li><a href="#tasks">Tasks</a>
<ul>
<li><a href="#1">1. Create <code>better_shapelib.py</code></a></li>
<li><a href="#2">2. Make a Mondrian "scene"</a>
<ul>
<li><a href="#2a">2a. Make a <code>mondrian</code> function</a></li>
<li><a href="#2b">2b. Add position and scale parameters to <code>mondrian</code></a></li>
</ul>
</li>
<li><a href="#3">3. Create Margritte "scene"</a>
  <ul>
    <li><a href="#3a">3a. Include at least 2 simple shapes from Project 2 in <code>better_shapelib.py</code> and update them </a></li>
    <li><a href="#3b">3b. Create a new compound shape for <code>better_shapelib.py</code></a></li>
    <li><a href="#3c">3c. Update Mondrian to randomly draw your new compound shape everywhere</a></li>
    <li><a href="#3d">3d. Incorporate the new randomly placed objects into last week's scene</a></li>
  </ul></li>
<li><a href="#4">4. Create a Surrealist "scene"</a></li>
<ul>
<li><a href="#4a">4a. Update your scene from Project 2 in <code>better_shapelib.py</code></a>
</li>
    <li><a href="#4b">4b. Update and test drawing last week's scene at multiple positions and scales</a></li>
    <li><a href="#4c">4c. Create a new surrealist scene that contains the Magritte scene.</a></li>
  </ul>

</ul>
</li>
<li><a href="#check-reproducibility">Check reproducibility</a></li>
<li><a href="#extensions">Extensions</a></li>
<li><a href="#submission-checklist">Submission checklist</a><br>
</li></ul>
</li>
</ul>
<h3 class="mume-header" id="1">1. Create <code>better_shapelib.py</code></h3>

<p>Import <code>turtle</code> and <code>random</code>. Copy-and-paste in your <code>goto</code> and <code>rectangle</code> functions from lab.</p>
<h3 class="mume-header" id="2">2. Make a Mondrian "scene"</h3>

<h4 class="mume-header" id="2a">2a. Make a <code>mondrian</code> function</h4>

<p>Copy-and-paste <code>main</code> from lab into <code>better_shapelib.py</code>. Rename it <code>mondrian</code>.</p>
<p>Add an keyword argument named <code>numRectangles</code> that has some default value. The function signature so far should be:</p>
<pre data-role="codeBlock" data-info="python" class="language-python"><span class="token keyword">def</span> <span class="token function">mondrian</span><span class="token punctuation">(</span>numRectangles<span class="token operator">=</span><span class="token operator">&lt;</span><span class="token builtin">int</span> of your choice<span class="token operator">&gt;</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
  <span class="token triple-quoted-string string">'''Fill me in'''</span>
</pre><p>Test out your <code>mondrian</code> function to make sure that it works. This should be done by adding the following to the bottom of <code>better_shapelib.py</code>:</p>
<pre data-role="codeBlock" data-info="python" class="language-python"><span class="token keyword">if</span> __name__<span class="token operator">==</span> <span class="token string">'__main__'</span><span class="token punctuation">:</span>
  mondrian<span class="token punctuation">(</span><span class="token punctuation">)</span>
</pre><p>Notes:</p>
<ul>
<li>Modify this main code to call <code>exitonclick</code> and probably <code>turtle.tracer(False)</code> (remember: if you turn animations off, call <code>turtle.update()</code> before <code>exitonclick</code> to make sure the canvas shows all your shapes).</li>
<li>Every time that you develop a new shape and/or scene in this 
project, you should test them out in main code like this and running <code>better_shapelib.py</code> to make sure they work.<br><strong>Do NOT wait until the end of the project to test your code!</strong> Test as you go!</li>
<li>For <code>mondrian</code> (and all other files and functions), 
follow the code organization best practices (e.g. make docstrings, use 
inline comments, etc.). <strong>This will affect your grade!</strong></li>
</ul>
<h4 class="mume-header" id="2b">2b. Add position and scale parameters to <code>mondrian</code></h4>

<p>Imagine that the Mondrian that is drawn by your <code>mondrian</code> function is "a compound shape". Add required position and scale parameters:</p>
<pre data-role="codeBlock" data-info="python" class="language-python"><span class="token keyword">def</span> <span class="token function">mondrian</span><span class="token punctuation">(</span>x<span class="token punctuation">,</span> y<span class="token punctuation">,</span> s<span class="token punctuation">,</span> numRectangles<span class="token operator">=</span><span class="token operator">&lt;</span><span class="token builtin">int</span> of your choice<span class="token operator">&gt;</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
  <span class="token triple-quoted-string string">'''Fill me in'''</span>
</pre><p>Make the position parameters adjust where on the canvas the 
Mondrian is drawn and the scale parameter adjust its size. Test out 
drawing your "Mondrian scene" a few times in different positions at 
different scales. You should get something that looks like this:</p>
<p align="center"><img src="better_shapelib_files/mondrianScene.png" width="300"></p>
<p>Take a screenshot. This is <strong>Required Image 1</strong> to be included in your project report.</p>
<p><em>Hint: It might help to think of the random positions of the 
Mondrian rectangles as offsets from the (x, y) that you pass into the <code>mondrian</code> function.</em></p>

<h3 class="mume-header" id="3">3. Create Margritte "scene"</h3>

<h4 class="mume-header" id="3a">3a. Include at least 2 simple shapes from Project 2 in <code>better_shapelib.py</code> and update them </h4>
<p><strong>Think ahead:</strong> you will be creating a scene where an 
out of place object will be repeated all over last week's scene. You 
will want to pick shapes that are needed to draw your new object. Look 
at artwork from the <a href="https://cs.colby.edu/hewolfe/courses/cs151/f21/projects/art.html#p3">Surrealist Art Movement</a> to see examples of incongruent repetition like <a href="https://library.artstor.org/#/asset/AWSS35953_35953_34184956">Golconda</a> or <a href="https://library.artstor.org/#/asset/ASFMOMAIG_10312704651">Les valeurs personnelles</a> by René Magritte.</p>
<p>Things to do for each simple shape function you paste into <code>better_shapelib.py</code>:</p>
<ul>
<li>Make sure that you use loops where ever possible. The goal is to 
make your code as efficient as possible in terms of the number of lines 
of code and the simplicity of that code. <em>None of your functions should have lots of repetitive code!</em></li>
<li>Add a <code>fill</code> keyword argument and integrate it into your function, include a default value.</li>
<li>Add a <code>color</code> keyword argument and integrate it into your function, include a default value.</li>
<li><strong>Remember:</strong> test each function one-by-one as you go.</li>
</ul>
<h4 class="mume-header" id="3b">3b. Create a new compound shape for <code>better_shapelib.py</code>
</h4>

<p>It should rely on the simple shapes from above.</p>
<ul>
<li>Make sure that you use loops where ever possible.</li>
<li>Add <code>x</code> and <code>y</code> keyword arguments and integrate them into your function to control the position the compound shape is placed.</li>
<li>Add a <code>s</code> keyword argument and integrate it into your function to control the scale of the compound shape.</li>
<li>Add a <code>fill</code> keyword argument and integrate it into your function.</li>
<li>Add a <code>color</code> keyword argument (maybe more if you need to control more than one color) and integrate it into your function.</li>
</ul>

<h4 class="mume-header" id="3c">3c. Create a <code>magritte</code> function to randomly draw your new compound shape everywhere</h4>

<ul>
<li>Create a copy of your <code>mondrian</code> function and rename it <code>magritte</code>. </li>
<li>Replace the <code>rectangle</code> function call with a call to your new compound shape.</li>
<li>Add at least one element of randomness when drawing your compound shapes (<em>it doesn't need to be fancy</em>). For example, only fill the shape 50% of the time, or pick between a couple of colors.</li>
<li>Test out drawing your "Magritte" image a few times in different positions at different scales.</li>
</ul>

<h4 class="mume-header" id="3d">3d. Incorporate the new randomly placed objects into last week's scene</h4>

<ul>
<li>Copy over your <code>colby1</code> function from Project 2.</li>
<li>Copy only the dependent functions from <code>shapelib.py</code> to <code>better_shapelib.py</code> that haven't been copied over yet. </li>
<li>Modify the <code>colby1</code> function to call the local functions, making any necessary updates to parameters. </li>
<li>Update the <code>colby1</code> function to call the <code>magritte</code> function.  Set the position and size parameters so that it only covers a portion of the scene.</li>
<li>Call only the <code>colby1</code> function in the main function.</li>
</ul>

<p>Run your code and take a screenshot. This is <strong>Required Image 2</strong> to be included in your project report.</p>

<h3 class="mume-header" id="4">4. Create a Surrealist "scene"</h3>

<h4 class="mume-header" id="4b">4a. Update your scene from Project 2 in <code>better_shapelib.py</code></h4>

<pre data-role="codeBlock" data-info="python" class="language-python"><span class="token keyword">def</span> <span class="token function">colby1</span><span class="token punctuation">(</span>x<span class="token punctuation">,</span> y<span class="token punctuation">,</span> s<span class="token punctuation">)</span><span class="token punctuation">:</span>
  <span class="token triple-quoted-string string">'''docstring'''</span>
  <span class="token comment"># your code here</span>
</pre><p>Make it so that your function uses the scale <code>s</code> and position <code>(x, y)</code> parameters like usual.</p>
<p>Reminders:</p>
<ul>
<li>Position one of your scene's shapes at <code>(x, y)</code>, convert the remaining hard-coded positions into offsets from <code>(x, y)</code>.</li>
<li>Scale offsets and lengths/distances, NOT positions.</li>
<li>Leave angles alone (e.g. don't change commands like <code>turtle.left(30)</code>).</li>
<li>Commands that move the turtle count as lengths/distances <code>turtle.forward(100)</code> <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo>→</mo></mrow><annotation encoding="application/x-tex">\rightarrow</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.36687em;vertical-align:0em;"></span><span class="mrel">→</span></span></span></span> <code>turtle.forward(s*100)</code></li>
</ul>

<h4 class="mume-header" id="4b">4b. Update and test drawing last week's scene at multiple positions and scales</h4>

<p>Call your <code>colby1</code> function at least three times (in main code — i.e. indented in <code>if __name__== '__main__':</code>). Take a screenshot like you did for the Mondrian above. This is <strong>Required Image 3</strong> to be included in your project report.</p>

<h4 class="mume-header" id="4c">4c. Create a new surrealist scene that contains the Magritte scene.</h4>

<p>In <code>sureal.py</code>, import your better shape library. You probably want to rename the import to save you typing:</p>
<pre data-role="codeBlock" data-info="python" class="language-python"><span class="token keyword">import</span> better_shapelib <span class="token keyword">as</span> bsl
</pre>

<p>Create a function called <code>sureal</code> in <code>sureal.py</code> that is a new scene which  incorporates your <code>colby1</code> scene at least once. Choose an artist or artwork from the <a href="https://cs.colby.edu/hewolfe/courses/cs151/f21/projects/art.html#p3">Surrealist Art Movement</a> for inspiration. For example, can you use this task to create a scene within a scene with disjointed or conflicting concepts?  </p>

<p> In your report section called <b>Art Reflection</b> discuss which compositions/artists inspired you and what aspects of the compositions you emulated.</p>

<p>Running <code>python3 surreal.py</code> should draw your surealist scene. Take a screenshot. This is <strong>Required Image 4</strong> to be included in your project report.</p>
<hr>
<h2 class="mume-header" id="check-reproducibility">Check reproducibility</h2>

<p>In order to grade your project, we need to be able to run your code 
and get the same results as you do! Here is a summary of the expected 
outputs from each of the source code files that you created:</p>
<ul>
<li><code>python3 lab3.py</code>: Draws your Mondrian from lab</li>
<li><code>python3 better_shapelib.py</code>: Draws your scene updated from Project 2 with a new compound object randomly placed multiple times at random sizes.</li>
<li><code>python3 sureal.py</code>: Draws your sureal scene.</li>
</ul>
<hr>
<h2 class="mume-header" id="extensions">Extensions</h2>

<p>Congratulations on completing the core tasks! If your code and report
 meet the above expectations, you’ve already earned up to 26/30 points 
for this project.</p>
<p>The remaining 4/30 are a chance for you to earn credit for exploring 
parts of this project and digging deeper to express your creativity! 
This is entirely optional; 26/30 is a B and is a perfectly respectable 
place to stop. Extensions are open-ended and exist to compliment the 
structured core project. Explore and learn something new that interests 
you! Concentrating your energy on 1-2 "deep" extensions that challenge 
you will earn you more points than many small, "shallow" extensions.</p>
<p>You can pick your own topics that interest you. Here are a few examples:</p>
<ol>
<li>Creative or complex scenes above and beyond the basic expectations count as extensions</li>
<li>Make a new scene and place it into the surreal scene.</li>
<li>Demonstrate even more levels of hierarchical encapsulation (scenes within scenes within scenes).</li>
<li>Learn about and use command line arguments control a number of different aspects of the scene. Be sure that you use <code>sys.argv</code> in <code>surreal.py</code> and the <code>sureal</code> function.</li>
</ol>
<hr>
<h2 class="mume-header" id="submission-checklist">Submission checklist</h2>

<p>To turn in your project, make sure you do all of the following:</p>
<ul>
<li>Check the rubric in Google Classroom and make sure your report and code contain all the required parts.</li>
<li>Move your lab folder inside your project folder (i.e. drag the <code>Lab03</code> folder inside <code>Project03</code>).</li>
<li>Create a zip file of your project.</li>
<li>Attach (drag) the zip file to the posted project assignment on Google Classroom.</li>
<li>Click Turn In on your Google Doc report on Google Classroom.</li>
</ul>
<p><a href="https://cs.colby.edu/courses/F21/cs151a/projects/report.html">Link to detailed turn in instructions and more information about what should be contained in the report</a></p>
<hr>
</div>

<p class="lastMod"><small>© 2021 Hannen Wolfe and Oliver Layton</small></p>


</body></html>