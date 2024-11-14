#!/bin/bash

# This is the script that will run when the API is called. Here the tool won't take the parameters from the env variables
# but rather it will accept them as arguments with flags and possitional ones. 

# TODO: Define general strategy to deal with files internally on APIs. What happens when the task is huge? We need an alternative

# This is an example: 

# Usage: ./api_task.sh -f <flag_argument> <positional_argument>

while getopts ":f:" opt; do
    case $opt in
        f)
            flag_argument=$OPTARG
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            exit 1
            ;;
    esac
done
shift $((OPTIND -1))

positional_argument=$1

echo "Flag argument: $flag_argument"
echo "Positional argument: $positional_argument"