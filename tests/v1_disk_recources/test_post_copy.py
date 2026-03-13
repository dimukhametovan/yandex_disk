import allure


@allure.title("POST /disk/resources/copy Happy Path - Async")
def test_copy_file_async_success(copy_api):
    src = "/test/test.bin"
    dst = "/test/test_copy.bin"

    response = copy_api.copy(from_path=src, dst_path=dst, force_async=True, overwrite=False)
    response.assert_status(202)
    response.assert_has_fields("href", "method", "templated")
    response.assert_field_type("href", str)


@allure.title("POST /disk/resources/copy Happy Path")
def test_copy_file_sync_success(copy_api):
    src = "/test/test.txt"
    dst = "/test/test_copy.txt"

    response = copy_api.copy(from_path=src, dst_path=dst, force_async=False, overwrite=False)
    response.assert_status(201)
    response.assert_has_fields("href", "method", "templated")
    response.assert_field_type("href", str)


@allure.title("POST /disk/resources/copy DiskNotFoundError")
def test_copy_non_existing_source(copy_api):
    src = "/test/non_existing_file.txt"
    dst = "/test/test_copy.txt"

    response = copy_api.copy(from_path=src, dst_path=dst, force_async=False, overwrite=False)
    response.assert_status(404)
    response.assert_error("DiskNotFoundError")


@allure.title("POST /disk/resources/copy DiskResourceAlreadyExistsError")
def test_copy_existing_destination(copy_api):
    src = "/test/test.txt"
    dst = "/test/test_copy.txt"
    copy_api.copy(from_path=src, dst_path=dst, force_async=False, overwrite=False)

    response = copy_api.copy(from_path=src, dst_path=dst, force_async=False, overwrite=False)
    response.assert_status(409)
    response.assert_error("DiskResourceAlreadyExistsError")

