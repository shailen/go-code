import logging
import re
import urllib2

REGEX_IMPORT = 'IMPORT\(\s*\'(.*)\'\s*,\s*\'(.*)\'\s*\)'


class ImportFunction:
    def __init__(self, file_path, tag_name, is_code_snippet=True):
        self.file_path = file_path
        self.tag_name = tag_name
        self.is_code_snippet = is_code_snippet

    def extract_tagged_lines(self):
        contents = self.__get_file_contents()
        regex_string = 'BEGIN\(%s\)[^\n]*\n(.*)END\(%s\)[^\n]*\n' % (self.tag_name, self.tag_name)
        extracted = re.search(regex_string, contents, re.MULTILINE | re.DOTALL)
        if extracted:
            # Remove the last line including END tag
            lastline_stripped = ImportFunction.__remove_lastline_from_string(extracted.group(1))
            if self.is_code_snippet:
                return ImportFunction.__make_code_snippet(lastline_stripped)
            else:
                return lastline_stripped
        else:
            logging.warning('Tagged lines are not found. Path %s, Tag %s' % (self.file_path, self.tag_name))

    def __get_file_contents(self):
        if self.file_path.startswith('https:') or self.file_path.startswith('http:'):
            return urllib2.urlopen(self.file_path).read()
        else:
            with open(self.file_path, 'r') as f:
                return f.read()

    @staticmethod
    def __make_code_snippet(contents):
        result = ''
        for l in contents.split('\n'):
            result += '    ' + l + '\n'
        return result

    @staticmethod
    def __remove_lastline_from_string(s):
        return s[:s.rfind('\n')]


def replace_import(file_name):
    if _includes_import(file_name):
        with open(file_name, 'r') as read_file:
            with open(file_name.replace('.md', '') + '_parsed.md', 'w') as write_file:
                for line in read_file.readlines():
                    import_in_line = re.search(REGEX_IMPORT, line)
                    if import_in_line:
                        import_function = ImportFunction(import_in_line.group(1), import_in_line.group(2))
                        extracted = import_function.extract_tagged_lines()
                        write_file.write(extracted)
                    else:
                        write_file.write(line)


def _includes_import(file_name):
    with open(file_name, 'r') as f:
        matched_imports = re.search(REGEX_IMPORT, f.read())
        return matched_imports is not None


if __name__ == '__main__':
    replace_import('codelab.md')
