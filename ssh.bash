#!/bin/bash

eval $(ssh-agent)
echo "Verified ssh agent is running."

DIRECTORY=$(PWD)
echo DIRECTORY

cd ~/.ssh
ssh-add "github"

cd $DIRECTORY

git pull
