# MSX Basic Sublime Text 3 highlight  

A set of configurations made to help improve the experience of [MSX Basic Dignified](https://github.com/farique1/msx-basic-dignified); yet another tool that allows to code MSX Basic with modern standards and convert it back to the classic format.  
An effort, however, has made to make its compatible with the classic MSX Basic syntax.  

There are three components:  
- A `tmPreferences` to add `'` (REM) to the comment shortcut key.  
- A `tmTheme` a theme based on Monkai with special scopes for **MBD**.  
- A pretty complete MSX Basic `sublime-syntax` with special highlights for **MBD**.  

*Overview:*  
![# Syntax-Overview](https://github.com/farique1/MSX-Sublime-Syntax/blob/master/Images/Syntax-Overview.jpg)  

### *Features*  
- General:  
  - All the basic stuff: functions, instructions, variables, quotes, numbers, operators, etc.  
  - Hexadecimal and Binary notation.  
![# Hex-notation-example](https://github.com/farique1/MSX-Sublime-Syntax/blob/master/Images/Hex-notation-example.png)  
  - `Data` line uniform color.  
![# Data-classic-example](https://github.com/farique1/MSX-Sublime-Syntax/blob/master/Images/Data-classic-example.png)  

- MSX Basic Dignified specific:  
  - `Rem` highlight warps line if ending with `:`  
![# Rem-wrap-example](https://github.com/farique1/MSX-Sublime-Syntax/blob/master/Images/Rem-wrap-example.png)  
  - `Data` wraps line if ending with `_`  
![# Data-example](https://github.com/farique1/MSX-Sublime-Syntax/blob/master/Images/Data-example.png)  
  - Defines:  
![# Define-example](https://github.com/farique1/MSX-Sublime-Syntax/blob/master/Images/Define-example.png)  
  - Labels:  
![# Label-example](https://github.com/farique1/MSX-Sublime-Syntax/blob/master/Images/Label-example.png)  
  - Missing or illegal labels:  
![# Missing-label-example](https://github.com/farique1/MSX-Sublime-Syntax/blob/master/Images/Missing-label-example.png)  
![# Non-standard-label-example](https://github.com/farique1/MSX-Sublime-Syntax/blob/master/Images/Non-standard-label-example.png)  
