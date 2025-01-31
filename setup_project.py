import os

# تعریف ساختار پوشه‌ها و فایل‌ها
project_structure = {
    "tax_assistant": [
        "backend",
        "backend/database",
        "backend/models",
        "backend/chatbot",
        "frontend",
        "frontend/static",
        "frontend/templates",
    ]
}

files = {
    "backend/database": [
        "connection.py",
        "mongo_connection.py",
        "init_postgres.sql",
        "store_data.py",
        "pdf_processor.py",
        "image_processor.py",
    ],
    "backend/models": ["bert_model.py", "gpt3_model.py"],
    "backend/chatbot": ["chatbot.py"],
    "frontend/static": ["styles.css", "script.js"],
    "frontend/templates": ["index.html"],
    "frontend": ["app.py"],
    "tax_assistant": ["requirements.txt", "README.md"],
}

# ایجاد پوشه‌ها
for base_folder, subfolders in project_structure.items():
    for folder in subfolders:
        os.makedirs(folder, exist_ok=True)

# ایجاد فایل‌ها
for folder, filenames in files.items():
    for filename in filenames:
        file_path = os.path.join(folder, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("")  # فایل‌ها را خالی ایجاد می‌کند

print("✅ ساختار پروژه با موفقیت ایجاد شد!")
