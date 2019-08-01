# Detecting toxicity in news articles - a study for news in Bulgarian language

## Motivation
Current repository is used as an experiment evaluation system. Generated results are being used in a research inspired by [RANLP'19](http://lml.bas.bg/ranlp2019/start.php) conference. 

## Dataset

Contains 221 articles, manually labelled by [Krasimir Gadjokov](https://www.gadjokov.com/) between 2011-2017. As well as 96 non-toxic articles fetched from credible bulgarian news outlets in 2019. To incorporate even more features we use Google API for articles translation. Each article is available in both english and bulgarian.

Toxicity categories are as follows (examples are in Bulgarian)):

| Category | Example |
|----------|---------|
| fake news (фалшиви новини) | [click here](http://bradva.bg/bg/article/article-108980#.WOEh6FPyt3k) |
| defamation (клевета) | [click here](http://pik.bg/%D0%B1%D0%BE%D0%BC%D0%B1%D0%B0-%D0%B2-%D0%BF%D0%B8%D0%BA-%D1%80%D0%B0%D0%B4%D0%B0%D0%BD-%D0%B8-%D0%BF%D1%80%D0%BE%D1%82%D0%B5%D1%81%D1%82%D0%BD%D0%B0-%D0%BC%D1%80%D0%B5%D0%B6%D0%B0-%D0%BD%D0%B0-%D1%82%D0%B0%D0%B9%D0%BD%D0%B0-%D1%81%D1%80%D0%B5%D1%89%D0%B0-%D0%BF%D0%BB%D0%B0%D0%BD%D0%B8%D1%80%D0%B0%D1%82-%D1%81%D0%B2%D0%B0%D0%BB%D1%8F%D0%BD%D0%B5%D1%82%D0%BE-%D0%BD%D0%B0-%D1%86%D0%B0%D1%86%D0%B0%D1%80%D0%BE%D0%B2-%D0%B4%D0%B0%D0%B2%D0%B0%D1%82-%D0%BF%D0%BE--news363313.html) |
| sensation (сензация) | [click here](https://fakti.bg/life/234099-3-znaka-che-ste-bogina-v-seksa) |
| hate speech (реч на омраза) | [click here](https://trud.bg/%D1%8F%D0%BA-%D1%80%D0%B8%D1%82%D0%BD%D0%B8%D0%BA-%D0%B7%D0%B0%D0%B1%D0%B8-%D0%BA%D0%B0%D0%B1%D0%B8%D0%BD%D0%B5%D1%82%D1%8A%D1%82-%D0%B2-%D0%B7%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%82%D0%B5-%D0%B7%D0%B0/) |
| delusion (заблуда) | [click here](http://www.zajenata.bg/%D0%BA%D0%B0%D0%BF%D0%B2%D0%B0%D0%B9%D1%82%D0%B5-%D0%BE%D1%82-%D1%82%D0%BE%D0%B7%D0%B8-%D0%BB%D0%B5%D0%BA-%D0%B2-%D1%83%D1%88%D0%B8%D1%82%D0%B5-%D1%81%D0%B8-%D0%B8-%D1%81%D0%BB%D1%83%D1%85%D1%8A%D1%82-%D0%B2%D0%B8-%D1%89%D0%B5-%D1%81%D0%B5-%D0%B2%D1%8A%D0%B7%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8-%D0%BD%D0%B0-97!-%D1%82%D0%BE%D0%B7%D0%B8-%D0%BB%D0%B5%D1%81%D0%B5%D0%BD-%D0%BD%D0%B0%D1%82%D1%83%D1%80%D0%B0%D0%BB%D0%B5%D0%BD-%D0%BB%D0%B5%D0%BA-%D0%B5-%D0%B5%D1%84%D0%B8%D0%BA%D0%B0%D1%81%D0%B5%D0%BD-%D0%B4%D0%BE%D1%80%D0%B8-%D0%B7%D0%B0-%D0%B2%D1%8A%D0%B7%D1%80%D0%B0%D1%81%D1%82%D0%BD%D0%B8-%D1%85%D0%BE%D1%80%D0%B0-news81287.html) |
| conspiracy (конспирация) | [click here](https://trud.bg/article-4882794/) |
| anti-democratic (анти-демократичен) | [click here](http://budnaera.com/201701f/17010944.html) |
| pro-authoritarian (про-авториратерен) | [click here](http://duma.bg/node/37323) |
| non-toxic (нетоксичен) | [click here](https://www.actualno.com/bgfootball/nov-stadion-za-cska-no-ima-seriozni-problemi-za-reshavane-news_737893.html)

Labels' source of truth: https://mediascan.gadjokov.com/

<img src="https://user-images.githubusercontent.com/493912/62256881-6726ac00-b403-11e9-9060-89f0eebce71f.png" width="400px" />

Dataset can be downloaded from [here]().

Detailed information about dataset, can be found in [docs](/docs/data).

## Features

We have generated feature sets for both English and Bulgarian

| Type | Embeddings size |
|--------|-------|
| LSA (title) | 15 |
| LSA (text)  | 200 |
| BERT (title) | 768 | 
| BERT (text) | 768 |
| META (article) | 15 |
| META (media) | 6 |


## Experiment results

| Type | Overall accuracy |
|--------|-------|
| Baseline | 30.29% |
| Linear Regression  | 54.33% |
| Linear Regression (tuned) | 55.65% | 
| Linear Regression (improved) + Oversammpled dataset | 56.21% |
| Neural network | 51.10% |


## References
