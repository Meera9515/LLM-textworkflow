# -*- coding: utf-8 -*-
"""llm-project.ipynb

# 1) استيراد المكتبات
!pip install transformers torch pandas openpyxl --quiet

from transformers import pipeline
import pandas as pd
from google.colab import files

# 2) إعداد الـ Pipelines
generator = pipeline("text-generation", model="aubmindlab/aragpt2-medium")   # نموذج عربي
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")     # للتلخيص
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ar")    # للترجمة

# 3) تنفيذ المهام
prompt = "اكتب فقرة قصيرة عن المستقبل التقني والذكاء الاصطناعي:"
gen_text = generator(prompt, max_new_tokens=80, do_sample=True, temperature=0.8, top_p=0.95)[0]["generated_text"]

summary = summarizer(gen_text, max_length=60, min_length=20, do_sample=False)[0]["summary_text"]

translation = translator("Artificial Intelligence is shaping the future of humanity.", max_length=50)[0]["translation_text"]

# 4) حفظ النتائج في DataFrame
df = pd.DataFrame({
    "Task": ["Generation (Ar)", "Summarization", "Translation (En→Ar)"],
    "Result": [gen_text, summary, translation]
})

# 5) حفظ كملف Excel
df.to_excel("LLM_Project_Results.xlsx", index=False)

# 6) تنزيل الملف على جهازك
files.download("LLM_Project_Results.xlsx")



