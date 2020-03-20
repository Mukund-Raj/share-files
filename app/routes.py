from app import flask_app
import urllib
from flask import request,send_file,render_template
import os
import mimetypes
import posixpath

supported_mimetypes=['.jpg','.png','.mp4']
mimetypes.init()



@flask_app.route('/')
def index():
    return render_template('index.html')

@flask_app.route('/images')
def only_images():
    return render_template('only_images.html')

#return send_file(filename,as_attachment=True)

@flask_app.route('/get')
def send_from_computer():
    
    links={}
    if request.args:
        print('working')
        print(request.args)
        filename = request.args['file']

        print(filename)
        #different links for downloading and viewing the file and openng the dirs

        if os.path.isdir(filename):
            if os.path.exists(filename):
                dirc=os.listdir(filename)
                for content in dirc:
                    
                    link=filename + "\\" +urllib.parse.quote(content,errors='surrogatepass')     

                    href=f"get?file={link}"
                    
                    if os.path.isdir(link):
                        #links.append(f"<a href='get?file={link}'><p>{content}\\</p></a>")
                        links[href]=content+"/"
                    
                    else:
                        #links.append(f"<a href='get?file={link}'><p>{content}\\</p></a>")
                        links[href]=content
            
                #print()
                #print(type(links))
                #print(links)
                return render_template('desktop_access.html',links = links)
                #print(os.listdir(filename))
                #return ('<br>').join(links),200 #f"{filename} is a directory",200
        
        if os.path.isfile(filename):
            nameOfFile = str(filename).split('\\')[-1]
            base,ext=posixpath.splitext(nameOfFile)
            print("base ",base)
            if ext is '.mp4':
                #return send_file(filename, as_attachment = True)
                return render_template('video_player.html',fileName=filename)
                #print(mimetypes.types_map[ext])
            else:
            #print(nameOfFile)
                return send_file(filename, as_attachment = False,attachment_filename = nameOfFile)
            #return f"{filename} is a file",200
        
    return render_template('desktop_access.html',links = links)
    
    #return "<a href='get?file=E:\'>E:\</a>",200
    
    """
    return '''<a href='send?file=E:\Ball in  a cup-32Bit\Ball in a cup.exe'>Ball in cup.exe</a><br>
    <a href='send?file=E:\Ball In A Cup 32 Bit Last update\Ball in a cup 32 Bit.zip'>Ball in cup last update.exe</a>
    <br>
    """
    
@flask_app.route('/upload')
def receive_the_files():
    return render_template('fileupload.html')

@flask_app.route('/file_dest')
def handle_file_destination():
    pass
    #return render_template('fileupload.html')



@flask_app.route('/receivedata',methods=['POST'])
def receive_data():
    if not os.path.exists('E:\\1 Shared files\\'):
        os.mkdir('E:\\1 Shared files\\')
    print("working")
    if request.method == 'POST':
        print("working")
        if request.files:
            files = request.files.getlist('file1')
           
           
            for f in files: 
                f.save(os.path.join('E:\\1 Shared files\\',f.filename))
                print(f.filename," saved")
            return "got your file",200

        return "bad",304