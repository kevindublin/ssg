#main function which pulls the index of pages and titles, then sends to the write function
def main():

    pages = site_index()

    for page in pages:
        page_src = page['source']
        page_output = page['output']
        page_title = page['title']
        if page_title == 'index':
            page_title = 'Vin Dublin | Full Stack Developer'
            pass
        write(page_src, page_output, page_title)
        pass

    print('...Completed Writing Pages!');
    pass

#write function which converts the template and content to strings and combines the pages
def write(page_src='content/index.html', page_output='docs/index.html', page_title='Vin Dublin | Full Stack Developer'):

    from jinja2 import Template

    page_content = open(page_src).read()
    template_html = open("template/base.html").read()
    template = Template(template_html)
    rendered_page = template.render(
    page_title = page_title,
    body_content = page_content,
    )
    open(page_output, 'w+').write(rendered_page)
    pass

#creates a list with dictionaries for the locations and titles of pages
def site_index():

    pages = []

    import  glob
    import  os
    source_files = glob.glob("content/*.html")

    for source in source_files:
        file_name = os.path.basename(source)
        name, extension = os.path.splitext(file_name)
        output_dir = source.replace('content/', 'docs/')
        pages.append({
        "source" : source,
        "output" : output_dir,
        "title" : name,
        })
        pass

    return pages
    pass



if __name__ == "__main__":
    main()
