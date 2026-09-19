# SAS Customer Intelligence 360

## SAS 360 API MARKETING DATA LIBRARY

> **Status: superseded.** This library has been replaced by [`sas-ci360-sol-data`](https://github.com/mnelson3/sas-ci360-sol-data) — the same Marketing Data API, rebuilt with mockable unit tests, typed exceptions, and safer configuration defaults. This repo is kept for historical reference; start new work in `sas-ci360-sol-data` instead.

### Overview

The Marketing Data API for SAS Customer Intelligence 360 provides endpoints for analytic and customer tables. The Marketing Data API for SAS Customer Intelligence 360 enables you to manage data for customers and upload an allowlist or denylist for recommendations. You can use this REST API to perform these actions:
 * fulfill GDPR requests
 * import and update customer data
 * get identity records
 * control product recommendations

For detailed information on REST API:<br>
https://support.sas.com/documentation/onlinedoc/ci/ci360-apis/marketingData/v1/redoc.html
<br><br>

### Table of Contents

This topic contains the following sections:

 - <a href="#prerequisites">Prerequisites</a>
 - <a href="#installation">Installation</a>
 - <a href="#getting-started">Getting Started</a>
 - <a href="#api-marketing-data-code">API Marketing Data Code</a>
 - <a href="#troubleshooting">Troubleshooting</a>
 - <a href="#contributing">Contributing</a>
 - <a href="#license">License</a>
 - <a href="#additional-resources">Additional Resources</a>
<br><br>

### Prerequisites

 * Required Python: >=3.6
 * Customer Intelligence 360 Tenant with Administrative Rights
 * SAS CI360 API Core Library:<br>
   https://github.com/mnelson3/sas_ci360_api_core
<br><br>

### Installation

To install the SAS CI360 API Marketing Data Library from a clone of this repository:
 1. `git clone https://github.com/mnelson3/sas_ci360_api_marketing_data.git`
 1. `cd sas_ci360_api_marketing_data`
 1. `pip install .`
<br><br>

### Getting Started

While this library is available for review, please note that it is considered a work in process and NOT considered "released for production".
<br><br>

### API Marketing Data Code

 1. Analytics Services - Contains the operations for the analytic services.
 1. Customer Jobs - Contains calls that create, change, move, or delete customer information. These calls are used for GDPR requests.
 1. File Transfer Location - Contains a call to generate and return a signed URL. Use this URL to upload a file directly to a cloud storage location.
 1. Identity Records - Contains calls that return identity record information. You can also use the Diagnostics page in the user interface to view identity records. For more information, see Diagnostic Reports in the Administration Guide.
 1. Import Request Jobs - Contains calls that create or retrieve requests to upload data to customer tables. You can also upload customer data through the user interface. For more information, see Upload Customer Data.
 1. Root - Contains the operations for the root resource.
 1. Table Jobs - Contains calls to create, retrieve, or update data for a table.
 1. Tables - Contains calls that return information for existing tables.
<br><br>

### Troubleshooting

For issues specific to sasci360apicore or sasci360apimarketingdata try updating the libraries.

To update sasci360apicore:
 1. Pull the latest changes from a clone of the [sas_ci360_api_core](https://github.com/mnelson3/sas_ci360_api_core) repository
 1. Open a terminal window (Unix/macOS) or command prompt (Windows) in that clone
 1. Copy and paste the following line at the cursor<br>
    pip install --upgrade .
 1. Press "Enter"<br>
    The SAS CI360 API Core Library should install

To update sasci360apimarketingdata:
 1. Pull the latest changes from a clone of this repository
 1. Open a terminal window (Unix/macOS) or command prompt (Windows) in that clone
 1. Copy and paste the following line at the cursor<br>
    pip install --upgrade .
 1. Press "Enter"<br>
    The SAS CI360 API Marketing Data Library should install
<br><br>

### Contributing

We welcome your contributions! Please read [CONTRIBUTING](CONTRIBUTING.md) for details on how to submit contributions to this project.
<br><br>

### License

This project is licensed under the [Nelson Grey LLC Community License 1.0](LICENSE).

- **Free for individuals, education, and research**: use, modify, and distribute this software for non-commercial purposes
- **Commercial evaluation**: evaluate the software for a possible commercial use, free of charge
- **Commercial production use**: requires a commercial license from Nelson Grey LLC
- **Automatic conversion**: on December 13, 2029, this automatically converts to the Apache License 2.0

For commercial licensing inquiries, contact support@nelsongrey.com.

### Additional Resources

For more information, see [REST APIs](https://go.documentation.sas.com/doc/en/cintcdc/production.a/cintapis/ch-rest-apis.htm).
<br><br>
