import allure


@allure.title("PATCH v1/disk/resources Happy Path")
def test_patch_source(patch_api):
	path = "/test/test.bin"
	body = {"custom_properties": {"custom_property": "custom"}}
	response = patch_api.patch(path=path, body=body)
	response.assert_status(200)
	print(response.json())
	response.assert_field('custom_properties', {"custom_property": "custom"})



@allure.title("PATCH v1/disk/resources 500 InternalServerError")
def test_patch_source_invalid_body(patch_api):
	path = "/test/test.bin"
	body =  {"custom_properties": ""}
	response = patch_api.patch(path=path, body=body)
	response.assert_status(500)
	response.assert_error("InternalServerError")
