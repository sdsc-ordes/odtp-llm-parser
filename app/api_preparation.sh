#!/bin/bash

# When running this component in API mode this script will run only once at the beginning of the component. 
# It's made to install the tool, download the model or do some other preparation work


# This is an example: Install jq and download a sample JSON file

# Install jq (a lightweight and flexible command-line JSON processor)
if ! command -v jq &> /dev/null
then
    echo "jq could not be found, installing..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update && sudo apt-get install -y jq
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install jq
    else
        echo "Unsupported OS. Please install jq manually."
        exit 1
    fi
else
    echo "jq is already installed"
fi

# Download a sample JSON file
echo "Downloading sample JSON file..."
curl -o sample.json https://jsonplaceholder.typicode.com/todos/1

echo "Preparation complete."