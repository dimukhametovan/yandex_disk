import allure
import pytest

@pytest.mark.done
@allure.title("PUT v1/disk/resources Happy Path")
def test_create_folder_success(folder_api):
	path = "test_folder"
	response = folder_api.create(path=path)
	response.assert_status(201)
	response.assert_has_fields("method", "href", "templated")
	response.assert_field_contains("href", path)

@pytest.mark.done
@allure.title("PUT v1/disk/resources 409 DiskPathPointsToExistentDirectoryError")
def test_create_existing_folder(folder_api):
	path = "test_folder"
	folder_api.create(path=path)
	response = folder_api.create(path=path)
	response.assert_status(409)
	response.assert_error("DiskPathPointsToExistentDirectoryError")

