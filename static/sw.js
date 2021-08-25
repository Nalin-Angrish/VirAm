const cacheName = 'mcs-vf-app';
const staticAssets = [
  '/chat'
];

self.addEventListener('install', async event => {
	console.log('install event')
	const cache = await caches.open(cacheName); 
  	await cache.addAll(staticAssets); 
});
  
self.addEventListener('fetch', async event => {
	console.log('fetch event')
});