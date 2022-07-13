import json
import os
import re

import requests

import main


def download_dependency_as_tar(url: str, filename: str, target_dir: str):
    response = requests.get(url, stream=True)
    if response.status_code == 200:

        fname = ''
        if "Content-Disposition" in response.headers.keys():
            fname = re.findall("filename=(.+)", response.headers["Content-Disposition"])[0]
        else:
            fname = url.split("/")[-1]

        print(fname)

        head, _ = os.path.split(os.path.join(target_dir, filename))
        os.makedirs(head, exist_ok=True)
        with open(f'{target_dir}/{fname}', 'wb') as f:
            f.write(response.raw.read())
    return url


def download_tar():
    package_lock_file = json.load(open('source/package-lock.json'))
    target_dir = 'downloaded_packages'

    for package_name, package_data in package_lock_file['dependencies'].items():
        print(f'Processing {package_name}')

        download_dependency_as_tar(package_data['resolved'], package_name, target_dir)


if __name__ == '__main__':
    download_tar()
