import os
import pathlib
from utils import debug

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class DirectoryTree:
    @classmethod
    def generate(cls, root_dir, dir_only=False):
        _generator = _TreeGenerator(root_dir, dir_only)
        tree = _generator.build_tree()
        return tree


class _TreeGenerator:
    def __init__(self, root_dir, dir_only=False):
        self._root_dir = pathlib.Path(root_dir)
        self._dir_only = dir_only
        self._tree = []

    def build_tree(self):
        debug(
            f"""====== DEBUG =======
              build_tree
                TREE = {self._tree}"""
        )
        self._tree_head()
        debug(
            f"""_tree_head
                TREE = {self._tree}"""
        )
        self._tree_body(self._root_dir)
        debug(
            f"""_tree_body
                TREE = {self._tree}"""
        )
        return self._tree

    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)

    def _tree_body(self, directory, prefix=""):
        entries = self._prepare_entries(directory)
        entries_count = len(entries)
        debug(f"""======== _tree_body ==========
              entries = {entries}
              entries_count = {entries_count}""")
        for index, entry in enumerate(entries):
            connector = ELBOW if index == entries_count - 1 else TEE
            debug(f"""   for {enumerate(entries)}
                    index = {index}
                    entry = {entry}
                    conector = {connector}""")
            if entry.is_dir():
                self._add_directory(entry, index, entries_count, prefix, connector)
                debug("IS DIR")
            else:
                self._add_file(entry, prefix, connector)
                debug("IS FILE")


    def _prepare_entries(self, directory):
        entries = directory.iterdir()
        if self._dir_only:
            entries = [entry for entry in entries if entry.is_dir()]
            return entries
        entries = sorted(entries, key=lambda entry: entry.is_file())
        return entries

    def _add_directory(self, directory, index, entries_count, prefix, connector):
        self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}")
        if index != entries_count - 1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        self._tree_body(
            directory=directory,
            prefix=prefix,
        )
        self._tree.append(prefix.rstrip())

    def _add_file(self, file, prefix, connector):
        self._tree.append(f"{prefix}{connector} {file.name}")