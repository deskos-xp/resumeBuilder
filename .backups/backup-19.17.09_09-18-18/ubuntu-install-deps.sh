#! /usr/bin/env bash

function main(){
	packages=('python3-pyqt5' 'python3-lxml' 'ttf-mscorefonts-installer' 'python3-pip' 'python3-setuptools' 'python3-lxml')
	sudo apt-get install $packages
	pip3 install reportlab

}
main
