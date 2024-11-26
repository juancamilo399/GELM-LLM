import json
import os

# Function to process input text files and convert them to JSONL format
def format_folder_to_jsonl(input_folder, output_file):
    # Open the output file once for writing
    with open(output_file, 'w') as outfile:
        # Iterate over all files in the input folder
        for filename in os.listdir(input_folder):
            if filename.endswith('.txt'):  # Process only .txt files
                file_path = os.path.join(input_folder, filename)
                
                # Read the content of the current file
                with open(file_path, 'r', encoding='utf8') as infile:
                    content = infile.read()
                
                # Splitting the input into sections
                try:
                    problem = content.split("<problem>")[1].split("</problem>")[0].strip()
                    bug_code = content.split("<bug_code>")[1].split("</bug_code>")[0].strip()
                    bug_desc = content.split("<bug_desc>")[1].split("</bug_desc>")[0].strip()
                    bug_fixes = content.split("<bug_fixes>")[1].split("</bug_fixes>")[0].strip()
                    unit_tests = content.split("<unit_tests>")[1].split("</unit_tests>")[0].strip()
                    stu_desc = content.split("<stu_desc>")[1].split("</stu_desc>")[0].strip()
                    dialogue = content.split("<dialogue>")[1].split("</dialogue>")[0].strip()
                except IndexError:
                    print(f"Error parsing file {filename}. Ensure all tags are present.")
                    continue
                
                # Formatting dialogue as a list of messages
                messages = [{"role": "system", "content": "You are a tutor that teaches with the Socratic method. You should guide the student to the answer and don't give it directly."}]
                i = 0
                dialogues = dialogue.split("\n")
                for line in dialogues:
                    if line.startswith("User:"):
                        if i == 0:
                            msg = line.replace("User:", "").strip()
                            messages.append({"role": "user", "content": f"{bug_code} {msg}"})
                        else:
                            messages.append({"role": "user", "content": line.replace("User:", "").strip()})
                    elif line.startswith("Assistant:"):
                        messages.append({"role": "assistant", "content": line.replace("Assistant:", "").strip()})
                    i += 1
                if messages[-1]["role"] == "user":
                    messages.pop()
                
                # Creating the JSON object
                json_object = {
                    "messages": messages
                }
                
                # Writing the JSON object to the JSONL file
                json.dump(json_object, outfile)
                outfile.write('\n')


# Convert the input text files in the folder to JSONL
format_folder_to_jsonl("datasets/train", "train.jsonl")
