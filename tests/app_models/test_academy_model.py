from app_models.rest.academy.Academy import Academy

m = Academy()

def test_addCategory():
    assert m.addCategory("web","WEB","#FFFFFF") == True

def test_addStep():
    assert m.addStep("step title","step context")

def test_getCategories():
    status, categories = m.getCategories()
    assert status == True

def test_getSteps():
    status, steps = m.getSteps()
    assert status == True

def test_sanatizeString():
    assert m.sanatizeString("oH)baby0-203") == "oh-baby0-203"

def test_getCategoryIdFromValue():
    status, categoryId = m.getCategoryIdFromValue("web")
    assert status == True
    assert categoryId == 0

def test_setCourse():
    assert m.setCourse("course title", "course description", "web", 120) == True

def test_addCourse():
    m.setCourse("course title", "course description", "web", 120)
    assert m.addCourse() == True

def test_getCourse():
    status, course = m.getCourse()
    assert status == True

def test_getCourses():
    status, courses = m.getCourses()
    assert status == True
