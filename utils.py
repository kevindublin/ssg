# pulls site map of pages and titles, then sends to the write function
def main():

    pages = site_map()
    for page in pages:
        page_src = page['source']
        page_output = page['output']
        page_title = page['title']
        if page_title == 'index':
            page_title = 'Vin Dublin | Full Stack Developer'

        write(pages, page_src, page_output, page_title)
    print('...Completed Writing Pages!')
    pass

# converts the template and content to strings and combine pages


def write(pages, page_src='', page_output='', page_title=''):

    from jinja2 import Template

    page_content = open(page_src).read()
    template_html = open("template/base.html").read()
    template = Template(template_html)
    rendered_page = template.render(

        page_title=page_title,
        body_content=page_content,
        pages=pages,
        page_output=page_output

    )
    open(page_output, 'w+').write(rendered_page)


# creates a list with dictionaries for the locations and titles of pages
def site_map():

    pages = []

    import glob
    import os
    source_files = glob.glob("content/*.html")

    for source in source_files:
        file_name = os.path.basename(source)
        name, extension = os.path.splitext(file_name)
        output_dir = source.replace('content/', 'docs/')
        pages.append({

            "source": source,
            "output": output_dir,
            "title": name,

        })

    return pages
    pass


if __name__ == "__main__":
    main()
