# Log Analysis
This project focuses on log analysis of communication between network nodes. The main objectives of the project are to extract message types, message data structures, and constraints from the logs and create valid messages using mutational and generation-based fuzzing techniques.

## 1. Script to Extract Message Types
The script provided in this project allows you to extract message types from log files. It utilizes regular expressions and file processing to identify and extract input and output log messages. The script follows these steps:

- Define regular expression patterns to match the log messages.
- Set the path to the folder containing the log files.
- Iterate over the log files in the folder. 
- Open each log file, read its contents, and check if it is empty.
- Use regular expressions to extract input and output log messages.
- Write the extracted input and output messages to separate files.

## 2. Machine Learning Module
The machine learning module included in this project provides functionality for tokenizing texts, preprocessing them for model input, creating a model architecture, and creating inference models for encoding and decoding sequences. The module utilizes the Keras library with TensorFlow backend for building and training the model. The module consists of the following functions:

**tokenize_texts(texts, num_words)**: This function tokenizes the input texts and creates a tokenizer object. The tokenizer is fitted on the texts to generate the vocabulary and assign unique indices to each word.

**read_text_file(file_path)**: This function reads a text file and splits its contents into sentences. The file path is provided as an argument.

**preprocess_texts(texts, tokenizer, max_length)**: This function preprocesses the texts by converting them into sequences and padding them to a maximum length. It takes the input texts, tokenizer object, and the desired maximum length as arguments.

**create_model(vocab_size, max_input_length)**: This function creates the model architecture for log analysis. It utilizes an encoder-decoder LSTM architecture with embedding layers. The model is compiled with the Adam optimizer and categorical cross-entropy loss.

**create_inference_model(model)**: This function creates inference models for the encoder and decoder parts of the log analysis model. It extracts the necessary layers from the main model and constructs the inference models for prediction.

**decode_sequence(input_seq, encoder_model, decoder_model, tokenizer, max_length)**: This function decodes the sequence using the encoder and decoder models. It takes the input sequence, encoder model, decoder model, tokenizer, and maximum length as arguments.

These functions can be used to preprocess the log data, create the log analysis model, train the model, and perform inference on new log sequences.

### Usage
To use the log analysis project, follow these steps:

- Set up the necessary dependencies, including numpy, scikit-learn, Keras, and TensorFlow.
- Prepare the log files in the designated folder.
- Modify the regular expression patterns and the log folder path in the script for extracting message types.
- Run the script to extract the message types and generate separate input and output files.
- Modify the necessary parameters, such as vocabulary size and maximum input length, in the machine learning module.
- Preprocess the log texts using the provided functions from the machine learning module.
- Create the log analysis model using the create_model function.
- Train the model using the preprocessed log data.
- Use the create_inference_model function to create the inference models for encoding and decoding log sequences.
- Perform log analysis by using the decode_sequence function on new log sequences.
- Feel free to explore and adapt the code according to your specific log analysis requirements.
