# attachmentav-sdk-python

A virus scan SDK for Python. Scan files for viruses, trojans, and other kinds of malware with attachmentAV.

## Getting started

First, install the module.

```sh
pip install attachmentav-virus-malware-scan-sdk
```

Second, get an API key by [subscribing to the attachmentAV API (SaaS)](https://attachmentav.com/subscribe/api/).

Third, send a scan request. Make sure to replace the `<API_KEY_PLACEHOLDER>` placeholder.

```python
import attachmentav

configuration = attachmentav.Configuration()
# When using the SaaS offering
configuration.api_key['apiKeyAuth'] = "<API_KEY_PLACEHOLDER>"
# When using the self-hosted offering, replace attachmentav.yourcompany.com with the domain name of your attachmentAV API installation: https://attachmentav.com/help/virus-malware-scan-api-aws/developer/definition.html#domain-name
#configuration.access_token = "<API_KEY_PLACEHOLDER>"
#configuration.host = "https://attachmentav.yourcompany.com/api/v1"

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)

with open("/path/to/file", "rb") as file:
    file_content = file.read()
    scan_result = api_instance.scan_sync_binary_post(file_content)
    print(scan_result)
```

The request returns a scan result similar to the following example.

```
{"status":"clean","size":"1024","realfiletype":"..."}
```

## What is attachmentAV?

[attachmentAV](https://attachmentav.com) offers antivirus for SaaS and cloud platforms. Scan your files and attachments stored in the cloud for viruses, worms, and trojans. attachmentAV detects malware in real-time. Supports Amazon S3, Atlassian, Cloudflare R2, Salesforce, WordPress, and more.

The [attachmentAV Virus and Malware Scan API](https://attachmentav.com/solution/virus-malware-scan-api/) provides a REST API that allows you to integrate malware scans into your application. The solution comes in two variants:

* [attachmentAV Virus Scan API (SaaS)](https://attachmentav.com/help/virus-malware-scan-api/setup-guide/): Get started quickly with a fully managed service.
* [attachmentAV Virus Scan API (self-hosted on AWS)](https://attachmentav.com/help/virus-malware-scan-api-aws/setup-guide/): Deploy the production-ready API on AWS.

attachmentAV raises the bar for information security. Our solution is ISO 27001 certified and GDPR compliant. We are establishing, implementing, maintaining, and continually improving an information security management system (ISMS). Sensitive data is encrypted in transit as well as at rest and deleted immediately after processing. More than 1,000 customers trust our malware protection technology.

## Install SDK

```sh
pip install attachmentav-virus-malware-scan-sdk
```

## Configure SDK

### Configure SDK (SaaS)

An [active subscription and API key](https://attachmentav.com/help/virus-malware-scan-api/setup-guide/#api-key) are required. Replace `<API_KEY_PLACEHOLDER>` with the API key.

```python
import attachmentav

configuration = attachmentav.Configuration()
configuration.api_key['apiKeyAuth'] = "<API_KEY_PLACEHOLDER>"

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)
```

### Configure SDK (self-hosted on AWS)

When following the setup guide, you specified the `ApiKeys` parameter for the CloudFormation stack. Replace `<API_KEY_PLACEHOLDER>` with one of those keys. 

```python
import attachmentav

configuration = attachmentav.Configuration()
configuration.access_token = "<API_KEY_PLACEHOLDER>"
configuration.host = "https://attachmentav.yourcompany.com/api/v1"

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)
```

## Examples


### Sync Scan: File

Send a file to the attachmentAV Virus Scan API and process the scan result.

See [ScanResult](sdk/docs/ScanResult.md) for details.

The maximum file size is 10 MB. The request timeout is 60 seconds.


```python
with open("/path/to/file", "rb") as file:
    file_content = file.read()
    scan_result = api_instance.scan_sync_binary_post(file_content)
    print(scan_result)
```

### Sync Scan: Download

Send a URL to the attachmentAV Virus Scan API. attachmentAV will download the file and return the scan result immediately.


See [SyncDownloadScanRequest](sdk/docs/SyncDownloadScanRequest.md) and [ScanResult](sdk/docs/ScanResult.md) for details.

The maximum file size is 10 MB. The request timeout is 60 seconds.


```python
sync_download_scan_request = attachmentav.SyncDownloadScanRequest(
  download_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
)
scan_result = api_instance.scan_sync_download_post(sync_download_scan_request)
print(scan_result)
```

### Sync Scan: S3

Send an S3 bucket name and object key to the attachmentAV Virus Scan API. attachmentAV will download the file and return the scan result immediately.

See [SyncS3ScanRequest](sdk/docs/SyncS3ScanRequest.md) and [ScanResult](sdk/docs/ScanResult.md) for details.

The maximum file size is 10 MB. The request timeout is 60 seconds.

> A [bucket policy](https://attachmentav.com/help/virus-malware-scan-api/setup-guide/#s3-bucket-policy) is required to grant attachmentAV access to private S3 objects.

```python
sync_s3_scan_request = attachmentav.SyncS3ScanRequest(
  bucket = "<BUCKET_NAME_PLACEHOLDER>",
  key = "<OBJECT_KEY_PLACEHOLDER>"
)
scan_result = api_instance.scan_sync_s3_post(sync_s3_scan_request)
print(scan_result)
```

### Async Scan: Download (callback)

Send a URL to the attachmentAV Virus Scan API. attachmentAV will send the scan result to the callback URL. See [callback URL](https://attachmentav.com/help/virus-malware-scan-api/setup-guide/#callback-url) for details.

See [AsyncDownloadScanRequest](sdk/docs/AsyncDownloadScanRequest.md) for details.

The maximum file size is 5 GB. The request timeout is 29 seconds; the asynchronous scan job is not affected by this limit.

> Not supported by attachmentAV Virus Scan API (Self-hosted on AWS) yet. Contact [hello@attachmentav.com](hello@attachmentav.com) to let us know, in case you need this feature. 

```python
async_download_scan_request = attachmentav.AsyncDownloadScanRequest(
  download_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
  callback_url = "https://api.yourcompany.com/attachmentav/callback"
)
api_instance.scan_async_download_post(async_download_scan_request)
print("Async download submitted")
```

Find full example [here](https://github.com/widdix/attachmentav-sdk-python/blob/main/examples/async-download.py)

### Async Scan: Download (polling)

Send a URL to the attachmentAV Virus Scan API. attachmentAV will download the file and store the scan result for 24 hours.

See [AsyncDownloadScanRequest](sdk/docs/AsyncDownloadScanRequest.md) for details.

The maximum file size is 5 GB. The request timeout is 29 seconds; the asynchronous scan job is not affected by this limit.

> Not supported by attachmentAV Virus Scan API (Self-hosted on AWS) yet. Contact [hello@attachmentav.com](hello@attachmentav.com) to let us know, in case you need this feature. 

```python
trace_id = str(uuid.uuid4())

async_download_scan_request = attachmentav.AsyncDownloadScanRequest(
  download_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
  trace_id = trace_id
)
api_instance.scan_async_download_post(async_download_scan_request)
print("Async download submitted.")

# wait some time...

scan_result = api_instance.scan_async_result_get(trace_id)
print(scan_result)
```

Find full example [here](https://github.com/widdix/attachmentav-sdk-python/blob/main/examples/async-download-polling.py)

### Async Scan: S3 (callback)

Send an S3 bucket name and object key to the attachmentAV Virus Scan API. attachmentAV will send the scan result to the callback URL. See [callback URL](https://attachmentav.com/help/virus-malware-scan-api/setup-guide/#callback-url) for details.

See [AsyncS3ScanRequest](sdk/docs/AsyncS3ScanRequest.md) for details.

The maximum file size is 5 GB. The request timeout is 29 seconds; the asynchronous scan job is not affected by this limit.

> A [bucket policy](https://attachmentav.com/help/virus-malware-scan-api/setup-guide/#s3-bucket-policy) is required to grant attachmentAV access to private S3 objects.

> Not supported by attachmentAV Virus Scan API (Self-hosted on AWS) yet. Contact [hello@attachmentav.com](hello@attachmentav.com) to let us know, in case you need this feature.

```python
async_s3_scan_request = attachmentav.AsyncS3ScanRequest(
  bucket = "<BUCKET_NAME_PLACEHOLDER>",
  key = "<OBJECT_KEY_PLACEHOLDER>",
  callback_url = "https://api.yourcompany.com/attachmentav/callback"
)
api_instance.scan_async_s3_post(async_s3_scan_request)
print("Async S3 submitted")
```

Find full example [here](https://github.com/widdix/attachmentav-sdk-python/blob/main/examples/async-s3.py)

### Async Scan: S3 (polling)

Send an S3 bucket name and object key to the attachmentAV Virus Scan API. attachmentAV will download the file and store the scan result for 24 hours.

See [AsyncS3ScanRequest](sdk/docs/AsyncS3ScanRequest.md) for details.

The maximum file size is 5 GB. The request timeout is 29 seconds; the asynchronous scan job is not affected by this limit.

> A [bucket policy](https://attachmentav.com/help/virus-malware-scan-api/setup-guide/#s3-bucket-policy) is required to grant attachmentAV access to private S3 objects.

> Not supported by attachmentAV Virus Scan API (Self-hosted on AWS) yet. Contact [hello@attachmentav.com](hello@attachmentav.com) to let us know, in case you need this feature.

```python
trace_id = str(uuid.uuid4())

async_s3_scan_request = attachmentav.AsyncS3ScanRequest(
  bucket = "<BUCKET_NAME_PLACEHOLDER>",
  key = "<OBJECT_KEY_PLACEHOLDER>",
  trace_id = trace_id
)
api_instance.scan_async_s3_post(async_s3_scan_request)
print("Async S3 submitted. ")

# wait some time...

scan_result = api_instance.scan_async_result_get(trace_id)
print(scan_result)
```

Find full example [here](https://github.com/widdix/attachmentav-sdk-python/blob/main/examples/async-s3-polling.py)

### Usage

Get remaining credits and quota.

See [Usage](sdk/docs/Usage.md) for details.

> Not supported by attachmentAV Virus Scan API (Self-hosted on AWS).

```python
usage_result = api_instance.usage_get()
print(usage_result)
```

### Who am I

Get information abour yourself.

See [Whoami](sdk/docs/Whoami.md) for details.

> Not supported by attachmentAV Virus Scan API (Self-hosted on AWS).

```python
whoami_result = api_instance.whoami_get()
print(whoami_result)
```

## Model

For more details about the data model, please refer to the following pages.

* [AsyncDownloadScanRequest](sdk/docs/AsyncDownloadScanRequest.md)
* [AsyncS3ScanRequest](sdk/docs/AsyncS3ScanRequest.md)
* [AttachmentAVApi](sdk/docs/AttachmentAVApi.md)
* [ScanResult](sdk/docs/ScanResult.md)
* [SyncDownloadScanRequest](sdk/docs/SyncDownloadScanRequest.md)
* [SyncS3ScanRequest](sdk/docs/SyncS3ScanRequest.md)
* [Usage](sdk/docs/Usage.md)
* [Whoami](sdk/docs/Whoami.md)

## Need help?

Do you need any help to get started with attachmentAV? [hello@attachmentav.com](mailto:hello@attachmentav.com).
