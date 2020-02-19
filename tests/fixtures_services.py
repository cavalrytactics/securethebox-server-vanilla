import pytest
from app_models.graphql.services.models import Service, Application, Configuration, Credential

def fixture_service_data():
    Service.drop_collection()
    service_one = Service(
        name="Load balancer",
        value="load_balancer",
    )
    service_one.save()
    service_two = Service(
        id="5e4b28e7fae1c6e30caccb66",
        name="Intrusion detection system",
        value="intrusion_detection_system",
    )
    service_two.save()

@pytest.fixture(scope="module")
def fixtures_data():
    fixture_service_data()
    return True