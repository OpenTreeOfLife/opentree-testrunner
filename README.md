opentree-testrunner
===================
This repository is intended to house scripts for integration testing of software
produced by the Open Tree of Life effort.

Installation
============

 1. Copy the file "test.conf.example" to "test.conf" 
 2. Open "test.conf" in a text editor and tweak the settings (see below)
 3. cd to the top of the working tree
 4. <code>pip install -r requirements.txt</code>

Usage
=====

    sh run_test.sh


Settings
========
"test.conf" is read using Python's config parser. So to see the syntax rules
refer to http://docs.python.org/library/configparser.html

See the peyotl repo wiki for details on the config options: https://github.com/OpenTreeOfLife/peyotl/wiki/configuration 