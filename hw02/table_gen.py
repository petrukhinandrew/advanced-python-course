from __future__ import annotations
from enum import Enum
from gen_utils import Formatter


class LatexTableAlignment(Enum):
    left = "\\raggedright\n"
    right = "\\raggedleft"
    center = "\\centering"


class LatexTablePlacement(Enum):
    fixed = "!h"
    floating = None


class LatexTableRowBorderPreset:
    def none(n, line, islast): return "{} \\\\ \n".format(line)

    def firstsingle(n, line, islast): return "{0} \\\\ {1}\n".format(
        line, "\n\\hline" if n == 0 else "")
    def firstdouble(n, line, islast): return "{0} \\\\ {1}\n".format(
        line, "\n\\hline \\hline" if n == 0 else "")

    def midsingle(n, line, islast): return "{} \\\\ {} \n".format(line, "\n\\hline \n" if not islast else "")

    def middouble(
        n, line, islast): return "{} \\\\ {} \n".format(line,"\n\\hline \\hline \n" if not islast else "")

    def allsingle(n, line, islast): return ("\\hline \n" if n ==
                                            0 else "") + "{} \\\\ \n\\hline \n".format(line)
    def alldouble(n, line, islast): return ("\\hline \\hline \n" if n ==
                                            0 else "") + "{} \\\\ \n\\hline \\hline \n".format(line)


class LatexTableColBorderPreset:
    def none(js): return " ".join(js)

    def midsingle(js): return "|".join(js)
    def middouble(js): return "||".join(js)

    def allsingle(js): return "|{}|".format("|".join(js))
    def alldouble(js): return "||{}||".format("||".join(js))

    def separatedfirstcol(js): return "{0}|{1}".format(js[0], " ".join(js[1:]))


class LatexTableJustificationPreset(Enum):
    def rightall(n): return ['r'] * n
    def leftall(n): return ['l'] * n
    def centerall(n): return ['c'] * n

    def leftfirstcenterrest(n): return ['l'] + ['c'] * (n - 1)


class LatexTable:
    def __init__(self, caption: str | None = None) -> None:
        self.alignment = LatexTableAlignment.left
        self.placement = LatexTablePlacement.floating
        self.caption = caption

        self.preset = [None, None, None]
        self.dataset = None

    def fixed(caption: str | None = None) -> LatexTable:
        instance = LatexTable(caption)
        instance.placement = LatexTablePlacement.fixed
        return instance

    def floating(caption: str | None = None) -> LatexTable:
        return LatexTable(caption)

    def aligned(self, alignment: LatexTableAlignment) -> LatexTable:
        self.alignment = alignment
        return self

    def with_caption(self, caption: str) -> LatexTable:
        self.caption = caption
        return self

    def with_col_preset(self, col_preset: LatexTableColBorderPreset):
        self.preset[0] = col_preset
        return self

    def with_row_preset(self, row_preset: LatexTableRowBorderPreset):
        self.preset[1] = row_preset
        return self

    def with_jus_preset(self, jus_preset):
        self.preset[2] = jus_preset
        return self

    def from_dataset(self, data: list[list[any]]) -> LatexTable:
        self.dataset = data
        return self

    def with_custom_spec(self, **kwargs) -> LatexTable:
        raise NotImplemented

    def merge_tabular(self, **kwargs) -> LatexTable:
        raise NotImplemented

    def from_dataline(self, line: list[any]) -> LatexTable:
        raise NotImplemented

    def __tabular_with_preset(ds: list[list[any]], preset: list[any]) -> str:
        def fill_ds_gaps(dirty: list[list[any]]) -> list[list[list[any]], int]:
            max_len = len(max(dirty, key=len))
            return [line + [" "] * (max_len - len(line)) for line in dirty], max_len

        def as_ltx_arr(arr: list[any]) -> str:
            return "& ".join([str(elem) for elem in arr])
        
        proper_ds, col_cnt = fill_ds_gaps(ds)
        row_cnt = len(proper_ds)
        
        fmt_tab_args = preset[0](preset[2](col_cnt))
        
        content = "".join([preset[1](n, as_ltx_arr(line), n == row_cnt)
                          for (n, line) in enumerate(proper_ds)]).rstrip("\n")
        return Formatter.env("tabular")(content, args=fmt_tab_args).rstrip("\n")

    def __str__(self) -> str:
        assert self.preset != [None, None, None]
        assert self.dataset != None
        content = self.alignment.value + \
            LatexTable.__tabular_with_preset(self.dataset, self.preset)
        if self.caption != None:
            content += Formatter.command("caption", self.caption)
        return Formatter.env("table")(content, opts=self.placement.value)
