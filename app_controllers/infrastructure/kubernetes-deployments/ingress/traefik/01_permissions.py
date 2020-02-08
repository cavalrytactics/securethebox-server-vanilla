import sys

def writeConfig(**kwargs):
    template = """
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: cluster-admin
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: User
  name: {emailAddress}
              """

    with open('./app_controllers/infrastructure/kubernetes-deployments/ingress/'+str(sys.argv[2])+'/01_permissions-'+str(sys.argv[1])+'-'+str(sys.argv[2])+'.yml', 'w') as yfile:
        yfile.write(template.format(**kwargs))


if __name__ == "__main__":
  writeConfig(clusterName=str(sys.argv[1]), serviceName=str(sys.argv[2]), emailAddress=str(sys.argv[3]))