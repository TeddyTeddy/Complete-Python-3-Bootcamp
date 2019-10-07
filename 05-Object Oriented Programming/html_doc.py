# https://www.htmlquick.com/tutorials/document-structure.html


class Tag(object):
    def __init__(self, name, contents):
        self.start_tag = f'<{name}>'
        self.end_tag = f'</{name}>'
        self.contents = contents

    def __str__(self):
        return f'{self.start_tag}{self.contents}{self.end_tag}'

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):
    def __init__(self):
        super().__init__(
            '!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"', '')
        self.end_tag = ''  # doctype doesnt have end tag


class Head(Tag):
    def __init__(self):
        super().__init__(name='HEAD', contents='')
        self._head_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._head_contents.append(new_tag)

    def display(self, file=None):
        self.contents = ''
        for tag in self._head_contents:
            self.contents += str(tag)
        super().display(file=file)


class Body(Tag):
    def __init__(self):
        super().__init__('BODY', '')  # body contents would be built up separately in _body_contents
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        self.contents = ''
        for tag in self._body_contents:
            self.contents += str(tag)
        super().display(file=file)


class HtmlDoc(object):
    def __init__(self, title_contents=''):
        self._doc_type = DocType()  # composition
        self._head = Head()  # composition
        self._head.add_tag(name='title', contents=title_contents)
        self._body = Body()  # composition

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)  # composition & delegation

    def display(self, file=None):  # polymorphism using composition and delegation
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    my_page = HtmlDoc(title_contents='Document title')
    my_page.add_tag('h1', 'main heading')
    my_page.add_tag('h2', 'sub-heading')
    my_page.add_tag('p', 'this is a paragraph')

    with open('main.html', 'w') as file:
        my_page.display(file=file)
    file.close()
