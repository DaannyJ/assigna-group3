def language_remover(df):
    from langdetect import detect

    def detect_language(text):
        try:
            return detect(text)
        except:
            return None

    df['language'] = df['description.text'].apply(detect_language)

    swedish_df = df[df['language'] == 'sv']
    swedish_df.drop('language', axis=1, inplace=True)
    return swedish_df