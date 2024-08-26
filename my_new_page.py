from site_creator.py_hmtl import generate_html_tag, add_html_title, estructura_html, set_name_file


# Ejemplo de uso
"""
    (function) def set_name_file(filename: Any) -> None
    Establece el nombre del archivo de salida.

    :param filename: Nombre del archivo de salida.
"""
set_name_file('output.html')


"""
    (function) def estructura_html() -> None
    Crea la estructura básica de un archivo HTML.
"""
estructura_html()


"""
    (function) def add_html_title(title: Any) -> None
    Agrega una etiqueta <title> al archivo HTML.

    :param title: Contenido de la etiqueta <title>.
    :return: None
"""
add_html_title('Nuevo Título de la Página')


"""
    (function) def generate_html_tag(
        tag: Any,
        content: Any,
        **attributes: Any
    ) -> None
    Genera una etiqueta HTML con el contenido y los atributos proporcionados. Agrega la etiqueta solo si no existe ya en el archivo.

    :param tag: Nombre de la etiqueta (por ejemplo, 'div', 'span').
    :param content: Contenido dentro de la etiqueta.
    :param attributes: Atributos opcionales como key-value pairs.
    :return: None
"""
generate_html_tag('p', 'Hola, mundo!', style='color: red;', id='greeting')
