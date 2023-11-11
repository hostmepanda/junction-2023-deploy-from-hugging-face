import os
import re
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

load_dotenv()

HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")
model_name = os.getenv("HUGGING_FACE_REPO_ID")
model_saved = './models/{model_name}'.format(model_name=model_name)

WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

tokenizer = AutoTokenizer.from_pretrained(model_name, legacy=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

model.save_pretrained(f'./models/{model_name}')
tokenizer.save_pretrained(f'./models/{model_name}')

article_text = """The long abstract should be written according to underlying structure of the structured abstract and in a
form that is shorter than the full text. The long abstract of the full paper shall be written with Times New
Roman font, double line spacing and 12 font size. Long abstracts can contain figures, tables, formulations
or images. Long abstracts should be in a structure that explains the content of the declaration therefore the
preparation phase of the said work. Page margins are formed regarding the A4 page size and are 2.5 cm
wide from the right, left, top and bottom. End of the lines should be aligned to the right and there should
be no syllable segmentation"""

input_ids = tokenizer(
    [WHITESPACE_HANDLER(article_text)],
    return_tensors="pt",
    padding="max_length",
    truncation=True,
    max_length=1024
)["input_ids"]

output_ids = model.generate(
    input_ids=input_ids,
    max_length=100,
    no_repeat_ngram_size=2,
    num_beams=4
)[0]

summary = tokenizer.decode(
    output_ids,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)

print(summary)

