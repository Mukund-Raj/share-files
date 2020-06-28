from app import flask_app
from urllib.parse import unquote,quote,urlparse
from flask import request,send_file,render_template,jsonify,Response,make_response,session,url_for,redirect
from io import BytesIO
import os
import threading
from app.config import Getdrives
import pathlib
from time import sleep
from json import dump,load
import mimetypes 
import posixpath
from app import config_file_path,ip_file_path
from shutil import make_archive
from secrets import token_urlsafe

my_password = '12345cruise#56@'


supported_mimetypes=['.jpg','.png','.mp4','.txt','.mp3','.avi','.py','.c','.cpp'] 
mimetypes.init()


#opening config file getting drive to which file should be saved
cfgfile = open(config_file_path,'r')

cfg = load(cfgfile)
savepath=cfg['drive']+':\\'+cfg['dfolder']+'\\'

@flask_app.route('/getEntry',methods=['GET','POST'])
def get_entry():
    if request.method == 'POST':
        if request.form:
            password = request.form.get('password').strip()
            if password == my_password:
                session['id'] = token_urlsafe(32)
                return redirect(url_for('index'))
            else:
                return "Wrong Password",200
    return render_template('entry.html')

@flask_app.route('/dtest')
def downloadtest():
    return render_template('dtest.html')

@flask_app.route('/')
def index():
    return render_template('index.html')

count = 100

def get_me_all_images():    
    path=os.path.normpath('E:\\')
    if os.path.exists(path):
        print('path exists')
    image_links =[]

    allpath = os.walk(path)

    count = 100
    i=0

    for single_path in allpath: 
        dirname,subdir,files = single_path
        #print(p)
        for file in files:
            filename = os.path.join(dirname,file)
            if os.path.isfile(filename):
                if os.path.getsize(filename) > 1024100:
                    ext=posixpath.splitext(filename)[1]
                    if ext in ['.png','.jpeg','.jpg']:
                        #converting os path to url path
                        #image_url = pathlib.Path(filename).as_posix()
                        filename = quote(filename)
                        image_url = f"get?file={filename}"
                        image_links.append(image_url)
                        i +=1
                        if i > count:
                            break

                        print(i)
        if i > count:
            break
    return image_links

@flask_app.route('/images')
def only_images():
    all_image_links=get_me_all_images()
    #print(all_image_links)
    return render_template('gimage.html',image_links = all_image_links)



'''
#return send_file(filename,as_attachment=True)
@flask_app.route('/decision',methods=['GET','POST'])
def showORdownload():
    if request.method=='POST':
        if request.is_json:
            file_choice = request.get_json()
            filename = urllib.parse.urlparse(file_choice['link']).query.split('=')[-1]
            filename = urllib.parse.unquote(filename)
            filename = os.path.normpath(filename)

            #print(file_choice['link'])
            if file_choice['option']:
                #print("user wants to download")
                #getting the filename from the link
                return send_file(filename, as_attachment = True)
            else:
                #print("user wants to see")
                return send_file(filename, as_attachment = False)
            #print(request.get_json())

    return "ok",200
'''

drives = Getdrives()
@flask_app.route('/get')
def send_from_computer():
    if session:
        links=[]
        if request.args:
            #print('working')
            #print(request.args)
            filename = request.args['file']

            #different links for downloading and viewing the file and openng the dirs
            filename=os.path.normpath(filename)
            #print(filename)
            if os.path.isdir(filename):
                if os.path.exists(filename):
                    dirc=os.listdir(filename)
                    for content in dirc:
                        #the actual link used in the directory
                        link=filename + '\\' +quote(content,errors='surrogatepass')     
                        
                        #for python to check for the directory
                        dir_link = filename+'\\'+content
                        #print(link)
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
                            base,ext=posixpath.splitext(content)
                            
                            #base is the only the filename so that if the filename is big then we can see the 
                            #extension of the file
                            single_content['content']=base
                            single_content['ext']= ext
                            #print(content)
                            single_content['fullname'] = content
                            #print(single_content['fullname'])
                            #fullname of the file for downloading
                            if ext.lower() in supported_mimetypes:
                                #print(ext)
                                single_content['option']=2
                            else:
                                single_content['option']=1
                        links.append(single_content)
                        
                
                    return render_template('desktop_access.html',links = links,all_drives=drives)

            if os.path.isfile(filename):
                nameOfFile = str(filename).split('\\')[-1]
                base,ext=posixpath.splitext(nameOfFile)
                return send_file(filename)
        return render_template('desktop_access.html',links = links,all_drives=drives)
    else:
        return redirect(url_for('get_entry'))

@flask_app.route('/folder/get')
def download_folder_as_zip():
    if session:
            
        print('folder name is ',request.args.get('file'))
        requested_folder_path = os.path.normpath(request.args.get('file').strip())
        
        if os.path.exists(requested_folder_path):
            if os.path.isdir(requested_folder_path):
                print('yes its a directory ',requested_folder_path)
                #the folder name to be zipped with
                zip_file_name = os.path.split(requested_folder_path)[1] + '_zip'
                if os.path.exists(zip_file_name):
                    os.remove(zip_file_name)
                #actual zipping of file
                #it returns the path where the zip file being saved
                where_my_zip_file = make_archive(zip_file_name,'zip',requested_folder_path)


                try:
                    f = open(where_my_zip_file,'rb')
                    bytes_data = BytesIO(f.read())
                    #first read zip file data in binary mode
                    f.close()
                    #after reading the zip file data remove the file 
                    #because we are using with it should remove the file contents too after send file
                    os.remove(where_my_zip_file)

                    #first check whether the file exist
                    if(os.path.exists(where_my_zip_file)):
                        print("zip file is deleted")
                    #after we send the file we will delete it
                    return send_file(bytes_data,as_attachment=True,attachment_filename=zip_file_name,mimetype='application/zip')

                except Exception as e:
                    reponse = make_response("File can't be zipped ",e)
                    return reponse
                
    else:
        return redirect(url_for('get_entry'))

@flask_app.route('/upload')
def receive_the_files():
    if session:
        return render_template('fileupload.html',file_save_path = savepath)
    else:
        return redirect(url_for('get_entry'))

@flask_app.route('/file_dest')
def handle_file_destination():
    #to be implemented
    pass
    #return render_template('fileupload.html')

#function that will use to save the file
def save_file(file_to_save):
    file_to_save.save(os.path.join(savepath,file_to_save.filename))
    print(file_to_save.filename," saved")



#called when files received from the user
@flask_app.route('/receivedata',methods=['POST'])
def receive_data():
    if session:
        if not os.path.exists(savepath):
            os.mkdir(savepath)
        #print("working")
        duplicate = []
        if request.method == 'POST':

            #print("working")
            if request.files:
                files = request.files.getlist('file1')
                #total count of files
                #now we will spawn files
                
                total_no_of_files = len(files)             

                for f in files:
                    if  not os.path.exists(os.path.join(savepath,f.filename)):
                        save_file(f)
                    else:
                        print(f.filename,"is duplicate")
                        duplicate.append(f.filename)

                if len(duplicate)==1:
                    return jsonify({"files":duplicate}),200
                else:
                    return "files submitted",200

            return "bad",304
    else:
        return redirect(url_for('get_entry'))