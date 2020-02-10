pytest tests/test_travis_controller.py
pytest tests/test_cloudrun_controller.py
pytest tests/test_kubernetes_controller.py

if [ $? -eq 0 ]; then
    git add .
    cz commit
    git push
else
    echo FAIL
fi

