import asyncio
import glob
import aioipfs
import json

source = './downloaded_packages'

files = glob.glob(source + '/**/*.tgz', recursive=True)

client = aioipfs.AsyncIPFS()

filename_to_hash = {}


async def add_files(files):
    async for added_file in client.add(*files, recursive=True):
        print(added_file)
        print('Imported file {0}, CID: {1}'.format(
            added_file['Name'], added_file['Hash']))
        async for f in client.pin.add(added_file['Hash']):
            print(f'Pinned file {f}')
            filename_to_hash[added_file['Name']] = added_file['Hash']
    await client.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(add_files(files))
loop.close()

with open('filename_to_cid.json', 'w') as f:
    json.dump(filename_to_hash, f)
