#! /usr/bin/env bash

d=`date +%H.%M.%S_%m-%d-%y`
mkdir .backups/backup-$d
cp -rv ./icons ./templates ./lib ./ui ./widgets_lib resume_builder.py .backups/backup-$d
extras=('todos.txt' 'readme.txt' 'backup.sh')
for doc in ${extras[@]} ; do
	if test -e $doc && test -f $doc ; then
		cp $doc .backups/backup-$d
	fi
done
tree .backups/backup-$d

cd ..

if test "$1" != '' ; then
	scp -r resume-builder carl@"$1":/home/carl/
fi

tar -Jcvf resume-builder-$d.tar.xz resume-builder 
ls -lh resume-builder-$d.tar.xz 
cd resume-builder
