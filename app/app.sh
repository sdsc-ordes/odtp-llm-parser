#!/bin/bash

# Run the extraction using app.py
python3 /odtp/odtp-app/app.py \
  --api_key $OPENAI_KEY \
  --schema /odtp/odtp-input/schema.json \
  --text /odtp/odtp-input/input.txt \
  --output /odtp/odtp-output/output.json