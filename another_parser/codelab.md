<toc-element></toc-element>

This codelab features a simple app
that produces a name badge,
suitable for wear at a pirate convention.
The point is not to dazzle you with the app's appearance or features,
but to teach you about the Dart language, core libraries, and tools.

<figure>
  <img src="img/final-app.png">
  <figcaption>The final app</figcaption>
</figure>

Now that you know what you'll be building,
it's time to get the code
and take a look at it.


### Start the editor

Throughout this codelab,
you use Dart Editor to edit and run your web app.

<div class="extended">
  <p>
    &rarr; If you don't already have Dart Editor, download it by
    clicking the <b>Download Dart + Editor</b> button
    on the following page:
  </p>

  <blockquote>
    <a href="https://www.dartlang.org/tools/download.html"
    target="_blank"><b>Dart download page</b></a>
  </blockquote>

  &rarr; Start Dart Editor.
  If you have problems, see
  <a href="https://www.dartlang.org/tools/editor/troubleshoot.html"
  target="_blank">Troubleshooting Dart Editor</a>.
</div>

<div class="kiosk">
  <p>&rarr; Start Dart Editor by clicking the Dart logo
  at the bottom of your computer screen:</p>

  <p><img src ="/static/img/app-icons/dart_screenshot.png"></p>
</div>


### Open the sample app

&rarr; In Dart Editor,
use **File > Open Existing Folder...**
to open the <b><io-location-string noclone="true"></io-location-string></b> directory.

<div class="row"> <div class="col-md-7" markdown="1">

<figure>
  <img src="img/filesanddirs.png">
  <figcaption><io-location-string noclone="true"></io-location-string> contains the files and directories for your app.</figcaption>
</figure>

<aside class="callout">
<b>Note:</b>
If you see <span style="color:red">red Xs</span> at the left of the
filenames or if the <code>packages</code> directory is missing,
the packages are not properly installed.
Right-click <code>pubspec.yaml</code> and select <b>Pub Get</b>.
</aside>

Key information:

* The `packages` directory, `pubspec.yaml`, and `pubspec.lock` are
  related to package dependencies.
  This project has all the dependencies set up for you.
  Dart Editor automatically installs the necessary packages.

* **Dart SDK** contains the source code for all of the functions,
  variables, and classes provided by the Dart Software Development Kit.

* **Installed Packages** contains the source code for all of the functions,
  variables, and classes for the additional libraries that this application depends on.
<toc-element></toc-element>


### Look in the web directory

&rarr; In Dart Editor, expand the **`begin`** directory
and then the **`web`** directory
by clicking the little arrows
![wee arrow](img/wee-arrow.png) to the left of their names.

The `web` directory contains `piratebadge.html`, `piratebadge.dart`,
and `piratebadge.css`.


### Open the files

&rarr;  Open `piratebadge.html` and `piratebadge.dart`,
by double-clicking each filename in Dart Editor.


### Review the code

&rarr; Get familiar with the HTML and the Dart code for the skeleton version of the app.


#### piratebadge.html

IMPORT('src/begin/web/piratebadge.html', 'initial_html')

Key information:

* During this code lab,
  all the changes you make to `piratebadge.html` are within
  the &lt;div&gt; element identified with the class `widgets`.

* In later steps,
  the &lt;span&gt; element with the ID `badgeName`
  is programmatically updated by the Dart code
  based on user input.

* The first &lt;script&gt; tag identifies
  the main file that implements the app.
  Here, it's the `piratebadge.dart` file.

* The Dart Virtual Machine (Dart VM) runs Dart code natively.
  The Dart VM is built into Dartium,
  a special build of the Chromium browser in which you can run Dart apps natively.

* The `packages/browser/dart.js` script checks for native Dart support
  and either bootstraps the Dart VM or loads compiled JavaScript instead.


#### piratebadge.dart

IMPORT('https://raw.githubusercontent.com/thagikura/dart-start-codelab/master/src/begin/web/piratebadge.dart', 'initial_dart')

Key information:

* This file contains the single entry point for the app&mdash;the `main()` function.
  The &lt;script&gt; tags in the `piratebadge.html` file start the application
  by running this function.

* The `main()` function is a top-level function.

* A top-level variable or function is one that is declared outside
  a class definition.

