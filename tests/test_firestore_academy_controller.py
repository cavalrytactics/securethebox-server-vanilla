from app_controllers.firestore_academy_controller import FirestoreAcademyController
from app_models.academy.Academy import Academy
import pytest
import os
import json

fac = FirestoreAcademyController()

pytest.globalData = []

def test_loadGlobalData():
    with open(str(os.getcwd())+"/tests/globalData.json", "r") as f:
        pytest.globalData = json.load(f)

def test_getCourses():
    status, courses = fac.getCourses()
    assert status == True

def test_addCourse():
    a = Academy()
    a.addCategory("web","WEB","#FFFFFF")
    a.addStep("step title","step context")
    a.setCourse("course title", "course description", "web", 120)
    status, course = a.getCourse()
    assert fac.addCourse(course) == True

def test_getCourse():
    academyId = "0-course-title"
    status, course = fac.getCourse("0-course-title")
    assert status == True

def test_updateCourse():
    academyId = "0-course-title"
    assert fac.updateCourse(academyId, {u"description":"updated"}) == True

def test_deleteCourse():
    assert fac.deleteCourse("0","course-title") == True

