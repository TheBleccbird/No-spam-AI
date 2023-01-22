
def clean_up_pipeline(dataset):
    cleaning_utils = [remove_hyperlink,
                      replace_newline,
                      remove_number,
                      remove_special_chars,
                      remove_white_spaces,
                      remove_long_words,
                      remove_nonascii_chars,
                      remove_exadecimals]
    for o in cleaning_utils:
        o(dataset)


def remove_hyperlink(dataset):
    dataset['subject'].replace({r"http\S+": None}, regex=True)
    dataset['email_from'].replace({r"http\S+": None}, regex=True)
    dataset['message'].replace({r"http\S+": None}, regex=True)


def replace_newline(dataset):
    dataset['subject'].replace({'\n': None}, regex=True)
    dataset['email_from'].replace({'\n': None}, regex=True)
    dataset['message'].replace({'\n': None}, regex=True)


def remove_number(dataset):
    dataset['subject'].replace({r'^[0-9]+$': None}, regex=True)
    dataset['email_from'].replace({r'^[0-9]+$': None}, regex=True)
    dataset['message'].replace({r'^[0-9]+$': None}, regex=True)


def remove_special_chars(dataset):
    spec_chars = ["!", '"', "#", "%", "&", "'", "(", ")",
                  "*", "+", ",", "-", ".", "/", ":", ";", "<",
                  "=", ">", "?", "@", "[", "\\", "]", "^", "_",
                  "`", "{", "|", "}", "~", "–"]
    for char in spec_chars:
        dataset['subject'] = dataset['subject'].str.replace(char, ' ', regex=True)
        dataset['email_from'] = dataset['email_from'].str.replace(char, ' ', regex=True)
        dataset['message'] = dataset['message'].str.replace(char, ' ', regex=True)


def remove_white_spaces(dataset):
    dataset['subject'] = dataset['subject'].str.split().str.join(" ")
    dataset['email_from'] = dataset['email_from'].str.split().str.join(" ")
    dataset['message'] = dataset['message'].str.split().str.join(" ")


def remove_long_words(dataset):
    dataset['subject'].replace({r'.{20,}': None}, regex=True)
    dataset['email_from'].replace({r'.{20,}': None}, regex=True)
    dataset['message'].replace({r'.{20,}': None}, regex=True)


def remove_nonascii_chars(dataset):
    dataset['subject'].replace({r'[^\x00-\x7F]+': None}, regex=True, inplace=True)
    dataset['email_from'].replace({r'[^\x00-\x7F]+': None}, regex=True, inplace=True)
    dataset['message'].replace({r'[^\x00-\x7F]+': None}, regex=True, inplace=True)


def remove_exadecimals(dataset):
    dataset['subject'].replace({r'0[xX][0-9a-fA-F]+': None}, regex=True, inplace=True)
    dataset['email_from'].replace({r'0[xX][0-9a-fA-F]+': None}, regex=True, inplace=True)
    dataset['message'].replace({r'0[xX][0-9a-fA-F]+': None}, regex=True, inplace=True)
