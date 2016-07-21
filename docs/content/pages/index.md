Title: About
Slug: intro
sortorder: 1
Authors: mvr
save_as: index.html
URL:

[//]: # (ALL LINKS ON THIS PAGE MUST BE like pages/foo.html)

[TOC]

<center><img style="border:3px solid black;" src="images/tunl.jpg" style="width:100%;opacity:0.6;filter:alpha(opacity=60);"/></center>

## About tunl

Tunl is a ssh-tunnel manager without a lot of frills.  It has a command-line interface which works any place you have ssh and python.  I wrote this mainly because I wanted dead simple command-line and programmatic access to a ssh-tunnel manager with unsurprising configuration files.  (Also I can't be bothered to remember the ssh command line syntax, and I sure do hate typing)

Tunl is written in python: see [this section](pages/dev.html) for information about using it as a library.

## Installing tunl

Install with pypi:

    $ pip install tunl

Or try the bleeding edge:

    $ git clone https://github.com/mattvonrocketstein/tunl.git
    $ cd tunl
    $ virtualenv venv
    $ source venv/bin/activate
    $ python setup.py develop

## Contributing

**Pull requests and feature requests are welcome**, just use [the githubs](https://github.com/mattvonrocketstein/tunl/issues).

<br/>

**Testing:**  
All tests are run with tox.  Afterwards, you can view the coverage results in the `htmlcov` folder.  Coverage information is also deployed with this document, [see the results here](htmlcov).

    $ pip install tox
    $ tox

<br/>
**Commit hooks**:
To maintain consistent style in the library, please use the same precommit hooks as me.  To install precommit hooks after cloning the source repository, run these commands:

    $ pip install pre-commit
    $ pre-commit install

<br/>
**Documentation:**  
Contributions to this documentation (in the `docs` folder of the source root) are also welcome.  If you make significant changes, run the documentation test-server and the script to check for broken links.

    $ cd docs
    $ pip install -r requirements.txt
    $ fab run # runs the auto-updating test server for the markdown docs

In another terminal, run the crawler script against the test server

    $ fab check_links
