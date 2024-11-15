# odtp-llm-parser

Add here your badges:
[![Launch in your ODTP](https://img.shields.io/badge/Launch%20in%20your-ODTP-blue?logo=launch)](http://localhost:8501/launch-component)
[![Compatible with ODTP v0.5.x](https://img.shields.io/badge/Compatible%20with-ODTP%20v0.5.0-green)]("")

> [!NOTE]  
> This repository makes use of submodules. Therefore, when cloning it you need to include them.
>  
> `git clone --recurse-submodules https://github.com/odtp-org/odtp-llm-parser`

The component is a Python script that extracts structured information from a text input using the OpenAI API based on a provided JSON schema. It accepts command-line arguments for the OpenAI API key, the JSON schema file path, the text input (either from a file or direct input), and an optional output file path. The script processes the text, calls the OpenAI API to extract information according to the schema, and writes the extracted data to a JSON file.

## Table of Contents

- [Tools Information](#tools-information)
- [How to add this component to your ODTP instance](#how-to-add-this-component-to-your-odtp-instance)
- [Data sheet](#data-sheet)
    - [Parameters](#parameters)
    - [Secrets](#secrets)
    - [Input Files](#input-files)
    - [Output Files](#output-files)
- [Tutorial](#tutorial)
    - [How to run this component as docker](#how-to-run-this-component-as-docker)
    - [Development Mode](#development-mode)
    - [Running with GPU](#running-with-gpu)
    - [Running in API Mode](#running-in-api-mode)
- [Credits and References](#credits-and-references)

## Tools Information

| Tool | Semantic Versioning | Commit | Documentation |
| --- | --- | --- | --- |
| [openai](https://pypi.org/project/openai/) | v1.54.4 | --- | [API Reference](https://platform.openai.com/docs/api-reference/introduction?lang=python)  |

## How to add this component to your ODTP instance

In order to add this component to your ODTP CLI, you can use. If you want to use the component directly, please refer to the docker section. 

``` bash
odtp new odtp-component-entry \
--name odtp-llm-parser \
--component-version v0.0.1 \
--repository https://github.com/sdsc-ordes/odtp-llm-parser 
```

## Data sheet

### Parameters

No Parameters

### Secrets

| Secret Name | Description | Type | Required | Default Value | Constraints | Notes |
| | OPENAI_KEY | OpenAI API key used for authentication | string | yes | None | Must be a valid OpenAI API key | Required for accessing OpenAI API |

### Input Files

### Input Files

| File/Folder | Description | File Type | Required | Format | Notes |
| --- | --- | --- | --- | --- | --- |
| schema.json | JSON schema file that defines the structure for information extraction | .json | Yes | JSON | Must be a valid JSON schema |
| input.txt | Text file containing the content to extract information from | .txt | Yes | Text | Plain text file |

### Output Files

| File/Folder | Description | File Type | Contents | Usage |
| --- | --- | --- | --- | --- |
| output.json | Extracted structured information | .json | JSON data following schema | Contains extracted data |

## Tutorial

### How to run this component as docker

Build the dockerfile.

``` bash
docker build -t odtp-llm-parser .
```

Run the following command. Mount the correct volumes for input/output/logs folders.

``` bash
docker run -it --rm \
-v {PATH_TO_YOUR_INPUT_VOLUME}:/odtp/odtp-input \
-v {PATH_TO_YOUR_OUTPUT_VOLUME}:/odtp/odtp-output \
-v {PATH_TO_YOUR_LOGS_VOLUME}:/odtp/odtp-logs \
--env-file .env odtp-llm-parser
```

### Development Mode

To run the component in development mode, mount the app folder inside the container:

``` bash
docker run -it --rm \
-v {PATH_TO_YOUR_INPUT_VOLUME}:/odtp/odtp-input \
-v {PATH_TO_YOUR_OUTPUT_VOLUME}:/odtp/odtp-output \
-v {PATH_TO_YOUR_LOGS_VOLUME}:/odtp/odtp-logs \
-v {PATH_TO_YOUR_APP_FOLDER}:/odtp/app \
--env-file .env odtp-llm-parser
```

### Running with GPU 

To run the component with GPU support, use the following command:

``` bash
docker run -it --rm \
--gpus all \
-v {PATH_TO_YOUR_INPUT_VOLUME}:/odtp/odtp-input \
-v {PATH_TO_YOUR_OUTPUT_VOLUME}:/odtp/odtp-output \
-v {PATH_TO_YOUR_LOGS_VOLUME}:/odtp/odtp-logs \
--env-file .env odtp-llm-parser
```

### Running in API Mode

To run the component in API mode and expose a port, use the following command:

``` bash
docker run -it --rm \
-v {PATH_TO_YOUR_INPUT_VOLUME}:/odtp/odtp-input \
-v {PATH_TO_YOUR_OUTPUT_VOLUME}:/odtp/odtp-output \
-v {PATH_TO_YOUR_LOGS_VOLUME}:/odtp/odtp-logs \
-p 7860:7860 \
--env-file .env \
--entrypoint python3 \
odtp-llm-parser \
/odtp/odtp-app/gradio_api.py
```

## Credits and references

SDSC

This component has been created using the `odtp-component-template` `v0.5.0`. 


docker run -it --rm -p 7860:7860 --env-file .env --entrypoint python3 odtp-llm-parser /odtp/odtp-app/gradio_app.py