# MSX Badig Build  

A build system to run [MSX Basic Dignified](https://github.com/farique1/msx-basic-dignified) source or tradicional MSX Basic code on **openMSX** straight from Sublime Text 3.  

>**MBB** requires **openMSX** and, to speed things up, a save state file with disk drive enabled.  
>If you want to build **MSX Basic Dignified** code you must have `msxbadig.py`  

Once installed, just choose *MSX Badig* built system from the *Build* menu on Sublime and Command+B at will.  

>**MBB** only work on Mac OS for now.  

## Setup  

**MBB** is composed of three files:  
- `MSX Badig.sublime-build`  
- `MSX Badig Build.py`  
- `MSX Badig Build.ini`  

`MSX Badig.sublime-build` and `MSX Badig Build.py` must go into an `MSX` subfolder inside the Sublime `packages` folder: *Sublime Text -> Preferences -> Browse Packages...* on a Mac.  
`MSX Badig Build.ini` must be on the same folder as the code being edited.    

## Configuration  

All the configuration is made through `MSX Badig Build.ini`:  

```ini
[DEFAULT]
openmsx_filepath = /Applications/openmsx/openmsx.app
savestate_filepath = /Users/<user>/.openmsx/savestates/state.oms
msxbadig_filepath = /Applications/msx-basic-dignified/msxbadig.py
export_path = /Users/<user>/desktop/projects/msxdsk1/
export_file = build.bas
throttle = True
classic_basic = False
```

The first three lines tell **MBB** where are the installations and executables of **openMSX**, **MSX Basic Dignified** and the required disk drive enabled **save state**.   

`export_path` is the folder where the built file will be placed. This folder will be inserted as a disk on **openMSX**.  
`export_file` is the name of the built file. It will be loaded with `RUN"` on **openMSX** and should have 8 characters.  

By default **MBB** will turn on *throttle* on **openMSX** to speed up the loading. You can disable it with `False` on `throttle`.  

And finally set `classic_basic` to `True` if you want to build a classic, standard, MSX Basic file. **MBB** will ignore the export settings and open the file being worked on **openMSX**. Remember, It will mount its folder as a disk and load its file name from the MSX. Also you need `MSX Badig Build.ini` there.  

## Execution  

Make sure *MSX Badig* is chosen on *Tools -> Build System* and that the `.ini` file is properly setup.  
Then, once you press Command+B, **MBB** will convert the source (with **MSX Basic Dignified**, if it is the case), open **openMSX** with the save state, insert the destination folder as a disk, toggle throttle (if chosen) and `RUN"` the destination file.  
**MSX Basic Dignified** will run with the settings enabled on its own `.ini` file.  
To exit the test session just close **openMSX**.  


## Acknowledgements  

***MBB** Was NOT thoroughly tested and can misbehave on several ways (most of the time I had no ideia what I was doing :P ). It is offered as is, with no guaranties whatsoever. Use at your own discretion.*  

Having said that, enjoy and send feedback.  
Thanks.  
