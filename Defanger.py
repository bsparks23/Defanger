import re

# Defangs IP addresses/domains based on a regex pattern. Once the regex pattern matches, the lambda function is applied and performs the replacement/defanging
def defang_text(input_text):
    
    defanged_ip = re.sub(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', lambda x: x.group(0).replace('.', '[.]'), input_text)

    defanged_domain = re.sub(r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b', lambda x: x.group(0).replace('.', '[.]'), defanged_ip)
    
    return defanged_domain

def process_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        defanged_text = defang_text(text)
    return defanged_text

def main():
    # Update with your input file
    input_filename = "input.txt" 
    output_filename = "defanged_output.txt" 

    defanged_text = process_file(input_filename)

    if defanged_text:  
        with open(output_filename, 'w') as output_file:
            output_file.write(defanged_text)
        print("Text defanged and saved to:", output_filename)
    else:
        print("Error: Failed to defang text. Please ensure there is data to parse and that your file is named:", input_filename + ". No output file was created.")

if __name__ == "__main__":
    main()