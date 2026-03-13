from core.base_endpoint import BaseEndpoint

class DeleteEndpoint(BaseEndpoint):
    def delete(self, path, force_async=False, md5=None, permanently=False, fields=None):
        params = {
            "path": path,
            "force_async": str(force_async).lower(),
			"permanently": str(permanently).lower(),}
        if md5 is not None:
            params["md5"] = md5
        if fields:
            params["fields"] = ",".join(fields)
        return self.request("DELETE", "/resources", params=params)
