#!/bin/bash

eval $(ssh-agent)
echo "Verified ssh agent is running."

DIRECTORY=$(PWD)
echo DIRECTORY

cd ~/.ssh
ssh-add "github"

cd $DIRECTORY

if [ $1 == "pull" ]; then 
	git pull
fi
if [ $1 == "push" ];
then
	if [ "$2" != "" ]; 
	then 
		git add .
		git commit -m "$2"
		git push
	fi
fi
