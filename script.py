from translate import Translator

translator = Translator(to_lang="ko")

try:
    with open('./test-input.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        # Access the translated text using the 'text' attribute
        with open('./test-output.txt', mode='w', encoding='utf-8') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('check your file path silly!')
