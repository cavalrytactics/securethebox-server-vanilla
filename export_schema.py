import json
from app_schema.schema import schema
import subprocess
import sys
from graphql.utils import schema_printer

my_schema_str = schema_printer.print_schema(schema)
# fp = open("schema.graphql", "w")
# fp.write(my_schema_str)
# fp.close()


# introspection_dict = schema.introspect()

# print(introspection_dict)
# Print the schema in the console
# print(json.dump(introspection_dict))

# # Or save the schema into some file
with open('schema.json', "w") as fp:
   fp.write(my_schema_str)

subprocess.Popen([f"cp schema.json ../securethebox-client-vanilla/data/schema.json"],shell=True).wait()