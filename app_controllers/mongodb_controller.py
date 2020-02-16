import pymongo
import os

class MongodbController():
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.database = self.client["TEST"]
        self.collection = self.database["TEST"]

    def setEnvironmentVariable(self, environmentVariable):
        try:
            if os.getenv(environmentVariable) is not None:
                setattr(self, environmentVariable,
                        os.getenv(environmentVariable))
            else:
                print(f"{environmentVariable} is not set")
                return False
            return True
        except:
            return False

    def setClient(self):
        try:
            self.client = pymongo.MongoClient(f"mongodb+srv://{self.MONGODB_USER}:{self.MONGODB_PASSWORD}@{self.MONGODB_CLUSTER}")
            self.client.list_database_names()
            return True
        except:
            return False

    def setNamespace(self, namespace):
        try:
            self.database = self.client[namespace]
            return True
        except:
            return False

    def setCollection(self, collection):
        try:
            self.collection = self.database[collection]
            self.collection.find_one()
            return True
        except:
            return False
    
    def addOneDocumentInsert(self, _object):
        try:
            objectId = self.collection.insert_one(_object).inserted_id
            return True, objectId
        except:
            return False
    
    def addOneDocumenUpdateUpsert(self, _object):
        try:
            self.collection.update_one({},{"$set":_object}, upsert=True)
            return True
        except:
            return False

    def getDocumentById(self, objectId):
        try:
            _object = self.collection.find_one({"_id": objectId})
            return True, _object
        except:
            return False

    def addManyDocuments(self, listObject):
        try:
            objectIds = self.collection.insert_many(listObject).inserted_ids
            return True, objectIds
        except:
            return False

    def getDocumentsCount(self):
        try:
            documentCount = self.collection.count_documents({})
            return True, documentCount
        except:
            return False

    def getDocumentCountFilter(self, objectDict):
        try:
            documentCount = self.collection.count_documents(objectDict)
            return True, documentCount
        except:
            return False
    
    def deleteOneDocumentsByKeyValue(self, objectDict):
        try:
            self.collection.delete_one(objectDict)
            return True
        except:
            return False

    def deleteManyDocumentsByKeyValue(self, objectDict):
        try:
            self.collection.delete_many(objectDict)
            return True
        except:
            return False

    def deleteAllDocuments(self):
        try:
            self.collection.delete_many({})
            return True
        except:
            return False