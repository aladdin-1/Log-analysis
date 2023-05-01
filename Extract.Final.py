import re
import os

# Define the regular expression patterns to match the log messages
input_pattern = r'(\d{4}/\w+/\d{2}\s\d{2}:\d{2}:\d{2}\.\d+)\s(\w+)\sPORTEVENT\s(\w+\.ttcn):\d+\(function:(\w+)\)\sReceive\soperation\son\sport\s(\w+)\[(\d+)\]\ssucceeded,\smessage\sfrom\s(\d+):\s@variables\.(\w+)\s:\s{([\s\S]*?)\}\sid\s(\d+)'
output_pattern = r'(\d{4}/\w+/\d{2}\s\d{2}:\d{2}:\d{2}\.\d+)\s(\d+)\sPORTEVENT\s(\w+\.ttcn):\d+\(function:(\w+)\)\sSent\son\ssipInternalPort\sto\s(\w+)\s@variables\.(\w+)\s:\s{([\s\S]*?)\}'

# Set the path to the folder containing the log files
log_folder = 'path\to\log\files'

# Iterate over the log files in the folder
for filename in os.listdir(log_folder):
    if filename.endswith('.txt'):
        # Open the log file and read its contents
        with open(os.path.join(log_folder, filename), 'r') as f:
            log_file = f.read()

        # Use the re.findall() function to extract all matching input and output log messages
        input_messages = re.findall(input_pattern, log_file)
        output_messages = re.findall(output_pattern, log_file)

        # Format and write the matching input messages to a file
        input_file_name = os.path.splitext(filename)[0] + '_input.txt'
        with open(os.path.join(log_folder, input_file_name), 'w') as input_file:
            for message in input_messages:
                date_time, component_id, component_name, function_name, recipient, index, sender, message_type, message_body, msg_id = message
                formatted_message = f"at {date_time} the component {component_id} received a message of type @{message_type} to {recipient} with the body {message_body}"
                input_file.write(formatted_message + '\n')

        # Format and write the matching output messages to a file
        output_file_name = os.path.splitext(filename)[0] + '_output.txt'
        with open(os.path.join(log_folder, output_file_name), 'w') as output_file:
            for message in output_messages:
                date_time, component_id, component_name, function_name, recipient, message_type, message_body = message
                formatted_message = f"at {date_time} the component {component_id} sent a message of type @{message_type} to {recipient} with the body {message_body}"
                output_file.write(formatted_message + '\n')