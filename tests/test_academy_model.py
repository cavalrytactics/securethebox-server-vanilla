from app_models.academy.Academy import Academy

a = Academy()

def test_addCategory():
    assert a.addCategory("web","WEB","#FFFFFF") == True

def test_addStep():
    assert a.addStep("step title","step context")

def test_getCategories():
    status, categories = a.getCategories()
    assert status == True

def test_getSteps():
    status, steps = a.getSteps()
    assert status == True

def test_sanatizeString():
    assert a.sanatizeString("oH)baby0-203") == "oh-baby0-203"

def test_getCategoryIdFromValue():
    status, categoryId = a.getCategoryIdFromValue("web")
    assert status == True
    assert categoryId == 0

def test_setCourse():
    assert a.setCourse("course title", "course description", "web", 120) == True

def test_addCourse():
    a.setCourse("course title", "course description", "web", 120)
    assert a.addCourse() == True

def test_getCourse():
    status, course = a.getCourse()
    assert status == True

def test_getCourses():
    status, courses = a.getCourses()
    assert status == True
