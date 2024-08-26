# Variable global para el nombre del archivo
output_file = 'output.html'

def set_name_file(filename):
    """
    Establece el nombre del archivo de salida.
    
    :param filename: Nombre del archivo de salida.
    """
    global output_file
    output_file = filename

def estructura_html():
    """
    Crea la estructura básica de un archivo HTML.
    """
    with open(output_file, 'w') as file:
        file.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Etiqueta Generada</title>\n</head>\n<body>\n</body>\n</html>')

def generate_html_tag(tag, content, **attributes):
    """
    Genera una etiqueta HTML con el contenido y los atributos proporcionados.
    Agrega la etiqueta solo si no existe ya en el archivo.
    
    :param tag: Nombre de la etiqueta (por ejemplo, 'div', 'span').
    :param content: Contenido dentro de la etiqueta.
    :param attributes: Atributos opcionales como key-value pairs.
    :return: None
    """
    # Construir la cadena de atributos
    attr_str = ' '.join(f'{key}="{value}"' for key, value in attributes.items())
    
    # Crear la etiqueta HTML
    if attr_str:
        html_tag = f'<{tag} {attr_str}>{content}</{tag}>'
    else:
        html_tag = f'<{tag}>{content}</{tag}>'
    
    # Leer el contenido actual del archivo HTML si existe
    try:
        with open(output_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        # Si el archivo no existe, creamos una estructura básica de HTML
        lines = ['<!DOCTYPE html>\n', '<html>\n', '<head>\n', '<title>Etiqueta Generada</title>\n', '</head>\n', '<body>\n', '</body>\n', '</html>']
    
    # Verificar si la etiqueta ya está presente
    tag_exists = any(html_tag in line for line in lines)
    
    # Si la etiqueta no existe, insertarla antes de la etiqueta de cierre </body>
    if not tag_exists:
        for i, line in enumerate(lines):
            if line.strip() == '</body>':
                lines.insert(i, html_tag + '\n')
                break
    
    # Escribir el contenido actualizado en el archivo HTML
    with open(output_file, 'w') as file:
        file.writelines(lines)

def add_html_title(title):
    """
    Agrega una etiqueta <title> al archivo HTML.
    
    :param title: Contenido de la etiqueta <title>.
    :return: None
    """
    # Leer el contenido actual del archivo HTML si existe
    try:
        with open(output_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        # Si el archivo no existe, creamos una estructura básica de HTML
        lines = ['<!DOCTYPE html>\n', '<html>\n', '<head>\n', '</head>\n', '<body>\n', '</body>\n', '</html>']
    
    # Buscar e insertar la etiqueta <title> en la sección <head>
    title_exists = False
    for i, line in enumerate(lines):
        if line.strip() == '</head>':
            if not title_exists:
                lines.insert(i, f'<title>{title}</title>\n')
                break
        elif '<title>' in line:
            # Si ya hay una etiqueta <title>, reemplazar su contenido
            lines[i] = f'<title>{title}</title>\n'
            title_exists = True
    
    # Escribir el contenido actualizado en el archivo HTML
    with open(output_file, 'w') as file:
        file.writelines(lines)
