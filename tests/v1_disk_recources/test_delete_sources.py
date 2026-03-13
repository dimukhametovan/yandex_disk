import allure
import pytest

@pytest.mark.done
@allure.title("DELETE /disk/resources 204 Happy Path")
def test_delete_file_to_trash_sync(delete_api):
    path = "test/test_copy.txt"

    response = delete_api.delete(path=path, permanently=False, force_async=False)
    response.assert_status(204) 
    
@pytest.mark.done
@allure.title("DELETE /disk/resources 202 Happy Path - Async")
def test_delete_file_async(delete_api):
    path = "/test/test_copy.bin"

    response = delete_api.delete(path=path, force_async=True, permanently=False)

    response.assert_status(202)
    response.assert_has_fields("href", "method", "templated")
    response.assert_field_type("href", str)
    

@pytest.mark.done
@allure.title("DELETE /disk/resources permanently=true")
def test_delete_file_permanently(delete_api):
    path = "/test/test_copy.txt"

    response = delete_api.delete(path=path, permanently=True, force_async=False)
    response.assert_status_in({202, 204})
    
@pytest.mark.done
@allure.title("DELETE /disk/resources: 404 DiskNotFoundError")
def test_delete_non_existing_resource(delete_api):
    path = "/does-not-exist"

    response = delete_api.delete(path=path, permanently=True)
    response.assert_status(404)
    response.assert_has_fields("error", "message", "description")
    response.assert_error("DiskNotFoundError")


