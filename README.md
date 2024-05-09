API Doc for problem1

**Documentation for Webpage Question Answering API**

**Overview**

This API takes a webpage URL and a question as input, and responds with the answer to the question based on the content of the webpage. If the answer is not found in the webpage, it responds with "I don't know the answer".

**Dependencies**

- Flask: A lightweight Python web framework for building APIs.
- requests: A Python library for making HTTP requests to fetch the webpage content.
- BeautifulSoup: A Python library for parsing HTML and XML documents.
- nltk: The Natural Language Toolkit library for natural language processing tasks.

**Installation**

1. Install Python 3.x (if not already installed)
2. Install the required packages:

```
pip install Flask requests beautifulsoup4 nltk
```

3. Download the NLTK data by running the following command in your Python interpreter:

```python
import nltk
nltk.download('punkt')
```

**API Usage**

The API endpoint is `/get_answer`, and it accepts POST requests with the following JSON payload:

```json
{
    "url": "https://en.wikipedia.org/wiki/Generative_artificial_intelligence",
    "question": "What are the concerns around Generative AI?"
}
```

**Input**

- `url` (string): The URL of the webpage to be queried.
- `question` (string): The question for which the answer needs to be found in the webpage content.

**Output**

The API returns a JSON response with the following structure:

```json
{
    "answer": "There's been apprehension regarding the possible misapplication of generative AI, including its involvement in cybercrime, dissemination of fake news or deepfakes to deceive or manipulate individuals, and the widespread displacement of human employment."
}
```

If the answer is not found in the webpage, the API responds with:

```json
{
    "answer": "I don't know the answer"
}
```

**Authentication**

This API does not require any authentication.

**Input Processing**

1. The API fetches the webpage content using the `requests` library and the provided URL.
2. The HTML content of the webpage is parsed using BeautifulSoup to extract the text.
3. The extracted text is tokenized into sentences using the `sent_tokenize` function from the NLTK library.

**Response Generation**

1. The API iterates over the sentences extracted from the webpage.
2. If the question is found in a sentence, that sentence is considered the answer and returned in the JSON response.
3. If the question is not found in any of the sentences, the API responds with "I don't know the answer".

**Deployment Instructions**

1. Save the provided code in a Python file (e.g., `app.py`).
2. Run the Flask app:

```
python app.py
```

The API will be running on `http://localhost:5000/` by default.

3. To test the API, send a POST request to `http://localhost:5000/get_answer` with the appropriate JSON payload.

You can use tools like Postman or cURL to send the request:

```
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://en.wikipedia.org/wiki/Generative_artificial_intelligence", "question": "What are the concerns around Generative AI?"}' http://localhost:5000/get_answer
```





API doc for problem2

**Documentation for Generate Marketing Content API**

**Overview**

This API generates marketing content for various formats such as LinkedIn posts, emails, and more, based on a given topic and additional parameters like emotion and length. It uses OpenAI's language model to generate the content.

**Dependencies**

- `langchain`: A Python library for building applications with large language models.
- `langchain_openai`: A package that provides integration between LangChain and OpenAI language models.

**Installation**

1. Install Python 3.x (if not already installed).
2. Install the required packages:

```
pip install langchain langchain_openai
```

**API Usage**

The API is implemented as a Python function `generate_content` that takes the following parameters:

- `format` (string): The desired format for the marketing content (e.g., "linkedin", "email").
- `topic` (string): The topic for which the marketing content should be generated.
- `emotion` (string, optional): The desired emotion or tone for the content.
- `length` (int, optional): The approximate length of the content in words.

**Input**

The input parameters can be provided directly to the `generate_content` function. For example:

```python
content = generate_content(format="linkedin", topic="Generative AI", emotion="excited", length=100)
```

**Output**

The function returns the generated marketing content as a string. For example:

```
"Excited to share insights on Generative AI! 🚀 With its innovative capabilities, Generative AI is revolutionising various industries, from creative arts to healthcare. Its potential to generate realistic images, text, and even music is reshaping the way we create and interact with technology. Let's explore the endless possibilities and opportunities this cutting-edge technology offers. #GenerativeAI #Innovation #TechRevolution 🤖💡"
```

**Authentication**

The API requires an OpenAI API key to be set as an environment variable `OPENAI_API_KEY`. In the provided code, the API key is set directly in the code:

```python
import os
os.environ["OPENAI_API_KEY"] = "sk-proj-dYsDrAgof5nimjwqYuoMT3BlbkFJRYL8kdtS3dTKil7spCJ2"
```

**Note**: It is recommended to set the API key as an environment variable instead of hardcoding it in the code for security reasons.

**Input Processing**

1. The API checks if the provided `format` is supported. If not, it returns an error message.
2. It retrieves the corresponding prompt template for the given `format` from the `format_prompts` dictionary.
3. If `emotion` and `length` parameters are provided, they are added to the prompt template using the `format` method of the `PromptTemplate` class.

**Response Generation**

1. An instance of the `OpenAI` language model is created with a temperature of 0.7 (adjust as needed).
2. An `LLMChain` is created using the language model instance and the processed prompt.
3. The `run` method of the `LLMChain` is called, which generates the marketing content based on the prompt and returns it.

**Usage Example**

```python
format = "linkedin"
topic = "Generative AI"
emotion = "excited"
length = 100

content = generate_content(format, topic, emotion, length)
print(content)
```

**Adding More Formats**

To add support for more content formats, you can extend the `format_prompts` dictionary with new `PromptTemplate` instances for the desired formats.

**Deployment Instructions**

This code can be deployed as a standalone Python script or integrated into a larger application or API. To run the code, simply execute the Python file after installing the required dependencies.

**Note**

This implementation uses the `langchain` and `langchain_openai` libraries, which provide a high-level interface for working with large language models like OpenAI's GPT-3. The quality and suitability of the generated content may vary depending on the topic, prompt templates, and language model used.
