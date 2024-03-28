from enum import Enum


class LatexPlacement(Enum):
    fixed = "!h"
    floating = None


class Formatter:
    def document_class(dc: str) -> str:
        template = "\\documentclass{{{}}}\n"
        return template.format(dc)

    def packages(pkgs: list[str]) -> str:
        return "".join([Formatter.package(pkg) for pkg in pkgs])

    def package(pkg: str) -> str:
        template = "\\usepackage{{{}}}\n"
        return template.format(pkg)

    def paragraph(content: str) -> str:
        template = "{} \\par"
        return template.format(content)

    def command(command: str, arg: str) -> str:
        template = "\\{0}{{{1}}}\n"
        return template.format(command, arg)

    def body(content: str) -> str:
        return Formatter.env("document", separate=False)(content)

    def env(env_name: str, separate: bool = True):
        template = "\\begin{{{0}}}{3}{2}\n{1}\n\\end{{{0}}}"

        if separate:
            template = "\n{}\n".format(template)

        def apply_env(data: str, args: str | None = None, opts: str | None = None):
            fmt_args = "" if args is None else "{{{}}}".format(args)
            fmt_opts = "" if opts is None else "[{}]".format(opts)
            return template.format(env_name, Formatter.with_indent(data), fmt_args, fmt_opts)

        return apply_env

    def with_indent(src: str) -> str:
        return "\n".join(["\t{}".format(line) for line in src.split("\n")]).rstrip('\n')
