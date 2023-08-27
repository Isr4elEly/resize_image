import os
import re
from PIL import Image

# cria a variável da nova largura
new_width = 0

def calc_new_height(width, height, new_width):
    return round(new_width * height / width)

def resize(root, file, new_width, new_img_name):
    original_img_path = os.path.join(root, file)
    new_img_path = os.path.join(root, new_img_name)

    pillow_img = Image.open(original_img_path)
    width, height = pillow_img.size

    if width > height:
        new_width = 1200
    else:
        new_width = 600

    # calcular a nova altura
    new_height = calc_new_height(width, height, new_width)

    #Redimensionando a imagem
    new_img = pillow_img.resize((new_width, new_height), Image.LANCZOS)
    new_img.save(
        new_img_path,
        optimize=True,
        quality=70,
        exif=pillow_img.info.get('exif')
    )

def is_image(extension: str):
    extension_lowercase = extension.lower()
    return bool(re.search(r'^\.(jpe?g|png)$',extension_lowercase))

def files_cheks(root, file):
    # separa o nome da extensão
    filename, extension = os.path.splitext(file)

    if not is_image(extension):
        return 
    
    flag = 'resized_'
    
    if flag in file:
        return

    new_img_name = flag + filename + extension

    resize(root=root, file=file, new_width=new_width, new_img_name = new_img_name)

def files_loop(root, files):
        for file in files:
            # verificar se o arquivo é imagens
            files_cheks(root, file)

def main(root_folder):
    # percorrer a pasta de imagens
    for root, dirs, files in os.walk(root_folder):
        files_loop(root, files)


if __name__ == '__main__':
    root_folder = './photo'
    main(root_folder)