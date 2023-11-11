# Fetches model from hugging face and use it to summarising text

## How to run

```bash
poetry shell
poetry install
python ./summarize.py 
```

## Environment variables
- `HUGGING_FACE_API_KEY` - hugging face access token
- `HUGGING_FACE_REPO_ID` - repo id, e.g. `HUGGING_FACE_REPO_ID=csebuetnlp/mT5_multilingual_XLSum`


```latex
@inproceedings{hasan-etal-2021-xl,
    title = "{XL}-Sum: Large-Scale Multilingual Abstractive Summarization for 44 Languages",
    author = "Hasan, Tahmid  and
      Bhattacharjee, Abhik  and
      Islam, Md. Saiful  and
      Mubasshir, Kazi  and
      Li, Yuan-Fang  and
      Kang, Yong-Bin  and
      Rahman, M. Sohel  and
      Shahriyar, Rifat",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.413",
    pages = "4693--4703",
}
```
