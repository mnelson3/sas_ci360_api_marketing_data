#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Table Jobs Module
Contains calls to create, retrieve, or update data for a table.
	1. get_table_job(self, table_job_id: str) -> requests.Response
	2. create_table_job(self, payload: dict) -> requests.Response
"""

import os
import unittest
from sasci360apimarketingdata import table_jobs


class TestTableJobs(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingData"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.table_jobs = table_jobs.TableJobs(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_table_job(self):
		"""
		1. get_table_job(self, table_job_id: str) -> requests.Response
		"""
		table_job_id = "0"
		result = self.table_jobs.get_table_job(table_job_id=table_job_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_table_job(self):
		"""
		2. create_table_job(self, payload: dict) -> requests.Response
		"""
		payload = {
			"jobType": "TABLE_DOWNLOAD",
			"dataDescriptorId": "5fa29779-88ba-46ff-a1c4-d2bd227e0164",
			"fileLocation": "",
			"headerRowIncluded": "",
			"includeSourceAndTimestamp": ""
		}
		result = self.table_jobs.create_table_job(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
