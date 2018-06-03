from ftplib import FTP
from pathlib import Path
import gzip
import argparse

filename = "ratings.list.gz"


parser = argparse.ArgumentParser()
parser.add_argument('--download', help='URL of the file',
                    default='ftp.fu-berlin.de/pub/misc/movies/database/'
                            'frozendata/ratings.list.gz')
args = parser.parse_args()

url = args.download
file_address = url.split('/')[0]
file_path = url[url.find('/'):url.rfind('/')]
file_name = url.split('/')[-1]
loc_file_path = Path(filename)

if not loc_file_path.exists():
    ftp = FTP()
    ftp.set_pasv("")
    ftp.connect(file_address)
    ftp.login()
    ftp.cwd(file_path)
    ftp.retrlines('LIST')
    local_file = open(loc_file_path, "wb")
    ftp.retrbinary("RETR " + filename, local_file.write, 8*1024)
    local_file.close()

with gzip.open(filename) as f:
    file_content = f.read()
    print(file_content)

with open("{}.txt".format(file_name), 'wb') as f:
    f.write(file_content)

