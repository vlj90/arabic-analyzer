import csv  # عشان تقرا الملف
import json  # عشان نحفظ التقرير النهائي

import emoji  # عشان  نحذف الاموجيات


def clean_text(text):  # دالة التنظيف
    text = emoji.replace_emoji(text, replace="")  # نبدل الاموجيات
    text = text.strip()

    punctuation = ["!", "؟", "?", ".", "،", "؛"]

    for mark in punctuation:
        text = text.replace(mark, "")

    tashkeel = ["َ", "ُ", "ِ", "ْ", "ّ", "ً", "ٌ", "ٍ"]

    for mark in tashkeel:
        text = text.replace(mark, "")

    # توحيد اشكال الالف
    alef = ["أ", "إ", "آ"]

    for letter in alef:
        text = text.replace(letter, "ا")
        text = text.replace("ـ", "")  # حق مد الكلمة

    text = " ".join(
        text.split()
    )  # تقسيم النص لكلمات وتحذف المسافات ونرجع نجمعها وحط بينهم مسافه وحدة

    return text


def analyze_csv(file_path):  # دالة لقراءة الملف وحساب الكلمات
    total_words = 0  # اجمالي عدد الكلمات
    word_counts = {}  # قاموس نخزن فيه كل كلمة عشان نعرف التكرار

    with open(file_path, "r", encoding="utf-8") as file:  # قراية الملف
        reader = csv.DictReader(file)

        for row in reader:
            result = clean_text(row["text"])
            words = result.split()  # تقسيم النص لكلمات

            total_words += len(words)  #  حساب عدد االكلمات

            for word in words:  # حساب التكرار
                if word in word_counts:
                    word_counts[word] += 1  # اذا موجودة زيد واحد
                else:
                    word_counts[word] = 1  # اذا موب موجودة فضيفها بقيمة واحد

    return total_words, word_counts


def get_top_words(word_counts):  # دالة تستقبل قاموس الكلمات وتكراراتها
    sorted_words = sorted(
        word_counts.items(), key=lambda item: item[1], reverse=True
    )  # ترتيب الكلمات من الأكثر تكرارًا إلى الأقل

    top_20_words = sorted_words[:20]  # اختيار أكثر 20 كلمة تكرارًا
    return top_20_words


def save_report(report, output_path):  # دالة حفظ التقرير
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=4)


# استدعاء كل الدوال

try:  # Error Handling اذا الملف مكنش موجود
    total_words, word_counts = analyze_csv("ar_text_data.csv")

except FileNotFoundError:
    print("الملف غير موجود")
    raise SystemExit(1)


top_20_words = get_top_words(word_counts)  # استخراج أكثر 20 كلمة
print("Top 20 words:", top_20_words)  # اعرضها

report = {
    "total_words": total_words,
    "top_20_words": top_20_words,
}
save_report(report, "report.json")  # حفظ التقرير في JSON
