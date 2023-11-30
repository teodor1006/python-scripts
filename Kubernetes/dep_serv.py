from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Common constants
NAMESPACE = "default"
APP_NAME = "<name>"
CONTAINER_NAME = "<container-name>"
IMAGE_NAME = "<image-name>"
CONTAINER_PORT = <container-port>
SERVICE_PORT = <port>

def create_deployment(api_instance):
    deployment = client.V1Deployment(
        metadata=client.V1ObjectMeta(name=APP_NAME),
        spec=client.V1DeploymentSpec(
            replicas=1,
            selector=client.V1LabelSelector(match_labels={"app": APP_NAME}),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels={"app": APP_NAME}),
                spec=client.V1PodSpec(
                    containers=[
                        client.V1Container(
                            name=CONTAINER_NAME,
                            image=IMAGE_NAME,
                            ports=[client.V1ContainerPort(container_port=CONTAINER_PORT)]
                        )
                    ]
                )
            )
        )
    )

    api_instance.create_namespaced_deployment(namespace=NAMESPACE, body=deployment)

def create_service(api_instance):
    service = client.V1Service(
        metadata=client.V1ObjectMeta(name=APP_NAME),
        spec=client.V1ServiceSpec(
            selector={"app": APP_NAME},
            ports=[client.V1ServicePort(port=SERVICE_PORT)]
        )
    )

    api_instance.create_namespaced_service(namespace=NAMESPACE, body=service)

if __name__ == "__main__":
    # Create Kubernetes API clients
    apps_api_instance = client.AppsV1Api(client.ApiClient())
    core_api_instance = client.CoreV1Api(client.ApiClient())

    # Create deployment and service
    create_deployment(apps_api_instance)
    create_service(core_api_instance)
