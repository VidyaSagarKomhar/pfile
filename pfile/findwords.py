from google.cloud import storage

def read_file_words(bucket_name,file_path):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_path)
    read_each_file = blob.download_as_text(encoding="utf-8")
    words = read_each_file.split()
    print('The len of the files {}'.format(len(words)))
    return len(words)
