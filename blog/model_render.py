# coding=utf-8
import mistune


class PostRender(mistune.Renderer):
    @classmethod
    def parse(cls, text):
        renderer = cls()
        md = mistune.Markdown(renderer=renderer)
        return md.render(text)
