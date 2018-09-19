#! /usr/bin/env bash

function main(){
	packages=('python3-pyqt5' 'python3-lxml' 'ttf-mscorefonts-installer' 'python3-pip' 'python3-setuptools' 'python3-lxml')
	sudo apt-get install $packages
	sudo ln -s /bin/bash /usr/bin/bash
	pip3 install reportlab

}
main
