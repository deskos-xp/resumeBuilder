#! /usr/bin/env bash

for f in `ls -1 Previews` ; do 
	echo '![Alt text]'"(Previews/$f?raw=true \"Preview $f\")" >> README.md
done
