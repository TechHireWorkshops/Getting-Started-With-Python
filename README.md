# Getting Started With Python

Python is an easy-to-learn and temendously popular language.  It can be used for just about anything, and is especially well-suited for data science, machine learning, and data scraping. Python is also very in-demand in the job market, and learning Python can give you a leg up in your job search.

## Installing Python

One of the biggest barriers to entry in Python, or any language, is installing and setting up the language and its environments so you can use it easily and reliably.

Python 2.7 comes pre-installed on Mac computers, but this version is far out of date.  The best way to update python, and ensure that we can continue to keep up to date with new python versions (as well as maintain projects written in older python versions, is with a version manager.

### Pyenv

Pyenv is one of the most popular version managers for Python, and is based on the Ruby rbenv version manager. This allows us to install different versions of Python on our machines and switch between them as needed.  To get started, we need to install some programs on which pyenv relies.

	xcode-select --install
	brew install openssl readline sqlite3 xz zlib
	
Once we've installed these packages, we're ready to install pyenv.  We run:

	brew install pyenv

When we run commands in our terminal, our computer searches through  a list of directories to find an executable file with that name. When we type something like `python`, our operating system searches through our system to find where Python is installed on our computer to run it.

Pyenv intercepts commands using something called shims, determines which Python version has been specified by your application, and passes our commands along to the correct Python installation.

To make sure that our computer uses these shims, instead of the default isntalled Python on our machines, we need to add some commands to our shell configuration files.

If we're using bash, we can run this command:

`echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile`

If we have zsh installed, we would run this instead:

`echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc`

To make sure that our terminal is using these redirects, we can run `exec "$SHELL"`, or just restart the terminal.

Now we can use pyenv to install new version of Python on our computer.  To see what versions are available, we run

	pyenv install --list
	
Without getting into the conda bootstrap versions of Python, we can see that 3.9.0 is the most recent stable versions of Python.  To install this, we run

	pyenv install 3.9.0
	
If we run the command `pyenv versions`, we can see the versions of Python installed our our machines.  There should be an asterisk next to one of our versions, showing which is the globally selected version of Python.  Similarly, we can run `python --version` to check our currently used version.

It looks like 2.7 is our currently selected version, which is not what we want.  To tell our computer to default to our newly-installed recent versions, we can run

	pyenv global 3.9.0
	
Now, when we check out versions, we will see that 3.9.0 is our selected version. We can also set different projects to use specific versions of python using `pyenv local <version>`.

### Pipenv

Just as Python has different versions, so too do the dependencies and libraries that you can use in Python. Often these different verions have differences that can break applications if the wrong one is being used. This can become a problem when working with others on apps, or installing a Python project from elsewhere.

Python comes with a package manager called pip, similart to Node's npm, or Ruby's bundler. By default, however, pip installs the most recent version of each dependency when run.  One way we used to address this issue, was by creating virtual environments for each Python project in which the app would run, with specified versions of each dependency (and the dependencies of those dependencies).

This solution works, but involved using different libraries for installation of packages, and for creation and management of virtual environments.  To consolidate this, pipenv was created. To install pipenv, we run:

	pip install pipenv
	
We can now use pipenv to install dependencies, and it will at the same time create a virtual environment for our project.  We won't be getting much into virtual environments, but take a look at [this article](https://opensource.com/article/18/2/why-python-devs-should-use-pipenv) for more information.

When we do want to add packages to our project, we can run

	pipenv install <package name>
	
This installs packages within the virtual environment that this Python project exists within.  To run this project inside the appropriate environment, we run

	pipenv run python <name of file>

## Using Python

Now that we have Python configured, let's start writing programs. We can create a new Python project by creating any file with the file extension `.py`. To run this file on our computer, we run `python <file name>` in our terminal from the project's root directory.  We're going to create a card guessing game to practice using Python, but before that, we need to cover a few basics of the language.

### Variables

Variables in Python have scope, meaning that they exist as either global or local variables.  Variables declared outside of a function are global, and can be used anywhere. Variables declared inside function are local, and can only be used inside of functions or in functions within that function.

#### Single values

Variables in Python do not require a command, they are initialized as they are defined

	number = 10
	name = "Mike"
	
Variables can created for any data type in this way

#### Lists, Sets, and Arrays

Python has a few different data types for storing multiple data points.  The first of these are lists.

Lists are:

- ordered collections of data.
- mutable.
- dynamic and can contain objects of different data types.
- accessible by index number.

Lists are declared like this:

	list = [1,2,3,4]
	
Tuples are a similar data type in Python.

Tuples are:

- ordered collections of data.
- immutable.
- able to contain objects of different data types.
- accessible by index number.

Tuples are declared thusly:

	tuple = (1,2,3,4)
	
Note that even though tuples are declared using round brackets, we can access them by index using square crackets, like `tuple[index number]`.

Arrays are a special data type in Python.  They need to be imported from the array library (more on importing later) before being used.  Arrays use less memory than lists of tuples

Arrays are:

- ordered collections of data.
- mutable
- not able to contain objects of different data types.
- accessible by index number.

There are several ways to declare arrays in Python. One such way is this:

```python
import array
a = array.array('i', [1, 3, 4])
```

We import the module array, which has inside of it a method, also called array, that we use to create an array.  we use `'i'`, to declare that this array will hold integers.

Take a look at [this article](https://www.w3schools.com/python/python_ref_list.asp) for methods that we can use with lists and arrays.

#### Dictionaries

Dictionaries in Python are the analogue to JavaScripts's objects or Java's hashmaps. Dictionaries are made up of items, which are key:value pairs.

Dictionaries are:

- changable
- unordered
- not tolerant of duplicates
- can contains any data types

Dictionaries in Python look like this:


```python
car={
	"make":"ford",
	"model":"focus",
	"year":2017
}
```

Quotes in dictionaries can be either single or double.  We can access or write to dictionaries using square brackets.  For example, if we wrote `car['make']`, we would see `"ford"`.  If we wrote `car['color']='blue'`, it would add the key:value pair "color":"blue" to our car dictionary.

A good list of dictionary methods can be viewed [here](https://www.w3schools.com/python/python_dictionaries_methods.asp).

### Indentation

In Python, we use indentation to group sets of lines together into a block.  If we want a set of instructions to run together, be it in a function, a loop, or a conditional, we indent each of those lines to the same position.  The lines introducing a block end with a colon.

### Conditionals

Conditionals in Python work as they do in most other languages, structured in the colon - indented block structure. It uses the keywords if, elif, and else to control the flow of the conditional. Let's look at an example where we check to see if a number whether a number is positive, and makes it positive if it is negative:

```python
if number < 0:
	print('Number is negative')
	number = number * -1
elif number > 0:
	print ('Number is positive')
else:
	print('Number is zero')
```

If we have a single clause condition, we can write it like this:

```
if number < 0 : print('Number is negative')
```

### Loops

In Python, we have the `for` and `while` loops, like in most other languages.  Here, we also use indentation to identify the block of code to run within the loop.  Let's look at a while loop.

```python
numbers = [1,2,3,4,5]
sum=0
i = 0
while i<len(numbers):
	sum+=numbers[i]
	i+=1
	
print(f'The sum of the numbers array is {sum}')
```

For loops in Python may loop a little different than you may have seen. The for statement in Python iterates over an iterable set of data, like a list. It is similar to a forEach function in JavaScript. To find the sum of a list of values, as we did in our while loop, we would write:

```python
numbers = [1,2,3,4,5]
sum=0
for number in numbers:
	sum+=number
	
print(f'The sum of the numbers array is {sum}')
```

If we do need to run a loop a set number of times, as we often do in a for loop, we can use Python's range function, which creates a sequence of numbers

```python
for x in range(5):
	print(x)
```

This function will print 

0
1
2
3
4

We can also use `break` and `continue` in loops to stop the loop, or skip and iteration.  If, within a loop, the `break` command runs, it stops the loop from running and moves to the lines after the loop. If `continue` runs, it skips everything in the loop after `continue`, and moves on to the next iteration of the loop.

### Functions

Functions in Python take several parts:

1. Functions begin with the keyword `def`
2. This is followed with the function name
3. Followed by parenthesis, in which you can include parameters for the function
4. This first line of a function is followed by a colon
5. The set of indented instructions following this is the function body, the block that executes when the function is called

Let's look this function, which created a list of numbers from the fibonacci sequence, up to some number n.

```python
def fibonacci(n):
	'''Gets the first few numbers of the fibonacci sequence'''
	a=0
	b=1
	sequence=[0]
	while b<=n:
		sequence.append(b)
		c=a+b
		a=b
		b=c
	return sequence
```

We can then call this number like this: `fibonacci(100)`

As you can see in the example above, we use the `return` keyword to return a value from the function to where we called it. If we don't use a return statement in a function, it returns 'None" by default.

We can also add an explanatory string about the function as the first line of the function body, called the docstring. The convention for docstrings is to write them in triple quotes.

### Modules

Like in many languages, we can write functions in python files, and import those functions into other files with the use of the Python keyword `import`. Besides our own modules, Python comes with a wide library of standard modules that allow for a lot of different functionality. These modules aren't available by default, to prevent the loading of code that would go unused.

When we do want to use these modules, we just add

	import <module name>
	
in our file.  For a list of available built-in modules, take a look at [this list](https://docs.python.org/3/library/).

## What to Strive for in Python

We've gone over the basics of using Python, and there is a lot more to learn.

Read [this article](https://towardsdatascience.com/how-to-be-pythonic-and-why-you-should-care-188d63a5037e) for information on the philosophy of writing Python.

Check out [this article](https://docs.python-guide.org/writing/style/) for a ton of conventions and some interesting ways Python has of achieving different functions.