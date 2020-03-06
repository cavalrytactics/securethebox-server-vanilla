yarn run relay --watch
gunicorn --bind 0.0.0.0:5000 main:app --reload
watch -n 5 pytest tests/app_schema/test_export_schema.py
watch -n 5 pytest -vs tests/app_schema/test_code_generator.py