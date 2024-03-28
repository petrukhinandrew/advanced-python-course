from __future__ import annotations
from .gen_utils import Formatter, LatexPlacement


class LatexImage:
    def __init__(self) -> None:
        self.__caption = None
        self.__path = None
        self.__placement = LatexPlacement.floating

    def fixed() -> LatexImage:
        inst = LatexImage()
        inst.__placement = LatexPlacement.fixed
        return inst

    def floating() -> LatexImage:
        return LatexImage()

    def with_caption(self, caption: str) -> LatexImage:
        self.__caption = caption
        return self

    def from_path(self, path: str) -> LatexImage:
        self.__path = path
        return self

    def __str__(self) -> str:
        assert self.__path != None
        content = Formatter.command("includegraphics", self.__path)
        if self.__caption != None:
            content += Formatter.command("caption", self.__caption)
        return Formatter.env("figure")(content, opts=self.__placement.value)
