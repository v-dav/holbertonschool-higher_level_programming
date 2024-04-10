# JavaScript DOM Manipulation

![Chrome Version](https://img.shields.io/badge/Chrome-57.0%2B-green.svg)
![Semistandard Compliant](https://img.shields.io/badge/Semistandard-Compliant-yellow.svg)
![XmlHTTPRequest](https://img.shields.io/badge/XmlHTTPRequest-Supported-blue.svg)
![Fetch API](https://img.shields.io/badge/Fetch%20API-Supported-orange.svg)

## Project Overview

In this project, you will dive into the world of JavaScript DOM (Document Object Model) manipulation. You will learn how to interact with web pages using JavaScript, selecting HTML elements, modifying their styles and content, and handling various events. Additionally, you will explore the use of XmlHTTPRequest and Fetch API to make requests and fetch data from servers. By the end of this project, you will have a solid understanding of client-side web development techniques.

## Resources

**Read or watch**:

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [Document Interface](https://developer.mozilla.org/en-US/docs/Web/API/Document)
- [Element Class](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [Locating DOM elements using selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors)
- [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
- [CSS Diner Play with Selectors](https://flukeout.github.io/)
- [Client-side Web APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs)
- [Introduction to web APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
- [Manipulating documents](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
- [Fetching data from the server](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)

## Learning Objectives

By the end of this project, you will be able to explain the following concepts without the need for external references:

- How to select HTML elements in JavaScript
- Differences between ID, class, and tag name selectors
- Modifying an HTML element's style
- Getting and updating an HTML element's content
- Modifying the DOM
- Making a request with XmlHTTPRequest
- Making a request with Fetch API
- Listening/binding to DOM events
- Listening/binding to user events

## Author

- [Vladimir Davidov](https://github.com/v-dav) - Holberton School

---

# Personal Notes
![image](https://github.com/v-dav/holbertonschool-higher_level_programming/assets/115344057/6366698c-c5b0-43e9-818d-d9b3c7a895cb)

## Selection

Top manipulate a DOM element we first need to select that element.

- `document.getElementById(’the-id’);`
- `document.getElementByClassName(’class-name’);`
- `document.getElementByTagName(’li’);`
- `document.querySelector(’any selector’) —> returns the first element in the DOM tree`
- `document.querySelectorAll(’any selector’) —> return a list of all the elements matching the selector`

## Styling

```jsx
const title = document.querySelector("#main-heading");

title.style.color = "red";

//if we want to apply the styling to a list of items, we need to loop through this list
// and apply the styling to each individual item
```

## Create elements & Modify Text

```jsx
const ul = document.querySelector('ul');
const li = document.createElement('li');

ul.append(li);

//modify text
li.innerText = "HEy hey"

.innerText --> the text contained //mostly used
.textContent --> the text displayed as in html file with indents etc.
.innerHTML --> all the tags inside the selected element //security issues
```

## Modyfiing Elements Attributes & Classes

```jsx
//Modify attributes
li.setAttribute('id', 'main-heading')
li.removeAttribute('id');

const title = document.querySelector('#main-heading')
title.getAttribute('id');

//add class to an element
li.classList.add('list-items')
li.classList.remove('list-items')
```

## Remove element

```jsx
li.remove();
```

## Navigating DOM tree

DOM object is the property of the window object (qhich has acces to the info of toolbar, height and width of the window)

Parent-child-sibling relationship

```jsx
let ul = document.querySelector('ul');

console.log(ul.parentNode);
console.log(ul.parentElement);

//one can use
console.log(ul.parentNode.parentNode);
console.log(ul.parentElement.parentElement)

.firstChild
.lastchild

ul.childNodes[1].style.backgroundColor = "blue";

ul.children
ul.firstElementChild
ul.lastElementChild

ul.previousSibling
ul.nextSibling

ul.prebiousElementSibling
ul.nextElementSibling
```

## EventListeners

```jsx
//inline HTML
<button onclick="alert('ILC')">Enter</button>

//script file: element.addEventListener("click", function)
//steps: grab the element, create a function, use addEventListener method

const button2 = document.querySelector('btn-2');
function alertBtn() {
	alert("ILKHLKKHJKLJL");

button2.addEventListener("click", alertBtn);
```

## Event delegation

It allows users to append a SINGLE event listener to a parent element that adds it to all of its present AND future descendants that match a selector
