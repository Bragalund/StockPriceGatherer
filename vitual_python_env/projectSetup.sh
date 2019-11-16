#!/bin/zsh
pip3 install virtualenv
virtualenv myNewVirtualenv                  # create new virtual environment for dependencies to be stored in
cd myNewVirtualenv
source bin/activate                         # activate virtual environment
pip3 install scrapy                         # install scrapy(webcrawler-framework) within virtual environment
scrapy startproject aftenposteentestproject # create scrapy-project structure