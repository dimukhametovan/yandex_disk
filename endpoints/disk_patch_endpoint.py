from core.base_endpoint import BaseEndpoint

class ResourcesPatchEndpoint(BaseEndpoint):
	def patch(self, path, body=None, fields=None):
		params = {
			"path": path
		}
		if fields:
			params["fields"] = ",".join(fields)
		return self.request("PATCH", "/resources", params=params, json=body)