import os
import tarfile
import requests
from paddle_serving_client.io import inference_model_to_serving

# Global Config
DOWNLOAD_TMP_DIR = "./tmp/"
MODEL_DIR = "./models/"


class DownloadError(Exception):
    pass


def download_file(url: str, filename: str):
    path = f"{DOWNLOAD_TMP_DIR}{filename}"
    print(f"Downloading '{url}' to '{path}'...")
    file = requests.get(url, verify=True)
    if file.status_code == 200:
        with open(path, 'wb') as f:
            f.write(file.content)
        print("Download Success!")
    else:
        raise DownloadError(f'path: {path}, url: {url}')


def extract(tar_path, target_path):
    print(f"Extracting file '{tar_path}' to '{target_path}'...")
    try:
        tar = tarfile.open(tar_path, "r:*")
        file_names = tar.getnames()
        for file_name in file_names:
            tar.extract(file_name, target_path)
        tar.close()
        print("Extract Success!")
    except Exception as e:
        raise e


if __name__ == "__main__":
    if not os.path.exists(DOWNLOAD_TMP_DIR):
        os.makedirs(DOWNLOAD_TMP_DIR)
    try:
        download_file("https://paddleocr.bj.bcebos.com/PP-OCRv3/chinese/ch_PP-OCRv3_det_infer.tar",
                      "ch_PP-OCRv3_det_infer.tar")
        download_file("https://paddleocr.bj.bcebos.com/PP-OCRv3/chinese/ch_PP-OCRv3_rec_infer.tar",
                      "ch_PP-OCRv3_rec_infer.tar")
        extract(f"{DOWNLOAD_TMP_DIR}ch_PP-OCRv3_det_infer.tar",
                DOWNLOAD_TMP_DIR)
        extract(f"{DOWNLOAD_TMP_DIR}ch_PP-OCRv3_rec_infer.tar",
                DOWNLOAD_TMP_DIR)
    except DownloadError:
        raise DownloadError
    det_infer_folder = f"{DOWNLOAD_TMP_DIR}ch_PP-OCRv3_det_infer/"
    rec_infer_folder = f"{DOWNLOAD_TMP_DIR}ch_PP-OCRv3_rec_infer/"
    inference_model_to_serving(dirname=det_infer_folder,
                               model_filename="inference.pdmodel",
                               params_filename="inference.pdiparams",
                               serving_server=f"{MODEL_DIR}ppocr_det_v3_serving",
                               serving_client=f"{MODEL_DIR}ppocr_det_v3_client"
                               )
    inference_model_to_serving(dirname=rec_infer_folder,
                               model_filename="inference.pdmodel",
                               params_filename="inference.pdiparams",
                               serving_server=f"{MODEL_DIR}ppocr_rec_v3_serving",
                               serving_client=f"{MODEL_DIR}ppocr_rec_v3_client")
