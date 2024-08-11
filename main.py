import TextAnalysis
from TextAnalysis import TextAnalysis
import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('Input.xlsx')
    urls = df.to_numpy()
    output = {
        'URL_ID': [],
        'URL': [],
        'POSITIVE SCORE': [],
        'NEGATIVE SCORE': [],
        'POLARITY SCORE': [],
        'SUBJECTIVITY SCORE': [],
        'AVG SENTENCE LENGTH': [],
        'PERCENTAGE OF COMPLEX WORDS': [],
        'FOG INDEX': [],
        'AVG NUMBER OF WORDS PER SENTENCE': [],
        'COMPLEX WORD COUNT': [],
        'WORD COUNT': [],
        'SYLLABLE PER WORD': [],
        'PERSONAL PRONOUNS': [],
        'AVG WORD LENGTH': []
    }
    for i in urls:
        url_id = i[0]
        output.get('URL_ID').append(url_id)
        url = i[1]
        output.get('URL').append(url)
        t = TextAnalysis(url, url_id)
        output.get('POSITIVE SCORE').append(t.PositiveScore)
        output.get('NEGATIVE SCORE').append(t.NegativeScore)
        output.get('POLARITY SCORE').append(t.PolarityScore)
        output.get('SUBJECTIVITY SCORE').append(t.SubjectivityScore)
        output.get('AVG SENTENCE LENGTH').append(t.AvgSentLen)
        output.get('PERCENTAGE OF COMPLEX WORDS').append(t.CmpxWordsPercentage)
        output.get('FOG INDEX').append(t.FogIndex)
        output.get('AVG NUMBER OF WORDS PER SENTENCE').append(t.AvgWordsPerSent)
        output.get('COMPLEX WORD COUNT').append(t.CmpxWordsCount)
        output.get('WORD COUNT').append(t.WordCount)
        output.get('SYLLABLE PER WORD').append(t.SyllablePerWord)
        output.get('PERSONAL PRONOUNS').append(t.PersonalPronoun)
        output.get('AVG WORD LENGTH').append(t.AvgWordLen)

        file_name = 'Output.xlsx'
        odf = pd.DataFrame.from_dict(output)
        odf.to_excel(file_name)


