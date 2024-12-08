import json
import re
from transformers import pipeline

# Load the translation model
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")

def is_code_block(line):
    code_patterns = [
        r"```",  # Markdown code block markers
        r"=>",   # Lambda or result mapping
        r"^[\s]*def ",  # Function definitions
        r"^[\s]*\d+\.",  # Line numbers in code (e.g., "1. def func")
        r"^[\s]*[A-Za-z0-9_]+\(",  # Function calls
        r"^[\s]*[\[\{]",  # JSON-like structures or lists
        r"^[\s]*</?[A-Za-z0-9_-]+>",  # HTML/XML-like tags
    ]
    for pattern in code_patterns:
        if re.search(pattern, line):
            return True
    return False

def translate_text(content):
    lines = content.split("\n")
    translated_lines = []
    inside_code_block = False
    
    for line in lines:
        if "```" in line:
            inside_code_block = not inside_code_block
            translated_lines.append(line)
            continue
        
        if inside_code_block or is_code_block(line):
            translated_lines.append(line)
        else:
            translation = translator(line, max_length=2048)
            translated_lines.append(translation[0]['translation_text'])
    
    return "\n".join(translated_lines)

def translate_jsonl_file(input_path, output_path):
    i = 0
    with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
        for line in infile:
            if line.strip():  # Skip empty lines
                data = json.loads(line)
                print(f"traslating line {i}")
                for message in data.get("messages", []):
                    if "content" in message:
                        message["content"] = translate_text(message["content"])
                print(f"line traslated {i}")
                i+=1
                outfile.write(json.dumps(data, ensure_ascii=False) + "\n")

input_file = "input.jsonl"
output_file = "output.jsonl"

translate_jsonl_file(input_file, output_file)

print(f"Translation complete. Translated file saved to {output_file}.")
