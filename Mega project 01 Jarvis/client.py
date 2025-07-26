from openai import OpenAI

# client = OpenAI()
# Defaults to getting the key using os.environ.get("OPENAI_API_KEY")

# If you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
   api_key="api key address ",
)


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis , skilled  in general task like Alexa and Google cloudw."},
        {"role": "user", "content": "what is coding."}
    ]
)

print(completion.choices[0].message) # maiy is ki jagha koi our update code kea hai just is mian change kea hi
# mews.txt main para hai
