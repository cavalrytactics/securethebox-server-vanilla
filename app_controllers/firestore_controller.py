import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from app_models.academy.Academy import Academy
import sys
import uuid

# Use a service account
cred = credentials.Certificate('./secrets/firebase-adminsdk.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

class Firestore():
    def __init__(self):
        self.academy = Academy()
    
    def getCourses(self):
        docs = db.collection(u'academy').stream()
        for doc in docs:
            self.academy.addCourseDict(doc.to_dict())
        return self.academy.getCourses()

    def addCourse(self, course_payload):
        for x in course_payload["steps"]:
            self.academy.addStep(x["title"],x["content"])
        self.academy.addCourse(
            course_payload["title"],
            course_payload["title"],
            course_payload["description"],
            course_payload["category"],
            course_payload["length"],
        )

        db.collection(u'academy').add(self.academy.course.to_dict())