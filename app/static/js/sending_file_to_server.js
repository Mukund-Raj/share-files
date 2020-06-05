
    var all_files = null;
    var total_size = 0;
    let count = 0;
    var total_data_loaded = 0;
    var duplicates_files = [];
    function send_file() {
        var file1 = document.getElementById('file1');

        if(document.getElementById('file1').files.length == 0)
        {
            alert('Please Select atleast one file')
            return;
        }

        var formdata = new FormData();
        /*
        for (var i = 0; i < document.getElementById('file1').files.length; i++) {
            formdata.append("file1", file1.files[i]);
            total_size += file1.files[i].size;
        }
        */
        all_files = file1.files;
        
        for(let i=0;i<all_files.length;++i)
        {
            total_size+=all_files[i].size;
        }
        
        formdata.set("file1",all_files[count]);

        /**
         * xhr start here 
         * we first send first file then onloadend we will send second file until then we 
         * just wait  for the server to save the file
         */
        let xhr = new XMLHttpRequest();

        xhr.open('POST', '/receivedata', true);
        xhr.responseType = 'json';

        xhr.upload.onprogress = function(event) {
            if (event.lengthComputable) {
                /*
                var uploaded = (event.loaded / event.total) * 100;

                document.getElementById('progressbar').value = uploaded.toFixed(2);
                document.getElementById('loaded-data').innerHTML = uploaded.toFixed(2);
                document.getElementById('status').innerHTML = "uploading..";
                document.getElementById('size').innerHTML = "<b>Uploaded </b>" + ((event.loaded / (Math.pow(2, 20))).toFixed(2)) + " MB out of " + (total_size / Math.pow(2, 20)).toFixed(2) + " MB";
                */
               total_data_loaded =event.loaded;
               console.log(total_data_loaded);
               var uploaded = (event.loaded / event.total) * 100;
               document.getElementById('progressbar').value = uploaded.toFixed(2);
               document.getElementById('loaded-data').innerHTML = uploaded.toFixed(2);

               //document.getElementById('status').innerHTML = "uploading..";
//document.getElementById('size').innerHTML = "<b>Uploaded </b>" + (total_data_loaded / (Math.pow(2, 20)).toFixed(2)) + " MB out of " + (total_size / Math.pow(2, 20)).toFixed(2) + " MB";
            }
        }

        xhr.send(formdata);

        xhr.upload.onload = function() {
            document.getElementById('status').innerHTML = "uploaded";
            console.log("uploaded");
        }

        xhr.onload = function() {
            if (xhr.status == 200) {
                console.log('sucesss');
                if(xhr.response!=null)
                {
                    const duplicate_response = xhr.response;
                    duplicates_files.push(duplicate_response["files"][0]);
                    console.log(duplicates_files);
                }
                //increment the count of file
                ++count;
                document.getElementById('status').innerHTML = count + ' files uploaded';
                if(count<all_files.length)
                {
                    formdata.set("file1",all_files[count]);
                    xhr.open('POST', '/receivedata', true);
                    xhr.send(formdata);
                }
                else{
                    reset();
                    const dFiles = document.getElementById('infod');
                    dFiles.innerHTML = "Duplicates files were" + '<br>';
                    for (let i = 0; i < duplicates_files.length; ++i) {
                        console.log(duplicates_files);
                        dFiles.innerHTML += duplicates_files[i] + '<br>';
                    }
                }
            }
        }
    }

function reset()
{
    total_size = total_data_loaded =  count = 0;
    all_files = null;
    duplicates_files = [];
    document.getElementById('progressbar').value = 0;
    document.getElementById('loaded-data').innerHTML = 0;
}