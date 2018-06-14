To initiate a build from browsers without the [URL API](https://caniuse.com/#feat=url)

```
var script = document.createElement('script');
var scriptUrl = 'https://cdn.jsdelivr.net/npm/url-polyfill@1.0.13/url-polyfill.min.js';
var spec = window.location.pathname.replace('/v2/', '') + window.location.search;

document.body.append(script);

loadingMain(spec);
```