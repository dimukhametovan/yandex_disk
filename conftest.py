import pytest
from endpoints.disk_copy_endpoint import ResourcesCopyEndpoint
from endpoints.disk_info_endpoint import DiskEndpoint
from endpoints.disk_folder_endpoint import FolderEndpoint
from endpoints.disk_delete_endpoint import DeleteEndpoint
from endpoints.disk_patch_endpoint import ResourcesPatchEndpoint


@pytest.fixture
def disk_api():
    return DiskEndpoint()


@pytest.fixture
def unauthorized_disk_api():
    endpoint = DiskEndpoint()
    endpoint.client.session.headers.pop("Authorization", None)
    return endpoint


@pytest.fixture
def copy_api():
    return ResourcesCopyEndpoint()


@pytest.fixture
def folder_api():
    return FolderEndpoint()


@pytest.fixture
def delete_api():
    return DeleteEndpoint()

@pytest.fixture
def patch_api():
    return ResourcesPatchEndpoint()