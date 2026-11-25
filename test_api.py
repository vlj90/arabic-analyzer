from fastapi.testclient import TestClient  # استيراد أداة اختبار الـ API
from api import app  # استيراد تطبيق FastAPI

client = TestClient(app)  # إنشاء عميل لإرسال الطلبات بشكل تلقائي


# الاختبار الأول: التحقق من عمل الصفحة الرئيسية
def test_home_endpoint():

    # إرسال طلب GET
    response = client.get("/")

    # التحقق من نجاح الطلب
    assert response.status_code == 200

    # التحقق من صحة الرسالة
    assert response.json() == {"message": "Arabic Text Analyzer API"}


# الاختبار الثاني: التحقق من رفع ملف CSV صحيح وتحليله
def test_valid_csv():

    # إنشاء محتوى ملف CSV تجريبي
    csv_content = "text\nمرحبا بالعالم\nمرحبا بالجميع"

    # إرسال الملف إلى نقطة الاتصال الخاصة بالتحليل
    response = client.post(
        "/analyze",
        files={"file": ("test.csv", csv_content.encode("utf-8"), "text/csv")},
    )

    # التحقق من نجاح رفع الملف
    assert response.status_code == 200

    # التحقق من إجمالي عدد الكلمات
    assert response.json()["total_words"] == 4

    # التحقق من أكثر كلمة تكرارا
    assert response.json()["top_20_words"][0] == ["مرحبا", 2]


# الاختبار الثالث: التحقق من رفض الملفات ذات الامتداد الخاطئ
def test_invalid_file_extension():

    # إرسال ملف تجريبي بامتداد PDF بدلا من CSV
    response = client.post(
        "/analyze",
        files={"file": ("test.pdf", b"test content", "application/pdf")},
    )

    # التحقق من رفض الطلب
    assert response.status_code == 400

    # التحقق من صحة رسالة الخطأ
    assert response.json()["detail"] == "Only CSV files are allowed"


# الاختبار الرابع: التحقق من رفض الملفات الفارغة
def test_empty_file():

    # إرسال ملف CSV بدون أي محتوى
    response = client.post(
        "/analyze",
        files={"file": ("empty.csv", b"", "text/csv")},
    )

    # التحقق من رفض الطلب
    assert response.status_code == 400

    # التحقق من صحة رسالة الخطأ
    assert response.json()["detail"] == "The uploaded file is empty"


# الاختبار الخامس: التحقق من رفض الملفات التي لا تحتوي على عمود text
def test_missing_text_column():

    # إنشاء محتوى CSV بدون عمود text
    csv_content = "name,age\nAhmed,25\nSara,30"

    # إرسال الملف إلى نقطة الاتصال الخاصة بالتحليل
    response = client.post(
        "/analyze",
        files={"file": ("invalid.csv", csv_content.encode("utf-8"), "text/csv")},
    )

    # التحقق من رفض الطلب
    assert response.status_code == 400

    # التحقق من صحة رسالة الخطأ
    assert response.json()["detail"] == "CSV file must contain a 'text' column"


# الاختبار السادس: التحقق من دقة تنظيف النصوص وحساب الكلمات
def test_word_count_accuracy():

    # إنشاء نص يحتوي على تشكيل وعلامات ترقيم وإيموجي
    csv_content = "text\nأَحمد! أحمد، احمد 😊\nإبداع إبداع."

    # إرسال الملف إلى نقطة الاتصال الخاصة بالتحليل
    response = client.post(
        "/analyze",
        files={"file": ("accuracy.csv", csv_content.encode("utf-8"), "text/csv")},
    )

    # التحقق من نجاح الطلب
    assert response.status_code == 200

    # التحقق من إجمالي عدد الكلمات بعد التنظيف
    assert response.json()["total_words"] == 5

    # التحقق من صحة الكلمات وتكرارها وترتيبها
    assert response.json()["top_20_words"] == [
        ["احمد", 3],
        ["ابداع", 2],
    ]
