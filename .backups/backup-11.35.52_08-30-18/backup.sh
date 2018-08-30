#! /usr/bin/env bash

d=`date +%H.%M.%S_%m-%d-%y`
mkdir -p .backups/backup-$d
cp -rv ./resume-builder .backups/backup-$d
extras=('backup.sh'  'LICENSE'  'README.md')
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

tar -Jcvf resume-builder-$d.tar.xz resumeBuilder 
ls -lh resume-builder-$d.tar.xz
cd resumeBuilder
