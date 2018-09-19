#! /usr/bin/env bash

git add .
git commit -am "updates"

d=`date +%H.%M.%S_%m-%d-%y`
mkdir -p .backups/backup-$d
cp -rv ./Previews ./resume-builder .backups/backup-$d
extras=('backup.sh'  'LICENSE'  'README.md' 'update.sh' 'install.sh' 'manjaro-deps.txt' 'arch-deps.txt' 'ubuntu-install-deps.sh')
for doc in ${extras[@]} ; do
	if test -e $doc && test -f $doc ; then
		cp $doc .backups/backup-$d
	fi
done
tree .backups/backup-$d

cd ..

if test "$1" != '' ; then
	ssh carl@"$1" "rm -r /home/carl/resumeBuilder"
	scp -r resumeBuilder carl@"$1":/home/carl/
fi

tar -Jcvf resume-builder-$d.tar.xz resumeBuilder 
ls -lh resume-builder-$d.tar.xz
cd resumeBuilder
