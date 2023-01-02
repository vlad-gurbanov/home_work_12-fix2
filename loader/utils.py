def save_picture(picture):
    filename = picture.filename
    file_type = filename.split('.')[-1]

    if file_type not in ('jpg', 'jpeg', 'png', 'svg', 'bmp'):
        return

    picture.save(f'./uploads/{filename}')
    return f'uploads/{filename}'
