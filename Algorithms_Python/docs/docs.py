import ast
import os


def remove_title(docstring):
    docstring = docstring[docstring.find('\n') + len('\n'):]
    docstring = docstring[docstring.find('\n') + len('\n'):]
    return docstring


def parse_params(docstring, output):
    docstring = remove_title(docstring)
    output.append('<ul>')
    for entry in docstring.strip().split('\n\n'):
        print(entry)
        param_name = entry.split(':')[0].strip()
        param_type = entry.split('\n')[0].split(':')[1].strip()
        param_desc = ' '.join(entry.split('\n    ')[1:])
        output.append(f'<li> <strong>{param_name}</strong>: ' +
                      f'<em>{param_type}</em> <br>')
        output.append(f'&nbsp;&nbsp;&nbsp;&nbsp;{param_desc} <br></li>')
    output.append('</ul>')


def parse_funcs(docstring, output):
    docstring = remove_title(docstring)
    output.append('<ul>')
    for entry in docstring.strip().split('\n\n'):
        end_of_func_title = entry.find('\n', entry.find('->'))
        func_title = entry[:end_of_func_title]\
            .replace('    ', ' ') if end_of_func_title != -1 else entry
        func_name = func_title[:entry.find('(')]
        try:
            func_desc = entry[end_of_func_title:] \
                if end_of_func_title != -1 else ''
        except Exception:
            func_desc = ''
        if 'Setter' in func_desc or 'Property' in func_desc:
            continue
        output.append(f"<li> <a href='#function-{func_name}'><code>")
        output.append(f'{func_title}')
        if func_desc == '':
            output.append('</code></a> <br> </li>')
        else:
            output.append('</code></a> <br>')
            output.append('&nbsp;&nbsp;&nbsp;&nbsp;')
            output.append(f'{func_desc}')
            output.append('<br></li>')
    output.append('</ul>\n')


def parse_returns(docstring, output):
    docstring = remove_title(docstring)
    return_type = docstring.split('\n')[0]
    return_desc = ' '.join(docstring.split('\n')[1:]).replace('    ', '')
    output.append(f'<em>{return_type}</em> <br>')
    output.append(f'&nbsp;&nbsp;&nbsp;&nbsp;{return_desc} <br>')


def parse_raises(docstring, output):
    docstring = remove_title(docstring)
    error_type = docstring.split('\n')[0]
    error_desc = ' '.join(docstring.split('\n')[1:]).replace('    ', '')
    output.append(f'<strong>{error_type}</strong> <br>')
    output.append(f'&nbsp;&nbsp;&nbsp;&nbsp;{error_desc} <br>')


def parse_classes(docstring, output):
    docstring = remove_title(docstring)
    output.append('<ul>')
    for entry in docstring.strip().split('\n\n'):
        class_title = entry.split('\n')[0]
        class_params_start = class_title.find('(')
        if class_params_start == -1:
            class_name = class_title
        else:
            class_name = class_title[:class_params_start]
        try:
            class_desc = ''.join(entry.split('\n')[1:])
        except Exception:
            class_desc = ''
        output.append(f"<li> <a href='#class-{class_name}'><code>")
        output.append(f'{class_title}')
        if class_desc == '':
            output.append('</code></a> <br> </li>')
        else:
            output.append('</code></a> <br>')
            output.append('&nbsp;&nbsp;&nbsp;&nbsp;')
            output.append(f'{class_desc}')
            output.append('<br></li>')
    output.append('</ul>')


parsing_funcs = {'Constants': parse_params,
                 'Attributes': parse_params,
                 'Parameters': parse_params,
                 'Returns': parse_returns,
                 'Yields': parse_returns,
                 'Raises': parse_raises,
                 'Functions': parse_funcs,
                 'Methods': parse_funcs,
                 'Classes': parse_classes}


def parse_module_doc(module_doc, output):
    module_name = module_doc.split('\n')[0]
    output.append(f'<h1>{module_name}</h1>')
    present_sections = {module_doc.find(i): i
                        for i in ['Constants', 'Functions', 'Classes']}
    positions = sorted([i for i in present_sections.keys()])
    section_positions = [i for i in positions if i != -1]
    if len(section_positions) == 0:
        output.append(' '.join(module_doc.split('\n')[1:]))
        output.append('---')
        return
    module_desc = module_doc[module_doc.find('\n',
                                             module_doc.find('\n') + 1):min(
                                    section_positions)]
    output.append(' '.join(module_desc.split('\n')))
    for position, section in present_sections.items():
        # the section is not present
        if position == -1:
            continue
        output.append(f'<h2>{section}</h2>')
        # the section is the last
        if position == max(positions):
            parsing_funcs[section](module_doc[position:], output)
        else:
            parsing_funcs[section](
                # isolate and parse the piece of module_doc from the start
                # of the current section (position) to the end of it
                # (positions[positions.index(position) + 1])
                module_doc[position:positions[positions.index(position) + 1]],
                output)
    output.append('---')


def parse_func_doc(node, output):

    docstring = ast.get_docstring(node)
    if docstring is None:
        return

    output.append(
        '<div style="page-break-after: always; visibility: hidden">' +
        '</div>')
    output.append('<br>')
    output.append(f'<h1 id="function-{node.name}">')
    print(node.name)
    output.append('<strong>Function</strong>')
    output.append(f'<code>{node.name}</code></h1>')

    present_sections = {docstring.find(i): i
                        for i in ['Parameters', 'Returns',
                                  'Raises', 'Yields']}
    positions = sorted([i for i in present_sections.keys()])
    section_positions = [i for i in positions if i != -1]
    if len(section_positions) == 0:
        output.append(docstring)
        output.append('\n---')
        return
    func_desc = docstring[:min(section_positions)]
    output.append(func_desc)
    for position, section in present_sections.items():
        # the section is not present
        if position == -1:
            continue
        output.append(f'<h2>{section}</h2>')
        # the section is the last
        if position == max(positions):
            parsing_funcs[section](docstring[position:], output)
        else:
            parsing_funcs[section](
                # isolate and parse the piece of module_doc from the start
                # of the current section (position) to the end of it
                # (positions[positions.index(position) + 1])
                docstring[position:positions[positions.index(position) + 1]],
                output)
    output.append('\n---')


def parse_class_doc(node, output):

    docstring = ast.get_docstring(node)
    if docstring is None:
        return

    output.append(
        '<div style="page-break-after: always; visibility: hidden">' +
        '</div>')
    output.append('<br>')
    output.append(f'<h1 id="class-{node.name}">')
    print(node.name)
    output.append('<strong>Class</strong>')
    output.append(f'<code>{node.name}</code></h1>')

    present_sections = {docstring.find(i): i
                        for i in ['Attributes', 'Methods']}
    positions = sorted([i for i in present_sections.keys()])
    section_positions = [i for i in positions if i != -1]
    if len(section_positions) == 0:
        output.append(docstring)
        output.append('\n---')
        return
    func_desc = docstring[:min(section_positions)]
    output.append(func_desc)
    for position, section in present_sections.items():
        # the section is not present
        if position == -1:
            continue
        output.append(f'<h2>{section}</h2>')
        # the section is the last
        if position == max(positions):
            parsing_funcs[section](docstring[position:], output)
        else:
            parsing_funcs[section](
                # isolate and parse the piece of module_doc from the start
                # of the current section (position) to the end of it
                # (positions[positions.index(position) + 1])
                docstring[position:positions[positions.index(position) + 1]],
                output)
    output.append('\n---')

    for nr, node in enumerate(ast.iter_child_nodes(node)):
        if nr == 0 or not (isinstance(node, ast.FunctionDef) or
                           isinstance(node, ast.ClassDef)):
            continue
        if isinstance(node, ast.FunctionDef):
            parse_func_doc(node, output)


def parse_docstrings(file_docstrings, output_file):
    tree = ast.parse(file_docstrings)
    output = []
    module_doc = ast.get_docstring(tree)
    if module_doc is None:
        return
    parse_module_doc(module_doc, output)
    for nr, node in enumerate(ast.iter_child_nodes(tree)):
        if nr == 0 or not (isinstance(node, ast.FunctionDef) or
                           isinstance(node, ast.ClassDef)):
            continue
        if isinstance(node, ast.FunctionDef):
            parse_func_doc(node, output)
        if isinstance(node, ast.ClassDef):
            parse_class_doc(node, output)
    with open(output_file, 'w') as out:
        out.write('\n'.join(output))


exclude_patterns = ['__init__', 'tests', 'docs', '__pycache__', 'venv']
open('Table_of_contents.md', 'w').close()


for root, dirs, files in os.walk('../'):
    for name in files:
        if '.py' in name and not any([(i in root or i in name)
                                      for i in exclude_patterns]):
            file = open(os.path.join(root, name), 'r')
            print(f'Currently parsing {name}')
            parse_docstrings(file.read(), f'{name[:-3]}.md')
            print('Success')
            # __init__.py parsing
        if name == '__init__.py':
            if any([i in root for i in exclude_patterns]):
                continue
            print(os.path.join(root, name))
            file = open(os.path.join(root, name), 'r').read()
            docstring = ast.get_docstring(ast.parse(file))
            if docstring is None:
                continue
            out = open('Table_of_contents.md', 'a')
            out.write(docstring + '\n')
            out.close()
