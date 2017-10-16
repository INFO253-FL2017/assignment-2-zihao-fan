1. What is the function of the following technologies in your assignment:
    - HTML: define the semantic structure of my website
    - CSS: adding style to the html
    - JavaScript: handles logics on the website without communicating with the server. e.g. check if required fields are filled out.
    - Python: implements the server side. Host the website as a web service, including listenning to requests and manage server-end logic.
    - Flask: A lightweight framework to help wrap the network requests. Providing easy to use api, like render_template and request.
    - HTTP: A application layer protocol that helps the browser communicate with the server.
    - GET & POST: Two kinds of HTTP request method. Defines how browsers communicate with the servers.
2. How does HTML, CSS, and JavaScript work together in the browser for this assignment?
    - HTML deifines the stucture of the web pages. CSS make the pages look better and Javascript handles the logic without communicate with the server. 
3. How does Python and Flask work together in the server for this assignment?
    - Flask provides the functionalities that allow easy web service building and helps handle the HTTP requests. Python provides the ability of implementing logic and communicate with the OS. 
4. List all of the possible GET and POST requests that your server returns a response for and describes what happens for each GET and POST request
    - GET: /about, /contact, /index, /blog/8-experiments-in-motivation, /blog/a-mindful-shift-of-focus, /blog/how-to-develop-an-awesome-sense-of-direction, /blog/training-to-be-a-good-writer, /blog/what-productivity-systems-wont-solve. Returns the webpage and the corresponding js and css files.
    - POST: /email, collect the data filled in the contact form, wrap it as a authenticated request and send to mailgun server. mailgun helps direct the message via SMTP and then returns a page that show if the email is successfully sent. 