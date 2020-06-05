
self.addEventListener('install', function(event) {
    // Perform install steps
    console.log('installing');
  });

self.addEventListener('fetch', function(event) {
      console.log(event);
  });
