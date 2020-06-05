if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/service-worker.js').
    then(function(reg)
    {
      console.log('service worker registered');
    }).catch(function(err){
      console.log("Service worker not registered. This happened:", err);
    });
  }

else
{
    console.log('no service worker is here');
}

window.addEventListener('beforeinstallprompt',(e)=>
    {   
        e.prompt();
        console.log('prompt worked');
        
    }
    );

window.addEventListener('appinstalled',(evt) =>
{
        console.log('a2hs installed');
});