When you are installing *face_recognition* library it will throw error-

    Failed building wheel for dlib
     Running setup.py clean for dlib
     Failed to build dlib
     Installing collected packages: dlib, face-recognition
     Running setup.py install for dlib ... error
     Complete output from command /Users/muralidharan/anaconda/bin/python -u -c "import setuptools, tokenize;__file__='/private/var/folders/xz/rcv9f_6x41gcvhrqzsd6mrxw0000gn/T/pip-build-5zqyoigf/dlib/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /var/folders/xz/rcv9f_6x41gcvhrqzsd6mrxw0000gn/T/pip-qhc3clwr-record/install-record.tx
    
    
    ----------
    
    
    t --single-version-externally-managed --compile:
        running install
        running build
        running build_py
        package init file 'dlib/__init__.py' not found (or not a regular file)
        running build_ext
        Invoking CMake setup: 'cmake /private/var/folders/xz/rcv9f_6x41gcvhrqzsd6mrxw0000gn/T/pip-build-5zqyoigf/dlib/tools/python -DCMAKE_LIBRARY_OUTPUT_DIRECTORY=/private/var/folders/xz/rcv9f_6x41gcvhrqzsd6mrxw0000gn/T/pip-build-5zqyoigf/dlib/build/lib.macosx-10.7-x86_64-3.6 -DPYTHON_EXECUTABLE=/Users/muralidharan/anaconda/bin/python -DCMAKE_BUILD_TYPE=Release'
        error: [Errno 2] No such file or directory: 'cmake'

Now if you go for dlib intead, it will show the same error that 'cmake module not found.....failed to build wheels for dlib'

Now having installed *cmake* library wont do any good either 

Successfully tried and tested approach-
1. For safe side go to [Visual Studio][1] and download the community version
   Initiate the installation process; and when you are at developer tools selection step.....make sure to select ***Desktop Development with C++***
[Visual Studio Configure][2]
After this configuration, Select *Install while downloading*


*Again the above process is just for safe side, since dlib and such libraries require C++ development tools*

2.The current version of python are not compatible with dlib and face_recognition libraries. So we are to downgrade our python version to be able to proceed further.
Go to [Python official website][3] and download python version 3.8.10 dated 3rd may 2021
In installation procedure of python 3.8.10 make sure to select ***add python.exe to path*** 

*Now you have one more python version on your desktop *
To check how many are available to you currently.....run this command on cmd:

    py -0

to select any particular version use: `py -*version?*`
this will bring you the interpreter of the requested python version but you wont be able to install any package here though !

In terminal when you run ***python --version***
it returns the current version of python and its that version which your system came across first

However, we are to use the python version 3.8.10 
so you don't have to uninstall your current version giving possibility to future issues; Instead go to ***Edit the system Environment Variables*** 
Go to PATH of either User or System > search for your required python version ,i.e, 3.8.10 PATH and move it to the top thus ensuring that system can get hold of this version first

Note: If any issue arises later regarding version then to avoid any confusions, you should remove PATHs to unwanted python version and later when you are done with the installation of dlib and face_recognition you can basically add those PATHs back in System Environment Variables, I assure it wont cause any other errors given that you followed every step as told.

Now coming back; just to ensure close the terminal, reopen it and run
`python --version`: it should return the required version ,i.e, 3.8.10

now in the terminal itself change the directory to where you want;
in this directory you have two options either to work in virtual environment 
or same environment 

With virtual environment you just have to first install the virtualenv package 

    pip install virtualenv

create your own virtual environment

    python -m venv myenv

to get inside that virtual environment by changing directory and once your in you have to run 

    ./Scripts/activate 


to activate your created virtual environment.

now simply install the libraries:

    pip install face_recognition

It will take some time, but it will install it
And now its recommended to add those PATHs to your then python version back in the ***System Environment Variables*** or if you havent removed it you should move it to the top. Deleting the 3.8.10 version shouldn't be a problem now either.

If there are any confusions regarding this solution, mention it in the comment
section I will be glad to help further! 

  [1]: https://visualstudio.microsoft.com/downloads/
  [2]: https://i.stack.imgur.com/exV7s.png
  [3]: https://www.python.org/downloads/
