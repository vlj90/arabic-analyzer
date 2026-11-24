import csv
import io
import tempfile
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, File, HTTPException, UploadFile

from main import analyze_csv, get_top_words  # نستورد الدوال اللي نحتاجها فقط

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Arabic Text Analyzer API"}


@app.post("/analyze")
async def analyze(file: Annotated[UploadFile, File()]):

    # التحقق من امتداد الملف
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")
    content = await file.read()  # قراءة محتوى الملف المرفوع

    # التحقق من أن الملف غير فارغ
    if not content.strip():
        raise HTTPException(status_code=400, detail="The uploaded file is empty")

        # التحقق من وجود عمود text
    text = content.decode("utf-8")
    reader = csv.DictReader(io.StringIO(text))

    if not reader.fieldnames or "text" not in reader.fieldnames:
        raise HTTPException(
            status_code=400, detail="CSV file must contain a 'text' column"
        )
    # انشاء مجلد مؤقت لحفظ الملف
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "uploaded.csv"

        file_path.write_bytes(content)  # حفظ محتوى الملف بشكل مؤقت

        # استدعاء دالة تحليل الملف
        total_words, word_counts = analyze_csv(file_path)

        # استخراج أكثر 20 كلمة تكرارا
        top_20_words = get_top_words(word_counts)

        # تجهيز التقرير النهائي
        report = {
            "total_words": total_words,
            "top_20_words": top_20_words,
        }

    return report  # ارجاع التقرير للمستخدم بصيغة JSON
