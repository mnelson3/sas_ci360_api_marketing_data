#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Customer Jobs Module
Contains calls that create, change, move, or delete customer information. These calls are used for GDPR requests.
	1. get_customer_job(self, customer_job_id: str) -> requests.Response
	2. create_customer_job(self, payload: dict) -> requests.Response
"""

import os
import unittest
from sasci360apimarketingdata import customer_jobs


class TestCustomerJobs(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingData"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.customer_jobs = customer_jobs.CustomerJobs(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_customer_job(self):
		"""
		1. get_customer_job(self, customer_job_id: str) -> requests.Response
		"""
		customer_job_id = "0"
		result = self.customer_jobs.get_customer_job(customer_job_id=customer_job_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_customer_job(self):
		"""
		2. create_customer_job(self, payload: dict) -> requests.Response
		"""
		payload = {
			"jobType": "GDPR_EXPORT",
			"identityType": "subject_id",
			"identityList": ["12343455"],
			"outputIdentityTypes": ["login_id", "subject_id", "visitor_id"]
		}
		result = self.customer_jobs.create_customer_job(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
