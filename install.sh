#! /usr/bin/env bash

function install(){
	if test "`whoami`" == "root" ; then
		if test "$1" == "install" ; then
			cp -r resume-builder /opt/
			cp /opt/resume-builder/resumeBuilder.desktop /usr/share/applications/
			cp /opt/resume-builder/icons/png/resume-builder.png /usr/share/icons/
		elif test "$1" == "remove" ; then
			rm -r /opt/resume-builder
			rm /usr/share/applications/resumeBuilder.desktop /usr/share/icons/resume-builder.png
		else
			printf "./install.sh [install|remove]\n"
		fi
	else
		printf "user '%s' is not root\n" "`whoami`"
	fi
}
install "$@"
