To initiate a build from browsers without the [URL API](https://caniuse.com/#feat=url) or [EventSource](https://caniuse.com/#feat=eventsource)

```
var polyfills = [];

if (!(URL && URL.constructor)) {
  polyfills.push('https://cdn.jsdelivr.net/npm/url-polyfill@1.0.13/url-polyfill.min.js');
}

if (!(EventSource && EventSource.constructor)) {
  polyfills.push('https://cdnjs.cloudflare.com/ajax/libs/event-source-polyfill/0.0.9/eventsource.min.js');
}

for (var index = 0; index < polyfills.length; index ++) {
  var script = document.createElement('script');
  script.src = polyfills[index];

  document.body.append(script);
}

var spec = window.location.pathname.replace('/v2/', '') + window.location.search;

loadingMain(spec);
```