    //returning us the object by id



function _(el){
    return document.getElementById(el);
}

function send_file()
{
    var file1=document.getElementById('file1');
    var total_size = 0;

    var time_reamin = 0;
    var previous_loaded_data = 0;
    var formdata=new FormData();
    for(var i=0;i<document.getElementById('file1').files.length;i++)
        {
            formdata.append("file1",file1.files[i]);
            total_size+=file1.files[i].size;
        }
    let xhr=new XMLHttpRequest();

    xhr.open('POST','/receivedata',true);


    xhr.upload.onprogress=function(event){
        if(event.lengthComputable)
        {
            //console.log(event.loaded + " out of "+event.total);
            var time = new Date().getSeconds();
            

        //console.log( ((event.total/Math.pow(2,20)) - event.loaded/Math.pow(2,20)).toFixed(2)) ;// ).toFixed(2))

            var uploaded = (event.loaded/event.total)*100;
            /*
            var data_rate = event.loaded - previous_loaded_data;

            var t = parseInt((event.total - event.loaded)/Math.pow(2,20)  / (data_rate/Math.pow(2,20)));

            document.getElementById('rem_time').innerHTML =parseInt(t)+" sec";
            previous_loaded_data = event.loaded;    
            */
            //console.log(Math.round(uploaded,1) +" %");

            document.getElementById('progressbar').value=uploaded.toFixed(2);
            document.getElementById('loaded-data').innerHTML=uploaded.toFixed(2);
            document.getElementById('status').innerHTML="uploading..";

            

            document.getElementById('size').innerHTML="<b>Uploaded </b>"+(( event.loaded/(Math.pow(2,20))).toFixed(2))+" MB out of "+ (total_size/Math.pow(2,20)).toFixed(2)+" MB";

        }

        /*
        _("status").innerHTML="Uploaded "+ event.loaded + " bytes of "+event.total;

        
        let percent=(event.loaded/event.total) * 100;
        _("progressbar").value=Math.round(percent);
        _("status").innerHTML=Math.round(percent) + "%uploaded.. please wait";
        */
    }

    xhr.send(formdata);
    
    xhr.upload.onload=function(event){
        document.getElementById('status').innerHTML="uploaded";
        console.log("uploaded");
    }
    /*
    xhr.onerror=function(event){
        _("status").innerHTML="upload failed";
    }
*/
    //xhr.abort();
}