import gradio as gr
import openai
import tempfile
import os
import json
import requests

def process_inputs(
    json_input_method,
    openai_api_key,
    json_file=None,
    json_url=None,
    json_text=None,
    text_input_method=None,
    text_file=None,
    text_url=None,
    text_input=None,
):
    # Check if OpenAI API key is provided
    if not openai_api_key:
        return "OpenAI API key is required.", None

    # Create temporary folders
    temp_dir = tempfile.mkdtemp()
    input_dir = os.path.join(temp_dir, "input")
    output_dir = os.path.join(temp_dir, "output")
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    # Process JSON Schema input
    if json_input_method == "File Upload" and json_file is not None:
        json_schema_path = json_file.name
        with open(json_schema_path, 'r') as f:
            json_schema = f.read()
    elif json_input_method == "URL" and json_url:
        response = requests.get(json_url)
        if response.status_code == 200:
            json_schema = response.text
        else:
            return "Failed to download JSON schema from URL.", None
    elif json_input_method == "Text Input" and json_text:
        json_schema = json_text
    else:
        return "No JSON schema provided.", None
    
    # Process Text input
    if text_input_method == "File Upload" and text_file is not None:
        text_path = text_file.name
        with open(text_path, 'r') as f:
            text_content = f.read()
    elif text_input_method == "URL" and text_url:
        response = requests.get(text_url)
        if response.status_code == 200:
            text_content = response.text
        else:
            return "Failed to download text from URL.", None
    elif text_input_method == "Text Input" and text_input:
        text_content = text_input
    else:
        return "No text provided.", None
    
    # Set OpenAI API key and create client
    client = openai.OpenAI(api_key=openai_api_key)

    # Construct the prompt
    prompt = f"""
    You are an assistant that extracts information from text and structures it according to a given JSON schema.

    Given the following text:

    {text_content}

    Extract the relevant information and provide it in the following JSON schema format:

    {json_schema}

    Ensure that the output is valid JSON and follows the schema exactly.

    Provide only the JSON output, and no additional text.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that extracts information from text and structures it according to a given JSON schema."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2048,
            temperature=0.0,
        )
        output_json = response.choices[0].message.content
    except Exception as e:
        return f"OpenAI API error: {str(e)}", None
    
    # Try to parse the output_json to ensure it's valid JSON
    try:
        parsed_output = json.loads(output_json)
        output_json_str = json.dumps(parsed_output, indent=2)
    except json.JSONDecodeError as e:
        return f"Failed to parse JSON output from OpenAI: {str(e)}\n\nRaw output:\n{output_json}", None
    
    # Save output to file
    output_file_path = os.path.join(output_dir, "output.json")
    with open(output_file_path, 'w') as f:
        f.write(output_json_str)
    
    # Return output_json_str and provide download link
    return parsed_output, output_file_path

# Define the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Extract Information and Structure it According to a JSON Schema")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### JSON Schema Input")
            json_input_method = gr.Radio(["File Upload", "URL", "Text Input"], label="JSON Schema Input Method", value="File Upload")
            json_file = gr.File(label="Upload JSON Schema File", visible=True, file_types=[".json", ".txt"])
            json_url = gr.Textbox(label="Enter URL for JSON Schema", visible=False)
            json_text = gr.Textbox(label="Enter JSON Schema Text", visible=False, lines=10)
        with gr.Column(scale=1):
            gr.Markdown("### Text Input")
            text_input_method = gr.Radio(["File Upload", "URL", "Text Input"], label="Text Input Method", value="File Upload")
            text_file = gr.File(label="Upload Text File", visible=True, file_types=[".txt"])
            text_url = gr.Textbox(label="Enter URL for Text", visible=False)
            text_input = gr.Textbox(label="Enter Text", visible=False, lines=10)
    
    # Bottom section - API key and submit
    with gr.Row():
        with gr.Column(scale=2):
            # Add this where other UI components are defined
            use_env_key = gr.Checkbox(
                label="Use OpenAI API key from environment variable if available (OPENAI_KEY)", 
                value=False
            )

            openai_api_key = gr.Textbox(
                label="OpenAI API Key",
                placeholder="Enter your OpenAI API key or check box above to use environment variable",
                type="password"
            )
            
            submit_button = gr.Button("Submit")
    
            output_json = gr.JSON(label="Output")
            download_button = gr.File(label="Download Output JSON", visible=False)
    
    def update_json_input_visibility(method):
        if method == "File Upload":
            return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)
        elif method == "URL":
            return gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)
        elif method == "Text Input":
            return gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)
    
    json_input_method.change(
        update_json_input_visibility,
        inputs=json_input_method,
        outputs=[json_file, json_url, json_text]
    )
    
    def update_text_input_visibility(method):
        if method == "File Upload":
            return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)
        elif method == "URL":
            return gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)
        elif method == "Text Input":
            return gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)
    
    text_input_method.change(
        update_text_input_visibility,
        inputs=text_input_method,
        outputs=[text_file, text_url, text_input]
    )


    
    def run_process_inputs(
        json_input_method,
        json_file,
        json_url,
        json_text,
        text_input_method,
        text_file,
        text_url,
        text_input,
        openai_api_key,
        use_env_key
    ):
        # Handle API key logic
        if use_env_key:
            openai_api_key = os.getenv('OPENAI_KEY', '')

            if not openai_api_key:
                return {"error": "OPENAI_KEY environment variable not found"}, gr.update(visible=False)
        else:
            if not openai_api_key or openai_api_key.strip() == "":
                return {"error": "OpenAI API key is required"}, gr.update(visible=False)
    
        output_json_dict, output_file_path = process_inputs(
            json_input_method,
            openai_api_key,
            json_file,
            json_url,
            json_text,
            text_input_method,
            text_file,
            text_url,
            text_input,
        )
        if output_file_path:
            return output_json_dict, gr.update(value=output_file_path, visible=True)
        else:
            return {"error": output_json_dict}, gr.update(visible=False)
    
    submit_button.click(
        run_process_inputs,
        inputs=[
            json_input_method,
            json_file,
            json_url,
            json_text,
            text_input_method,
            text_file,
            text_url,
            text_input,
            openai_api_key,
            use_env_key 
        ],
        outputs=[output_json, download_button],
        api_name="/run_process_inputs"  # Expose this function via API
    )
    
demo.launch(server_name="0.0.0.0")
