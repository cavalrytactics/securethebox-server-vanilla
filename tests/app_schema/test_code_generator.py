from app_schema.code_generator import CodeGenerator
import os
import pytest
import json
from app_mutations.courses.mutations import CreateCourseMutation, CourseInput
import importlib
from inspect import isclass, getmembers, isfunction, getmodule
import sys
import inflect

c = CodeGenerator()

def test_loadGlobalData():
    with open(str(os.getcwd())+"/tests/globalData.json", "r") as f:
        pytest.globalData = json.load(f)

def test_setCurrentDirectory():
    assert c.setCurrentDirectory() == True

def test_generateGraphqlFiles():
    gbl = globals()
    moduleToImport = f"app_models.graphql.models"
    for modelName, cls in getmembers(importlib.import_module(moduleToImport), isclass):
        if "Field" not in modelName:
            p = inflect.engine()
            pluralField = p.plural_noun(modelName.lower()).capitalize()
            for subject in pytest.globalData["graphqlSubjects"]:
                if subject == pluralField.lower():
                    print("-->",modelName.lower(),"subject:",subject)
                    assert c.setQueryType("mutation") == True
                    assert c.setSubject(modelName.lower()) == True
                    assert c.setOperationName("create"+modelName.capitalize()) == True

                    gbl = globals()
                    moduleToImport = f"app_mutations.{pluralField.lower()}.mutations"
                    gbl[moduleToImport] = importlib.import_module(moduleToImport)
                    for name, cls in getmembers(importlib.import_module(moduleToImport), isclass):
                        # print(name,cls)
                        if "Input" in name:
                            assert c.setInputClass(cls) == True
                        if "Mutation" in name:
                            assert c.setSubjectMutation(cls) == True
                        assert c.setFields() == True
                        assert c.setSelectionSet() == True
                        assert c.setInputDict() == True
                        c.setInputData()
                        assert c.setQuery() == True
                        assert c.writeFile() == True
                        assert c.copyToFrontend() == True
                    assert c.resetClass() == True


