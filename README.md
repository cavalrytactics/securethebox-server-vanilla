# securethebox-server-vanilla

## Application Flow

1. app_models/ help model the data a Class used for app_controllers/
  - Creates a structure to re-use code

2. app_controllers/ are used to interact with interna/external service APIs
  - A service will have multiple functions within a Class
  - Deploying/Configuring Kubernetes Clusters/Pods/etc 
  - Setting up services over API requests

3. app_managers/ is used by app_routes/
  - Packed functions to perform a broad action for a specific service

4. app_routes/ is used by apiv1/apiv2 blueprints
  - Backend API endpoints/routes

5. apiv1/apiv2 blueprints are used by main.py (Flask)
  - Divides up API versions for future development
  - apiv1 is traditional REST API
  - apiv2 is reserved for GraphQL functionality