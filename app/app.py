import argparse
import openai
import json
import sys
from typing import Any, Dict

def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description='Extract information from text using OpenAI and output JSON.')
    parser.add_argument('--api_key', type=str, required=True, help='OpenAI API key.')
    parser.add_argument('--schema', type=str, required=True, help='JSON schema file path.')
    parser.add_argument('--text', type=str, required=True, help='Text file path or direct text input.')
    parser.add_argument('--output', type=str, default='output.json', help='Output JSON file path.')
    return parser.parse_args()

def load_json_schema(schema_path: str) -> Dict[str, Any]:
    """
    Load the JSON schema from a file.

    Args:
        schema_path (str): Path to the JSON schema file.

    Returns:
        Dict[str, Any]: Loaded JSON schema.

    Raises:
        Exception: If the schema file cannot be loaded.
    """
    try:
        with open(schema_path, 'r') as f:
            json_schema = json.load(f)
        return json_schema
    except Exception as e:
        print(f"Error loading JSON schema: {e}")
        sys.exit(1)

def load_text_input(text_input: str) -> str:
    """
    Load text input from a file or return the direct text.

    Args:
        text_input (str): Path to the text file or direct text input.

    Returns:
        str: The text content to process.
    """
    try:
        with open(text_input, 'r') as f:
            return f.read()
    except FileNotFoundError:
        # If file not found, assume text is direct input
        return text_input
    except Exception as e:
        print(f"Error reading text input: {e}")
        sys.exit(1)

def call_openai_api(api_key: str, json_schema: Dict[str, Any], text_input: str) -> Dict[str, Any]:
    """
    Call the OpenAI API to extract information based on the JSON schema.

    Args:
        api_key (str): OpenAI API key.
        json_schema (Dict[str, Any]): JSON schema for extraction.
        text_input (str): Text content to process.

    Returns:
        Dict[str, Any]: Extracted data as per the schema.

    Raises:
        Exception: If the API call fails.
    """
    openai.api_key = api_key

    messages = [
        {"role": "system", "content": "You are a helpful assistant that extracts information based on a JSON schema."},
        {"role": "user", "content": text_input}
    ]

    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo-0613',  # or 'gpt-4-0613' if available and needed
            messages=messages,
            functions=[
                {
                    "name": "extract_information",
                    "description": "Extract information according to the schema.",
                    "parameters": json_schema
                }
            ],
            function_call={"name": "extract_information"}
        )

        # Extract the arguments from the function call
        output = response['choices'][0]['message']['function_call']['arguments']
        data = json.loads(output)
        return data
    except Exception as e:
        print(f"Error during API call: {e}")
        sys.exit(1)

def write_output(data: Dict[str, Any], output_path: str) -> None:
    """
    Write the extracted data to a JSON file.

    Args:
        data (Dict[str, Any]): Extracted data.
        output_path (str): Path to the output JSON file.
    """
    try:
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Extraction complete. Output saved to {output_path}")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

def main():
    args = parse_arguments()
    json_schema = load_json_schema(args.schema)
    text_input = load_text_input(args.text)
    extracted_data = call_openai_api(args.api_key, json_schema, text_input)
    write_output(extracted_data, args.output)

if __name__ == '__main__':
    main()
