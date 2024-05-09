import os
os.environ["OPENAI_API_KEY"] = "sk-proj-dYsDrAgof5nimjwqYuoMT3BlbkFJRYL8kdtS3dTKil7spCJ2"

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI

# Define prompts for different content formats
linkedin_prompt = PromptTemplate(
    input_variables=["topic", "emotion", "length"],
    template="Generate a LinkedIn post on the topic of {topic}. The post should be engaging, informative, and include relevant hashtags. {emotion} {length}",
)

email_prompt = PromptTemplate(
    input_variables=["topic", "emotion", "length"],
    template="Write an email promoting a product or service related to {topic}. The email should be persuasive and highlight the key benefits. {emotion} {length}",
)

# Create a mapping of format to prompt
format_prompts = {
    "linkedin": linkedin_prompt,
    "email": email_prompt,
    # Add more formats and prompts as needed
}

# Define a function to generate marketing content
def generate_content(format, topic, emotion=None, length=None):
    if format not in format_prompts:
        return f"Error: '{format}' is not a supported format."

    prompt = format_prompts[format]

    # Add emotion and length instructions to the prompt if provided
    if emotion and length:
        prompt = prompt.format(topic=topic, emotion=emotion, length=length)
    elif emotion:
        prompt = prompt.format(topic=topic, emotion=emotion)
    elif length:
        prompt = prompt.format(topic=topic, length=length)
    else:
        prompt = prompt.format(topic=topic)

    # Create an LLM chain with the prompt
    llm = OpenAI(temperature=0.7)
    chain = LLMChain(llm=llm, prompt=prompt)

    # Generate marketing content
    result = chain.run()

    return result

# Example usage
format = "linkedin"
topic = "Generative AI"
emotion = "excited"
length = 100

content = generate_content(format, topic, emotion, length)
print(content)