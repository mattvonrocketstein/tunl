Title: Contributing
Slug: contributing
sortorder: 7
Authors: mvr

[TOC]

Github is [here](https://github.com/mattvonrocketstein/tunl).  Pull requests welcome.


### Tests

To run the unittests:

    $ cd tunl
    $ source venv/bin/activate
    $ pip install tox
    $ tox


### Documentation

This documentation is built with pelican.  Edit the markdown files in docs/content/pages, and use the commands below to run and preview the rendered content on the test-server.

    $ cd tunl/docs
    $ fab run

