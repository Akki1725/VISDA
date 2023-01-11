# The main brainframe of VISDA
# Importing modules
import openai


# Extracting API keys
with open("Data\\API.txt") as f:
    API = f.read()

# Extracting API keys
with open("Data\\API_Codex.txt") as f:
    API_codex = f.read()


# Text completion response
def response(query, chat_log=None):

    openai.api_key = API
    completion = openai.Completion()

    with open("E:\Docs\Projects\Projects\VISDA\DataBase\chat_log.txt") as log:
        chat_log_temp = log.read()

    if chat_log is None:
        chat_log = chat_log_temp

    prompt = f"{chat_log}You: {query}\nVISDA:"
    response = completion.create(
        model ="text-davinci-003",
        prompt = prompt,
        temperature = 0.9,
        max_tokens = 150,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0.6
    )
    answer = response.choices[0].text.strip()
    chat_log_temp_update = chat_log_temp + f"\nYou: {query}\nVISDA: {answer}"

    with open("E:\Docs\Projects\Projects\VISDA\DataBase\chat_log.txt", "w") as log:
        log.write(chat_log_temp_update)

    answer = str(answer)
    return answer


# Image completion response
def create(description):

    openai.api_key = API
    
    prompt = str(description)
    image_response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
    image = image_response["data"][0]["url"]
    image = str(image)
    return image

# Write code
def write(prompt):
    openai.api_key = API_codex
    completion = openai.Completion()

    if "python" in prompt or "sql" in prompt:
        prompt = f"'''\n{prompt}\n'''"
    
    elif "java" in prompt and "script" in prompt:
        prompt = f"/*\n{prompt}\n*/"
    
    elif "java" in prompt:
        prompt = f"// {prompt}\n"
    
    elif "html" in prompt:
        prompt = f"<!-- {prompt} -->\n<!DOCTYPE html>"

    else:
        prompt = f"# {prompt}\n"

    response = completion.create(
        model = "code-davinci-002",
        prompt = prompt,
        temperature = 0,
        max_tokens = 256,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )

    answer = response["choices"][0]["text"]
    if "html" in prompt:
        answer = f"\n<!DOCTYPE html>\n{answer}"
    else:
        answer = f"\n{answer}"
    answer = str(answer)
    return answer


# Code explanation with code input
def explain(prompt, code):
    openai.api_key = API_codex
    completion = openai.Completion()
    code = code    
    prompt = f"'''\n{prompt}:\n{code}\n'''\nHere is what the above code is doing:\n"
    response = completion.create(
        model = "code-davinci-002",
        prompt = prompt,
        temperature = 0,
        max_tokens = 64,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0,
        stop = ["'''"]
    )

    answer = response["choices"][0]["text"]
    answer = f"\n{answer}"
    answer = str(answer)
    return answer
