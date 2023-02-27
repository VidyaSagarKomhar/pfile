from google.cloud import storage

def read_file_words(datastring):
    words = datastring.split()
    print('The len of the files {}'.format(len(words)))
    return len(words)
