# L-o-A-w-L (Level of Abstraction with LLM) 📚

## Overview
L-o-A-w-L (Level of Abstraction with LLM) is an innovative 🛠️ tool designed to dynamically adjust the level of abstraction in a document using language learning models (LLMs). Leveraging the power of LLMs, L-o-A-w-L allows users to interactively explore 🕵️‍♂️ documents at various levels of detail, simply by scrolling 🖱️ to increase or decrease the abstraction level. This project aims to enhance reading efficiency 🚀 and comprehension, making it easier to grasp complex documents or quickly get an overview of lengthy texts.

## How It Works

### Web Version

#### Step 1: Launch the Web Application 🚀
Start the L-o-A-w-L web application using Gunicorn for a robust and responsive user experience.


```bash
gunicorn app:app
```

#### Step 2: Upload Document 📤
Currently, users can input a document via a URL. Support for other formats like `.txt`, `.pdf`, and `.docx` is in the works. 🚧

#### Step 3: Set Initial Abstraction Level 🔍
The system automatically sets an initial depth level to maintain meaning upon compression. An additional expansion level is available to enrich the understanding of the document's general idea. This bidirectional approach is key for initial exploration.

#### Step 4: Interactive Abstraction Scaling 🎚️
Adjust the level of detail by scrolling over a paragraph. Enjoy a seamless experience as the initial summaries at various depths are pre-computed and require no further processing.

#### Step 5: Display of Tokens and Save Document 💾
Witness the efficiency of language models as L-o-A-w-L displays the tokens used for generating summaries. Save the state of your document at any time, capturing the desired level of abstraction for future reference.

### Behind the Scenes 🧠
L-o-A-w-L harnesses deep learning models for context-aware text analysis and summarization. When you adjust the level of abstraction, pre-computed summaries ensure instant response without the need for further server computation.

### Step 6: Export and Use 📋
Once you've fine-tuned the document to your liking, export the summary with the click of a button. Use the condensed material for presentations, quick reviews, or as a foundation for more in-depth study.


## Behind the Scenes
Underneath the user-friendly interface, L-o-A-w-L employs advanced deep learning models to analyze and summarize text WHILE MAINTAINING THE CONTEXT AWARENESS. When the user adjusts the abstraction level, a request is sent to the server where the LLM processes the current text in view. The LLM evaluates the context and content, generating a summary that corresponds to the requested level of detail.

The flexibility of the LLM allows L-o-A-w-L to produce summaries that are not only concise but also context-aware, ensuring that key information is highlighted or expanded upon as needed. This makes it an invaluable tool for researchers, students, or professionals who need to process large volumes of text efficiently.

## TODO 🚧

- **LangChain Independence**: Decouple L-o-A-w-L from specific language chain dependencies to enhance flexibility and compatibility with a broader range of NLP models.
- **Web UI Improvement**: Further develop the web interface to provide a more intuitive and seamless user experience, including more interactive elements and real-time feedback mechanisms.
- **Support for Various Formats**: Expand the range of document formats supported by L-o-A-w-L, including but not limited to `.docx`, `.pptx`, and more, to cater to a wider audience.
- **Integration of Local Models**: Implement the option for users to utilize local models for text abstraction, offering an alternative to cloud-based processing for enhanced privacy and speed.
- **JSON Parsing Capability**: Introduce JSON parsing features to allow users to work with structured data, enabling the abstraction of information from JSON files for summary or detailed exploration.
- **User Customization Options**: Provide users with the ability to customize abstraction levels, model choices, and other settings to personalize the tool according to their specific needs and preferences.

