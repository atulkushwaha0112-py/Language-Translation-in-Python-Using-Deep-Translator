from deep_translator import GoogleTranslator
# By Atul Kushwaha

# Translate "Hello" into Hindi

Sentence="Hello"
Source_language="en" # english
Translated_language="hi" # hindi

result = GoogleTranslator(source=Source_language, target=Translated_language).translate(Sentence)
print("Translation in Hindi:", result)


# Translation in Hindi: नमस्ते




