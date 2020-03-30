from app import flask_app
import urllib.parse
from flask import request,send_file,render_template
import os
import json
import mimetypes 
import posixpath

supported_mimetypes=['.jpg','.png','.mp4','.txt','.mp3','.avi','.py','.c','.cpp'] 
mimetypes.init()

#opening config file getting drive to which file should be saved
cfgfile = open('app/config.json','r')
cfg = json.load(cfgfile)
savepath=cfg['drive']+':\\'+cfg['dfolder']+'\\'


@flask_app.route('/dtest')
def downloadtest():
    return render_template('dtest.html')

@flask_app.route('/')
def index():
    return render_template('index.html')

@flask_app.route('/images')
def only_images():
    return render_template('only_images.html')

#return send_file(filename,as_attachment=True)
@flask_app.route('/decision',methods=['GET','POST'])
def showORdownload():
    if request.method=='POST':
        if request.is_json:
            file_choice = request.get_json()
            filename = urllib.parse.urlparse(file_choice['link']).query.split('=')[-1]
            filename = urllib.parse.unquote(filename)
            filename = os.path.normpath(filename)

            print(file_choice['link'])
            if file_choice['option']:
                print("user wants to download")
                #getting the filename from the link
                return send_file(filename, as_attachment = True)
            else:
                print("user wants to see")
                return send_file(filename, as_attachment = False)
            #print(request.get_json())

    return "ok",200


@flask_app.route('/get')
def send_from_computer():
    
    links=[]
    if request.args:
        print('working')
        print(request.args)
        filename = request.args['file']

        #different links for downloading and viewing the file and openng the dirs
        filename=os.path.normpath(filename)
        print(filename)
        if os.path.isdir(filename):
            if os.path.exists(filename):
                dirc=os.listdir(filename)
                for content in dirc:
                    #the actual link used in the directory
                    link=filename + '\\' +urllib.parse.quote(content,errors='surrogatepass')     
                    
                    #for python to check for the directory
                    dir_link = filename+'\\'+content
                    print(link)
                    

                    href=f"get?file={link}"
                    single_content={}
                    if os.path.isdir(dir_link):
                        #links.append(f"<a href='get?file={link}'><p>{content}\\</p></a>")
                        #links[href]=content+"/"
                        single_content['href']=href
                        single_content['content']=content+"\\"
                    else:
                        #links.append(f"<a href='get?file={link}'><p>{content}\\</p></a>")
                        #links[href]=content
                        single_content['href']=href
                        single_content['content']=content
                        
                        base,ext=posixpath.splitext(content)
                        if ext.lower() in supported_mimetypes:
                            #print(ext)
                            single_content['option']=2
                        else:
                            single_content['option']=1
                    links.append(single_content)
                    
            
                #print()
                #print(type(links))
                #print(links)
                #for link in links:
                    #print(link)
                return render_template('desktop_access.html',links = links)
                #print(os.listdir(filename))
                #return ('<br>').join(links),200 #f"{filename} is a directory",200
        
        if os.path.isfile(filename):
            nameOfFile = str(filename).split('\\')[-1]
            base,ext=posixpath.splitext(nameOfFile)
            print("base ",base)
            print(ext)
            #if ext in supported_mimetypes:
                #return send_file(filename, as_attachment = True)
                #return send_file(filename, as_attachment = False,attachment_filename = nameOfFile)
                #render_template('video_player.html',fileName=filename)
                #print(mimetypes.types_map[ext])
            #else:
            #print(nameOfFile)
            return send_file(filename)
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
    #if not os.path.exists('E:\\1 Shared files\\'):
        #os.mkdir('E:\\1 Shared files\\')
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    print("working")
    if request.method == 'POST':
        print("working")
        if request.files:
            files = request.files.getlist('file1')
           
           
            for f in files: 
                f.save(os.path.join(savepath,f.filename))
                print(f.filename," saved")
            return "got your file",200

        return "bad",304