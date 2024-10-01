import requests
from requests.adapters import HTTPAdapter, Retry
import requests
import os
from PIL import Image
from io import BytesIO
import pandas as pd


def download_curated_sequence(sequence_id_vec, path_to_images_ids):
    # This function downloads the images of a sequence given the sequence ID and the path to the sequences images.
    # The images are downloaded in the 'downloads' folder (auto created)

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    # This is the access token for the Mapillary API. You can get your own access token by signing up on the Mapillary website and creating an application.
    access_token = 'fill_in_your_access_token'

    # For each sequence, we get the image IDs and download the images.
    for sequence_id in sequence_id_vec:
        url = 'https://graph.mapillary.com/image_ids?sequence_id={}'.format(
            sequence_id)
        header = {'Authorization': 'OAuth {}'.format(access_token)}
        r = requests.get(url, headers=header)
        data = r.json()

        if not os.path.exists('downloads/' + sequence_id):
            os.makedirs('downloads/' + sequence_id)

        cured_img_ids = pd.read_csv(
            path_to_images_ids + '/' + sequence_id + '/' + sequence_id + '_cured_data.txt', header=None)

        # Use of a session to handle retries in case of network errors.
        s = requests.Session()
        retries = Retry(total=5, backoff_factor=1,
                        status_forcelist=[502, 503, 504])
        s.mount('http://', HTTPAdapter(max_retries=retries))

        # For each image, we get the image data and save the image.
        for i in range(len(cured_img_ids)):
            image_url = 'https://graph.mapillary.com/{}?fields=thumb_original_url, geometry, computed_compass_angle'.format(
                cured_img_ids[1][i])
            img_r = s.get(image_url, headers=header)
            img_data = img_r.json()
            image_get_url = img_data['thumb_original_url']

            with open('downloads' + '/{}/{}.jpg'.format(sequence_id, cured_img_ids[1][i]), 'wb') as handler:
                image_data = s.get(image_get_url, stream=True).content
                image = Image.open(BytesIO(image_data))
                save_path = 'downloads' + \
                    '/{}/{}.jpg'.format(sequence_id, cured_img_ids[1][i])
                image.save(save_path)
                print('Downloaded image ', cured_img_ids[1][i])


if __name__ == "__main__":

    # List of sequences to download
    sequence_id_vec_tsukuba = ['JhXV7GKUIpaAi9jZlWSvsq',
                               'SdgiezUl5pDFBY9avcfux1']
    sequence_id_vec_paris = ['9ax8up9b5cptf92ueyowam',
                             '8jhok49ioq2z1qey83axiz']
    sequence_id_vec_paris_2 = [
        'i2PZwEzhAWag8tl9xJcQXo', 'gsOUFN18HjZlzKIhm4C7EX']
    sequence_id_vec_brussels = [
        'w9e18WNtvRsxKL5noJ3fhI', 'oXcMxLCK3eGgDfH7tN8Qir']
    sequence_id_vec_berlin = [
        'v5alNyCdc3P2F7IfhYg10n', 'AQY9PT3g8JawW2dpjqUro5']
    sequence_id_vec_morlaix = [
        '1a1vWkPJjtJ8fBxVJhFKDw', '6mvmqd2hd0f9npy8kh5lpx']
    sequence_id_vec_niigata = [
        '5u6ffmp08ymli80jx0assa', 'J2QFAtzaTiCPOGx1DuIvWK']
    sequence_id_vec_tsukuba_1 = [
        'FAPGX6yCUNBJknfriRKeOz', 'XDJLbxr5uc3wRTSEsV4I2A']

    # To test and download a single sequence
    download_curated_sequence(sequence_id_vec_paris_2,
                              'sequences_ids/')

    #######################################################
    # Uncomment the following lines to download all sequences

    # all_sequences = [sequence_id_vec_tsukuba, sequence_id_vec_paris, sequence_id_vec_paris_2,
    #               sequence_id_vec_brussels, sequence_id_vec_berlin, sequence_id_vec_morlaix, sequence_id_vec_niigata, sequence_id_vec_tsukuba_1]

    # for i in range(len(all_sequences)):
    # download_full_sequence(all_sequences[i])
    # print("Downloaded sequence ", i)
    # cure_pair_sequences(all_sequences[i])
    # print("Cured sequence ", i)
