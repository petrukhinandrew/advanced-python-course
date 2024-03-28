from __future__ import annotations
from .gen_utils import Formatter
from .table import LatexTable
from .image import LatexImage


class LatexDoc:
    def __init__(self, doc_class: str | None = None) -> None:
        self.__doc_class = doc_class
        self.__packages = []
        self.__body = ""

        self.__cur_env_stack = []
        self.__cur_arg_stack = []
        self.__cur_body_stack = []

    def article() -> LatexDoc:
        instance = LatexDoc("article")
        return instance

    def use_package(self, package: str) -> LatexDoc:
        self.__packages.append(package)
        return self

    def as_paragraph(self, text: str) -> LatexDoc:
        self.__cur_body_stack.append(Formatter.paragraph(text))
        return self

    def as_raw(self, text: str) -> LatexDoc:
        self.__cur_body_stack.append(text)
        return self

    def into_env(self, env_name) -> LatexDoc:
        self.__cur_env_stack.append(Formatter.env(env_name))
        self.__cur_arg_stack.append(None)
        return self

    def with_args(self, args: str) -> LatexDoc:
        self.__cur_arg_stack[-1] = args
        return self

    def as_table(self, table: LatexTable) -> LatexDoc:
        return self.as_raw(str(table))

    def as_image(self, image: LatexImage) -> LatexDoc:
        return self.as_raw(str(image))

    def insert_content(self) -> LatexDoc:
        content = "\n".join(self.__cur_body_stack)
        for (env, args) in zip(self.__cur_env_stack, self.__cur_arg_stack):
            content = env(content, args=args)
        self.__cur_body_stack.clear()
        self.__cur_env_stack.clear()
        self.__cur_arg_stack.clear()
        self.__body += content
        return self

    def __str__(self) -> str:
        assert self.__doc_class != None
        fmt_doc_class = Formatter.document_class(self.__doc_class)
        fmt_packages = Formatter.packages(self.__packages)
        fmt_body = Formatter.body(self.__body)
        return "\n".join([fmt_doc_class, fmt_packages, fmt_body])

    def save_as(self, path: str) -> None:
        assert path.endswith(".tex")
        with open(path, 'w') as output:
            output.write(str(self))
