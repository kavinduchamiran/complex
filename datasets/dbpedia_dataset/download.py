import requests

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

if __name__ == "__main__":
    # big files
    # file_id = '1tArkcc43b4D7mpuZPikHShSRj7ZxOl2g'
    # destination = 'valid.txt'
    # download_file_from_google_drive(file_id, destination)
    #
    # file_id = '1D3exaccibg3AD0Y66QlRmNB8tRYIxBuU'
    # destination = 'train.txt'
    # download_file_from_google_drive(file_id, destination)
    #
    # file_id = '1WpmwWTcuaISBNuUzkGdK58DOUtMKuCP_'
    # destination = 'test.txt'
    # download_file_from_google_drive(file_id, destination)

    # small files
    file_id = '1qRf9e3ykSXDoGH7wm5_B_i9l3p2nnI29'
    destination = 'valid.txt'
    download_file_from_google_drive(file_id, destination)

    file_id = '1MJFB7FKrMKnuDuZDzqfilKKWcKtQKMA9'
    destination = 'train.txt'
    download_file_from_google_drive(file_id, destination)

    file_id = '1Ki7E3QNENPuXkJD5KC7gakHK-_A_3m7W'
    destination = 'test.txt'
    download_file_from_google_drive(file_id, destination)

