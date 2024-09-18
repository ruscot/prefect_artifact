# Installation

Create virtual env for python:
```bash
python3 -m venv venv/
```
Activate virtual env:
```bash
source venv/bin/activate
```
Install prefect and pandas:
```bash
pip install -U prefect pandas
```
Connect to prefect cloud:
```bash
prefect cloud login
```
Link https://app.prefect.cloud/