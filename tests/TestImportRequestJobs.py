#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Import Request Jobs Module
Contains calls that create or retrieve requests to upload data to customer tables.
	1. get_import_requests(self, **kwargs) -> requests.Response
	2. create_import_request(self, payload: dict) -> requests.Response
	3. get_import_request(self, import_request_job_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apimarketingdata import import_request_jobs


class TestImportRequestJobs(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingData"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.import_request_jobs = import_request_jobs.ImportRequestJobs(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_import_requests(self):
		"""
		1. get_import_requests(self, **kwargs) -> requests.Response
		"""
		result = self.import_request_jobs.get_import_requests()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_import_request(self):
		"""
		2. create_import_request(self, payload: dict) -> requests.Response
		"""
		payload = {
			"name": "test import",
			"dataDescriptorId": "eaa43b2f-05d3-4460-9448-ce480fcf507f",
			"fieldDelimiter": ",",
			"fileLocation": "https://<server>/transfers/2018071611/18e7986aa6c442038b1f33f334d8b79a?X-Amz-Security-Token=<token>&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210815T214314Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=<credential>&X-Amz-Signature=<signature>",
			"fileType": "CSV",
			"headerRowIncluded": True,
			"recordLimit": 0,
			"updateMode": "upsert"
		}
		result = self.import_request_jobs.create_import_request(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_import_request(self):
		"""
		3. get_import_request(self, import_request_job_id: str) -> requests.Response
		"""
		import_request_jobs_id = "0"
		result = self.import_request_jobs.get_import_request(import_request_job_id=import_request_jobs_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
