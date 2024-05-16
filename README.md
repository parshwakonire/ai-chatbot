<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
</head>
<body>
<h1>ChatBot</h1>
    <p>ChatBot is a basic Python-based chatbot that can handle a variety of simple queries. It can tell you the current time, perform basic arithmetic operations, provide definitions for specific terms, and respond to basic greetings and farewells.</p>
    <h2>Table of Contents</h2>
  <ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>

  </ul>
    <h2 id="features">Features</h2>
    <ul>
        <li><strong>Current Time</strong>: Responds with the current time.</li>
        <li><strong>Arithmetic Operations</strong>: Evaluates basic arithmetic expressions.</li>
        <li><strong>Definitions</strong>: Provides definitions for a set of predefined terms.</li>
        <li><strong>Greetings and Farewells</strong>: Responds to common greetings and farewells.</li>
    </ul>
    <h2 id="installation">Installation</h2>
    <ol>
        <li><strong>Clone the repository</strong>:
            <pre><code>git clone https://github.com/parshwakonire/pd-chatbot cd pd-chatbot</code></pre>
        </li>
        <li><strong>Set up a virtual environment (optional but recommended)</strong>:
            <pre><code>python -m venv venv
source venv/bin/activate  <!-- On Windows use `venv\Scripts\activate` --></code></pre>
        </li>
        <li><strong>Install required packages</strong>:
            <pre><code>pip install requests</code></pre>
        </li>
    </ol>
    <h2 id = "usage">Usage</h2>
    <p>Run the chatbot script:</p>
    <pre><code>python chatbot.py</code></pre>
    <h3>Interacting with the ChatBot</h3>
    <p>The chatbot accepts various inputs and responds accordingly:</p>
    <ul>
        <li><strong>Greetings</strong>:
            <pre><code>User: hi
Bot: Hello! How can I help you?</code></pre>
        </li>
        <li><strong>Farewells</strong>:
            <pre><code>User: bye
Bot: Goodbye! Have a great day!</code></pre>
        </li>
        <li><strong>Current Time</strong>:
            <pre><code>User: time
Bot: The current time is 10:30:00 AM</code></pre>
        </li>
        <li><strong>Arithmetic Operations</strong>:
            <pre><code>User: 2 + 2
Bot: The result is: 4</code></pre>
        </li>
        <li><strong>Definitions</strong>:
            <pre><code>User: define computer
Bot: The definition of 'computer' is: A machine that can be programmed to automatically carry out sequences of arithmetic or logical operations. Modern digital electronic computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks.</code></pre>
        </li>
        <li><strong>Other Queries</strong>:
            <pre><code>User: who is the prime minister of india
Bot: Mr. Narendra Modi</code></pre>
        </li>
    </ul>
   <h2 id="contributing">Contributing</h2>
  <p>Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:</p>
  <ol>
    <li>Fork the repository.</li>
    <li>Create a new branch (<code>git checkout -b feature/yourfeature</code>).</li>
    <li>Make your changes and commit them (<code>git commit -am 'Add new feature'</code>).</li>
    <li>Push your changes to the branch (<code>git push origin feature/yourfeature</code>).</li>
    <li>Create a pull request.</li>
  </ol>
   
  <h2 id="license">License</h2>
  <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
  </body>
</html>
