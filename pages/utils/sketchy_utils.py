
def normalize_labels(label):
    return label.capitalize().replace("_", " ")

def gcs_list_folders(bucket, prefix="", delimeter="/", guess_lexicographically_last_item="~", gcs_client=None):
    folders = set()
    prefix_parts = prefix.split(delimeter)
    start_offset = "/".join(prefix_parts)
    last_blob_name = None
    while True:
        blobs = list(gcs_client.list_blobs(
            bucket_or_name=bucket,
            prefix=prefix,
            start_offset=start_offset,
            max_results=1
        ))
        if not blobs:
            break
        blob = blobs[0]
        if last_blob_name == blob.name:
            raise Exception("Saw blob {} twice, try setting a different guess_lexicographically_last_item={}.".format(
                repr(blob.name), repr(guess_lexicographically_last_item)
            ))
        folder = delimeter.join(blob.name.split(delimeter)[0:len(prefix_parts)] + [""])
        folders.add(folder)
        start_offset = folder + guess_lexicographically_last_item
        last_blob_name = blob.name
        try_characters = 1

    return folders

def gcs_list_files(bucket, prefix=""):
    return list(bucket.list_blobs(prefix=prefix))

def gcs_download_image_bytes(bucket, path):
    content = bucket.blob(path).download_as_bytes()
    return content
