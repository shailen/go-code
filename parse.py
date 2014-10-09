"""
Script to parse the contents of a codelab into JSON.
"""

import logging
import os

import re
import yaml
import requests


logging.basicConfig(level=logging.INFO)

base_dir_path = 'repos'
doc_file = 'doc.md'
metadata_file = 'metadata.yaml'


data = {base_dir_path: {}}

IMPORT_REGEXP = re.compile(r"IMPORT\('(\S+?)',\s*'(\w+?)'\)")

comment_chars_map = {
  '.dart': '//',
  '.py': '#',
  '.html': '<!--'
}

"""Reads the contents of the markdown file."""
def read_md_file(dirpath, filename):
    file_path = os.path.join(dirpath, filename)
    data[base_dir_path][os.path.basename(dirpath)] = {}
    with open(file_path) as fh:
        md = fh.read()
    return md


"""Returns a list of IMPORTs in a markdown file. Each entry in the list is
itself a two-item list, where the first item is the import path and second item
is the name of the import tag."""
def extract_import_tags(text):
    tags = []
    matches = re.finditer(IMPORT_REGEXP, text)
    for match in matches:
        tags.append([match.group(1), match.group(2)])
    return tags


"""Makes a request to GitHub to get the file used in an IMPORT."""
def fetch_import_code(path):
    # TODO(shailen): add some error handling code.
    return requests.get(path).content


"""Generates the string used in the regexp for getting the contents between
BEGIN() and END() tags."""
def get_begin_end_regexp_string(path, tag):
    file_suffix = os.path.splitext(path)[1]
    comment_chars = comment_chars_map[file_suffix]
    # TODO(shailen): de-uglify this. Seriously.
    return r"%s\s*?BEGIN\(%s\)([\s\S]+?)%s\s*?END\(%s\)" % (
        comment_chars, tag, comment_chars, tag)


"""Gets code snippet defined by an IMPORT and ensures four spaces of leading
whitespace required by markdown."""
def get_code_snippet(match):
    snippet = match.group(1)
    snippet_lines = snippet.split('\n')
    for line in snippet_lines:
      if line.strip():
        # Get leading whitspace.
        lspace_len = len(line) - len(line.lstrip())
        break
    space = ' '
    return '\n'.join(
        ["%s%s" % (space * 4, line[lspace_len:]) for line in snippet_lines]
    )


"""Reads content of a markdown file, substituting IMPORTS with code
snippets, and returns the converted markdown."""
def process_md_file_with_imports(dirpath, filename):
    md = read_md_file(dirpath, filename)
    # Assuming for now that all IMPORT tags use urls.
    imports = extract_import_tags(md)

    for _import in imports:
        path, tag = _import
        code = fetch_import_code(path)
        matches = re.finditer(re.compile(
                get_begin_end_regexp_string(path, tag),
                re.MULTILINE), code)

        for match in matches:
            snippet = get_code_snippet(match)
            md = re.sub(re.compile(r"IMPORT\('%s', '%s'\)" %
              (path, tag)), snippet, md)
    return md


"""Generates the key, comprising of the org name and the repo name, used for
storing repo data as JSON."""
def get_org_and_repo(dirpath):
    repo = os.path.basename(dirpath)
    org = os.path.split(os.path.dirname(dirpath))[1]
    return os.path.join(org, repo)


"""Generates the metadata and code for a repo as JSON."""
def generate_data(base_dir_path):
  for dirpath, subdirs, filenames in os.walk(base_dir_path):
      for filename in filenames:
          if filename != doc_file:
              continue

          md = process_md_file_with_imports(dirpath, filename)
          for filename in os.listdir(dirpath):
              if filename != metadata_file:
                  continue

              with open(os.path.join(dirpath, metadata_file),
                      'r') as fh:
                  metadata = yaml.load(fh)

              key = get_org_and_repo(dirpath)
              data[base_dir_path][key] = metadata
              data[base_dir_path][key]['md'] = md
          print(data)

if __name__ == "__main__":
    generate_data(base_dir_path)
