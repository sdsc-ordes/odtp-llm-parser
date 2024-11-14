# Name of the component

Add here your badges:
[![Launch in your ODTP](https://img.shields.io/badge/Launch%20in%20your-ODTP-blue?logo=launch)](http://localhost:8501/launch-component)
[![Compatible with ODTP v0.5.x](https://img.shields.io/badge/Compatible%20with-ODTP%20v0.5.0-green)]("")

> [!NOTE]  
> This repository makes use of submodules. Therefore, when cloning it you need to include them.
>  
> `git clone --recurse-submodules https://github.com/odtp-org/odtp-component-xxxxx`

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

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
| [Tool 1](link-to-repository-1) | vX.Y.Z | [commit-hash-1](link-to-commit-hash-1) | [Documentation 1](link-to-doc-1)  [Documentation 2](link-to-doc-2) |
| [Tool 2](link-to-repository-2) | vA.B.C | [commit-hash-2](link-to-commit-hash-2) | [Documentation 2](link-to-doc-2) |

## How to add this component to your ODTP instance

In order to add this component to your ODTP CLI, you can use. If you want to use the component directly, please refer to the docker section. 

``` bash
odtp new odtp-component-entry \
--name odtp-component \
--component-version v0.0.1 \
--repository Link to repository \
--image Link to dockerhub image \
```

## Data sheet

### Parameters

| Parameter | Description | Type | Required | Default Value | Possible Values | Constraints |
| --- | --- | --- | --- | --- | --- | --- |
| A | B | C | D | E | F | G |

### Secrets

| Secret Name | Description | Type | Required | Default Value | Constraints | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| A | B | C | D | E | F | G |

### Input Files

| File/Folder | Description | File Type | Required | Format | Notes |
| --- | --- | --- | --- | --- | --- |
| A | B | C | D | E | F |

### Output Files

| File/Folder | Description | File Type | Contents | Usage |
| --- | --- | --- | --- | --- |
| A | B | C | D | E |

## Tutorial

### How to run this component as docker

Build the dockerfile.

``` bash
docker build -t odtp-component .
```

If you need to pass build arguments, use the `--build-arg` flag:

``` bash
docker build -t odtp-component --build-arg ARG_NAME=ARG_VALUE .
```

Run the following command. Mount the correct volumes for input/output/logs folders.

``` bash
docker run -it --rm \
-v {PATH_TO_YOUR_INPUT_VOLUME}:/odtp/odtp-input \
-v {PATH_TO_YOUR_OUTPUT_VOLUME}:/odtp/odtp-output \
-v {PATH_TO_YOUR_LOGS_VOLUME}:/odtp/odtp-logs \
--env-file .env odtp-component
```

### Development Mode

To run the component in development mode, mount the app folder inside the container:

``` bash
docker run -it --rm \
-v {PATH_TO_YOUR_INPUT_VOLUME}:/odtp/odtp-input \
-v {PATH_TO_YOUR_OUTPUT_VOLUME}:/odtp/odtp-output \
-v {PATH_TO_YOUR_LOGS_VOLUME}:/odtp/odtp-logs \
-v {PATH_TO_YOUR_APP_FOLDER}:/odtp/app \
--env-file .env odtp-component
```

### Running with GPU

To run the component with GPU support, use the following command:

``` bash
docker run -it --rm \
--gpus all \
-v {PATH_TO_YOUR_INPUT_VOLUME}:/odtp/odtp-input \
-v {PATH_TO_YOUR_OUTPUT_VOLUME}:/odtp/odtp-output \
-v {PATH_TO_YOUR_LOGS_VOLUME}:/odtp/odtp-logs \
--env-file .env odtp-component
```

### Running in API Mode

To run the component in API mode and expose a port, use the following command:

``` bash
docker run -it --rm \
-v {PATH_TO_YOUR_INPUT_VOLUME}:/odtp/odtp-input \
-v {PATH_TO_YOUR_OUTPUT_VOLUME}:/odtp/odtp-output \
-v {PATH_TO_YOUR_LOGS_VOLUME}:/odtp/odtp-logs \
-p {HOST_PORT}:{CONTAINER_PORT} \
--env-file .env odtp-component
```

## Credits and references

XXXXXXXXXX

This component has been created using the `odtp-component-template` `v0.5.0`. 