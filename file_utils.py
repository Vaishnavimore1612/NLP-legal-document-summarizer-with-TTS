import zipfile
import os

def create_zip(text_content, audio_path=None, out_zip="result_package.zip"):
    with zipfile.ZipFile(out_zip, 'w') as zipf:
        txt_file = "result.txt"
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(text_content)
        zipf.write(txt_file)
        os.remove(txt_file)

        if audio_path and os.path.exists(audio_path):
            zipf.write(audio_path, os.path.basename(audio_path))
    
    return out_zip
