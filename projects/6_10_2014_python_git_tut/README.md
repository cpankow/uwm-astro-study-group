# Week 1 (6/10/2014) -- Python/Git Tutorial

 * Presenters: Chris Pankow (chris.p.pankow (at) g + mail , com)
 * Topics: Introduction to python and version control with git

## Preliminaries

Each week will have a basic overview set of notes which accompany any relevant code examples or presentations for that week. This file represents the overview for this week. It is written in a very basic stylization of HTML called [Markdown](http://daringfireball.net/projects/markdown/). If you've ever edited a wiki page or something like that, you will have seen other flavors of this. There are a few usage tutorials: [from the creators](http://daringfireball.net/projects/markdown/syntax), [from github](https://help.github.com/articles/markdown-basics), [and their differences](https://help.github.com/articles/github-flavored-markdown). If you view a markdown code file (typically suffixed with ".md") on github, it will automatically render it for you (see for example, our [front page](https://github.com/cpankow/uwm-astro-study-group/blob/master/README.md)).

### Using Markdown with GitHub

[github](github.com), which you are presumably using to view this will be our main code staging and sharing area. It is basically a repository host with a lot of extra features. You'll note that the markdown used on github can be integrated with the features on this site. A few cursory examples:

 * Refer to a commit: d98132b19ea98f2dbeb7349cef16e7a0078e7255
 * Paste a syntax highlighted set of code:

```python
print "...ain't it cool?"
```

...there's much more, but we'll go over git basics before we dive into its full integration with github.

### Issue Tracker

Every github repository comes with its own issue tracker. While we may not make frequent use of this, it could find use as we commit our examples and find bugs or improvements. Our specific issue tracker is [here](https://github.com/cpankow/uwm-astro-study-group/issues). The issue descriptions and comments all use markdown and the tricks above to make life easier for everyone.

## Python

In a nutshell:

 * http://xkcd.com/353/
 * http://legacy.python.org/dev/peps/pep-0020/
  * OR ```python
import this
```

...the book (Appendix A) does a good job of describing the highlights of python and the various subpackages, and I'll go over some of it, as well as expand a little on why things are the way they are. Stylistically speaking, we'll try as much as possible to adhere to [PEP8](http://legacy.python.org/dev/peps/pep-0008/) style guidelines. Don't worry too much if you don't always, but do try and make a good faith effort. You'd be surprised how much good formatting helps in the understanding and reuse of code. If you don't want to read any of that, do the following:

 * 4 spaces, no tabs to indent
 * Try to break comments and long lines up if possible (79 characters usually)
 * use variable_name and ClassName styling
 * be consistent with previously written code whenever possible

Almost all the examples in the book look as if they came from the [ipython](ipython.org) interpreter. ipython is an enhancement of the [REPL](https://en.wikipedia.org/wiki/REPL) (Read Evalulate Print Loop) interpreter which you can get by just typing ```python``` at the command line. It has good integration with the toolkits we'll be using, such as matplotlib, numpy. and scipy. It also has excellent docstring help built in --- try the following example at an ipython prompt:

```
In [0]: ?list
```

You can also do a double question mark (```??```) or use the ```help``` function, like so:

```
In [0]: help(list)
```

If you want to take things just a little further, I'd suggest looking into the [ipython notebook](http://ipython.org/notebook.html). If you're familiar with Mathematica notebooks, these are similar. If you're not, you can think of the ipython notebook as a way to make a shareable webpage out of an ipython session, complete with plots and tables of results. It's very handy for scientification. Here's a tutorial [video](http://youtu.be/H6dLGQw9yFQ).

## Getting Set Up

You'll need a number of software packages to really get started. Luckily, many of these can be installed quite easily.

### Mac OS X

For OS X, I recommend [MacPorts](https://www.macports.org/). Then find the package you want (python packaged tend to be prefixed by their python version --- e.g. py27):

    port search astroML
    py-astroML @0.2 (python, science)
        tools for machine learning and data mining in astronomy

    py26-astroML @0.2 (python, science)
        tools for machine learning and data mining in astronomy

    py27-astroML @0.2 (python, science)
        tools for machine learning and data mining in astronomy

    Found 3 ports.

and install it (note the ```sudo``` sitting in front, indicating that you're installing to system locations and will need to enter your password --- this is usually required).

    sudo port install py27-astroML
    Password:
    --->  Computing dependencies for py27-astroML
    --->  Fetching archive for py27-astroML
    --->  Attempting to fetch py27-astroML-0.2_0.darwin_11.x86_64.tbz2 from http://packages.macports.org/py27-astroML
    --->  Attempting to fetch py27-astroML-0.2_0.darwin_11.x86_64.tbz2.rmd160 from http://packages.macports.org/py27-astroML
    --->  Installing py27-astroML @0.2_0
    --->  Activating py27-astroML @0.2_0
    --->  Cleaning py27-astroML
    --->  Updating database of binaries
    --->  Scanning binaries for linking errors
    --->  No broken files found. 

Depending on what you have already installed with port, your output may look different, but the last few lines should be similar to what I have. Some packages have many dependencies and this process could take a long time to finish.

## Debian

The package manager for Debian is (apt)[https://wiki.debian.org/Apt). Searching for packages looks like

    $ apt-cache search python-astropy

Debian tends to prefix python packages with ````python-```. Installing is slightly different:

    $ apt-get install python-astropy

## Other OSs

### Ubuntu

Ubuntu is a Debian variant, you can use the ```apt-``` commands from above, or use a graphical front end like ```aptitude```.

### Scientific Linux

SL is a variant of the RedHat Linux distribution. In general, it uses the ```yum``` package installer. If necessary, I'll post instructions on how to use this tool.

### Windows

Windows has its own command line terminal emulator, but it's sufficiently different from POSIX-compliant (e.g. the style of command line terminals available on OSX and Linux) that it will be hard for you to follow some of the things we're doing here. I'll recommend installing a POSIX compliant environment like [cygwin](http://www.cygwin.com/). Even then, it can be a pain to get all the things you need. In the end, I'd recommend using a Linux based environment. Linux has become sophisticated enough that you can run it in a [Virtual Machine](https://www.virtualbox.org/) (VM) and Ubuntu even has its own "Windows application" called [Wubi](https://wiki.ubuntu.com/WubiGuide).

## Miscellania

 * Web-based python interpreter (and more): http://ideone.com/
 * Line by line debugging? (see the [reference page](https://docs.python.org/2/library/pdb.html))
    python -m pdb name_of_script
 * Code editors: [emacs](https://www.gnu.org/software/emacs/) --- good, [vim](http://www.vim.org/) -- bestest
  * But see also: http://mrozekma.com/editor-learning-curve.png
 * Which shell to use? I like [zsh](http://www.zsh.org/), but you need [more](https://github.com/robbyrussell/oh-my-zsh). Never... ever... and I mean ever use (t)csh. No one likes that guy.
  * If the above question is not understandable or irrelevant, you're using bash, and that's okay.
 * Getting help: try stackoverflow.com , but make sure you search their question base first. 99% of the time, your question has already been thoroughly answered.
