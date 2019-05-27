import pandas as pd
from numpy import dot
from numpy.linalg import norm


def _cos_sim(a, b):
    return [dot(a, b)/(norm(a)*norm(b))]


def get_df(articles, transformation_options={
    'bert_title': 'REDUCE_MAX',
    'bert_text': 'CLS_TOKEN'
}):
    results = []

    bert_title = transformation_options['bert_title']
    bert_text = transformation_options['bert_text']

    for article in articles:
        bg_bert_title = article['features']['bg']['BERT']['title'][bert_title]
        bg_bert_text = article['features']['bg']['BERT']['text'][bert_text]
        bg_bert_cos = _cos_sim(bg_bert_title, bg_bert_text)

        bg_xlm_title = article['features']['bg']['XLM']['title']
        bg_xlm_text = article['features']['bg']['XLM']['text']
        bg_xlm_cos = _cos_sim(bg_xlm_title, bg_xlm_text)

        en_use_title = article['features']['en']['USE']['title']
        en_use_text = article['features']['en']['USE']['text']
        en_use_cos = _cos_sim(en_use_title, en_use_text)

        en_bert_title = article['features']['en']['BERT']['title'][bert_title]
        en_bert_text = article['features']['en']['BERT']['text'][bert_text]
        en_bert_cos = _cos_sim(en_bert_title, en_bert_text)

        en_nela_title = article['features']['en']['NELA']['title']
        en_nela_text = article['features']['en']['NELA']['text']
        en_nela_cos = _cos_sim(en_nela_title, en_nela_text)

        en_elmo_title = article['features']['en']['ELMO']['title']
        en_elmo_text = article['features']['en']['ELMO']['text']
        en_elmo_cos = _cos_sim(en_elmo_title, en_elmo_text)
    
        results.append([
            article['title'],
            article['text'],
            {
                'title': article['title'],
                'text': article['text']
            },
            bg_bert_title,
            bg_bert_text,
            bg_bert_cos,
            bg_xlm_title,
            bg_xlm_text,
            bg_xlm_cos,
            en_use_title,
            en_use_text,
            en_use_cos,
            en_nela_title,
            en_nela_text,
            en_nela_cos,
            en_elmo_title,
            en_elmo_text,
            en_elmo_cos,
            en_bert_title,
            en_bert_text,
            en_bert_cos,
            article['media_info'],
            article['label']
        ])

    return pd.DataFrame(results, columns=[
        'title',
        'text',
        'article',
        'bg_bert_title',
        'bg_bert_text',
        'bg_bert_cos',
        'bg_xlm_title',
        'bg_xlm_text',
        'bg_xlm_cos',
        'en_use_title',
        'en_use_text',
        'en_use_cos',
        'en_nela_title',
        'en_nela_text',
        'en_nela_cos',
        'en_elmo_title',
        'en_elmo_text',
        'en_elmo_cos',
        'en_bert_title',
        'en_bert_text',
        'en_bert_cos',
        'media',
        'label'
    ])


def oversample(df, n=None, frac=None):
    labels = df['label'].unique()

    oversampled = None

    for label in labels:
        if frac:
            samples = df[df['label'] == label].sample(frac=frac,
                                                      random_state=0,
                                                      replace=True)
        elif n:
            samples = df[df['label'] == label].sample(n=n,
                                                      random_state=0,
                                                      replace=True)
        else:
            raise 'n/frac is required.'

        if oversampled is None:
            oversampled = samples
        else:
            oversampled = oversampled.append(samples)

    return oversampled.sample(frac=1).reset_index(drop=True)
