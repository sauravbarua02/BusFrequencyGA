<!DOCTYPE HTML>
<html>

<head>
    <meta charset="utf-8">

    <title>Jupyter Notebook</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="/static/base/images/favicon.ico?v=97c6417ed01bdc0ae3ef32ae4894fd03">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="stylesheet" href="/static/components/jquery-ui/themes/smoothness/jquery-ui.min.css?v=3c2a865c832a1322285c55c6ed99abb2" type="text/css" />
    <link rel="stylesheet" href="/static/components/jquery-typeahead/dist/jquery.typeahead.min.css?v=7afb461de36accb1aa133a1710f5bc56" type="text/css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    

    <link rel="stylesheet" href="/static/style/style.min.css?v=e79dbfdd7c8f19c96a1c8d0d7da38bdc" type="text/css"/>
    
<link rel="stylesheet" href="/static/auth/css/override.css?v=19ec59d2c4f1203c49fe47462028cd9a" type="text/css" />

    <link rel="stylesheet" href="/custom/custom.css" type="text/css" />
    <script src="/static/components/es6-promise/promise.min.js?v=f004a16cb856e0ff11781d01ec5ca8fe" type="text/javascript" charset="utf-8"></script>
    <script src="/static/components/preact/index.js?v=00a2fac73c670ce39ac53d26640eb542" type="text/javascript"></script>
    <script src="/static/components/proptypes/index.js?v=c40890eb04df9811fcc4d47e53a29604" type="text/javascript"></script>
    <script src="/static/components/preact-compat/index.js?v=f865e990e65ad27e3a2601d8adb48db1" type="text/javascript"></script>
    <script src="/static/components/requirejs/require.js?v=951f856e81496aaeec2e71a1c2c0d51f" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20200108145342",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

</head>

<body class=""
 
  
 
dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="/tree" title='dashboard'>
      <img src='/static/base/images/logo.png?v=641991992878ee24c6f3826e81054a0f' alt='Jupyter Notebook'/>
  </a></div>

  
  
  
  
  
  


  
  
  </div>
  <div class="header-bar"></div>

  
  
</div>

<div id="site">


<div id="ipython-main-app" class="container">

    
    
    <div class="row">
    <div class="navbar col-sm-8">
      <div class="navbar-inner">
        <div class="container">
          <div class="center-nav">
            <form action="/login?next=%2Fedit%2Fgaequationplot.py" method="post" class="navbar-form pull-left">
              <input type="hidden" name="_xsrf" value="2|008ef725|019942d797dd5928ca9a8d3c5039e52a|1578479332"/>
              
                <label for="password_input"><strong>Password or token:</strong></label>
              
              <input type="password" name="password" id="password_input" class="form-control">
              <button type="submit" class="btn btn-default" id="login_submit">Log in</button>
            </form>
          </div>
        </div>
      </div>
    </div>
    </div>
    
    
    
    
    <div class="col-sm-6 col-sm-offset-3 text-left rendered_html">
      <h3>
        Token authentication is enabled
      </h3>
      <p>
        If no password has been configured, you need to open the notebook
        server with its login token in the URL, or paste it above.
        This requirement will be lifted if you
        <b><a href='https://jupyter-notebook.readthedocs.io/en/stable/public_server.html'>
            enable a password</a></b>.
      </p>
      <p>
        The command:
        <pre>jupyter notebook list</pre>
        will show you the URLs of running servers with their tokens,
        which you can copy and paste into your browser. For example:
      </p>
      <pre>Currently running servers:
http://localhost:8888/?token=c8de56fa... :: /Users/you/notebooks
</pre>
      <p>
        or you can paste just the token value into the password field on this
        page.
      </p>
      <p>
        See
        <b><a
         href='https://jupyter-notebook.readthedocs.io/en/stable/public_server.html'>
                the documentation on how to enable a password</a>
        </b>
        in place of token authentication,
        if you would like to avoid dealing with random tokens.
      </p>
      <p>
        Cookies are required for authenticated access to notebooks.
      </p>
      
        <h3>Setup a Password</h3>
        <p> You can also setup a password by entering your token and a new password
        on the fields below:</p>
        <form action="/login?next=%2Fedit%2Fgaequationplot.py" method="post" class="">
                <input type="hidden" name="_xsrf" value="2|008ef725|019942d797dd5928ca9a8d3c5039e52a|1578479332"/>
          <div class="form-group">
            <label for="token_input"><h4>Token</h4></label>
            <input type="password" name="password" id="token_input" class="form-control">
          </div>
          <div class="form-group">
            <label for="new_password_input"><h4>New Password</h4></label>
            <input type="password" name="new_password" id="new_password_input" class="form-control" required>
          </div>
          <div class="form-group">
            <button type="submit" class="btn btn-default" id="login_new_pass_submit">Log in and set new password</button>
          </div>
        </form>
      

    </div>
    
    
</div>


</div>








<script type="text/javascript">
  require(["auth/js/main"], function (auth) {
    auth.login_main();
  });
</script>



<script type='text/javascript'>
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>
</body>

</html>