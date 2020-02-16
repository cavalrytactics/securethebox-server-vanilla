import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from app_models.rest.category.Category import Category
import sys
import uuid
import os

# Use a service account
try:
    cred = credentials.Certificate(os.getcwd()+'/secrets/firebase-adminsdk.json')
except:
    currentDirectory = os.getcwd()
    with open(os.getcwd()+"/secrets/openssl","r") as f:
        envList = str(f.readline()).replace("$","").split(",")
        os.chdir(os.getcwd()+"/secrets")
        subprocess.Popen([f"openssl aes-256-cbc -K {os.environ[str(envList[0])]} -iv {os.environ[str(envList[1])]} -in secrets.tar.enc -out secrets.tar -d && tar xvf secrets.tar"],shell=True).wait()
        os.chdir(currentDirectory)
        cred = credentials.Certificate(os.getcwd()+'/secrets/firebase-adminsdk.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

class FirestoreRolesController():
    def __init__(self):
        self.category = Category()
    
    # def getRoles(self):
    #     try:
    #         docs = db.collection(u'category').stream()
    #         for doc in docs:
    #             self.category.addCourseDict(doc.to_dict())
    #         courses = self.academy.getCourses()
    #         return True, courses
    #     except:
    #         return False

    def addRole(self, role_payload):
        try:
            # ic_1_security_analyst
            db.collection(u'roles').document(str(role_payload["name"]).replace(" ","-")).set(role_payload)
            return True
        except:
            return False

    # def getCourse(self, academyId):
    #     try:
    #         course = db.collection(u'academy').document(academyId).get()
    #         return True, course.to_dict()
    #     except:
    #         return False

    # def updateCourse(self, academyId, course_payload):
    #     try:
    #         db.collection(u'academy').document(academyId).update(course_payload)
    #         return True
    #     except:
    #         return False

    # def deleteCourse(self, categoryId, courseSlug):
    #     try:
    #         db.collection(u'academy').document(str(categoryId)+"-"+str(courseSlug)).delete()
    #         return True
    #     except:
    #         return False