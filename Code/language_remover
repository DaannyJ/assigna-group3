def language_remover()
    from langdetect import detect

    df = pd.read_csv("2022_downsampled_10000.csv", index_col=0)

    def detect_language(text):
        try:
            return detect(text)
        except:
            return None

    df['language'] = df['description.text'].apply(detect_language)

    swedish_df = df[df['language'] == 'sv']
