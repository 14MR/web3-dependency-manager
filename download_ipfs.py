import json


def download_ipfs():
    filename_to_cid = json.load(open('filename_to_cid.json'))
    package_lock_file = json.load(open('source/package-lock.json'))
    target_dir = 'downloaded_packages'

    for package_name, package_data in package_lock_file['dependencies'].items():
        print(f'Processing {package_name} {package_data["resolved"]}')

        filename = package_data['resolved'].split('/')[-1]
        print(filename)
        print(filename_to_cid[filename])
        print(' ')

        requests.get('htt')


if __name__ == '__main__':
    download_ipfs()
