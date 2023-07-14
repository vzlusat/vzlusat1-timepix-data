#!/bin/bash

# get the path to this script
MY_PATH=`dirname "$0"`
MY_PATH=`( cd "$MY_PATH" && pwd )`

cd $MY_PATH

echo "Unpacking all VZLUSAT-1 data"
tar -xvzf all.tar.gz
