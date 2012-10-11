opentree-testrunner
===================
This repository is intended to house scripts for integration testing of software
produced by the Open Tree of Life effort.

Installation and Usage
======================

 1. Copy the file "test.conf.example" to "test.conf" 
 2. Open "test.conf" in a text editor and tweak the settings (see below)
 3. cd to the top of the working tree
 4. <code>sh run_test.sh</code>
 


Settings
========
"test.conf" is read using Python's config parser. So to see the syntax rules
refer to http://docs.python.org/library/configparser.html

Please add a note below if you add an option.


#### "host" Section #####

* `tnrshost` hostname and port for the server running the TNRS services.
