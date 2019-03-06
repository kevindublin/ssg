# import modules from utilities
import utils
import sys

utils.main()


def main():

    print("This is argv:", sys.argv)
    command = sys.argv[1]
    print(command)
    if command == "build":
        print("Build was specified")
        print("Building pages...")
        utils.main()
    elif command == "new":
        print("New page was specified")
        new_page = input('new page name >')
        new_page = new_page.lower()
        if new_page.isalnum() is False:
            main()
        print("Building new page...")
        new_file = 'content/'+new_page+'.html'
        open(new_file, 'w+').write(
            '''
                <h3>New Page</h3>
                <br />
                <img src="img/vin.jpg" class="img-photo"/>
                <br />
                 <p>
                    Insert new text.
                 </p>
                 <br />
                 <ul class="list-unstyled"
                    <li><a href="mailto:vin@kevindublin.com">
                    <button type="button" class="btn btn-dark btn-block">Contact
                    </button></a></li>
                    <li><a href="resume.pdf">
                    <button type="button" class="btn btn-dark btn-block">Resume
                    </button></a></li>
                </ul>
            </div>
        '''
        )
        utils.main()
    else:
        print("Please specify ’build’ or ’new’")


if __name__ == '__main__':
    main()
