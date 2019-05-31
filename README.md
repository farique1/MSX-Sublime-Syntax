# MSX Basic Tools for Sublime Text 3

A syntax highlight compatible with MSX Basic made originally to help improve the experience of [MSX Basic Dignified](https://github.com/farique1/msx-basic-dignified).  
Also a [build system](https://github.com/farique1/MSX-Sublime-Syntax/blob/master/MSX%20Badig%20Build.md) using openMSX.

>MSX Basic Dignified is yet another tool that allows to code MSX Basic with modern standards and convert it back to the classic format.  
 

There are four components:  
- A `tmPreferences` to add `'` (REM) to the comment shortcut key.  
- A `tmTheme` based on Monkai with special scopes for **MBD**.  
- A pretty complete MSX Basic `sublime-syntax` with special highlights for **MBD**.  
- A [build system](https://github.com/farique1/MSX-Sublime-Syntax/blob/master/MSX%20Badig%20Build.md) to run [MSX Basic Dignified](https://github.com/farique1/msx-basic-dignified) source or tradicional MSX Basic code on **openMSX** straight from Sublime Text 3.  

### *Overview:*  
![# Syntax-Overview](https://github.com/farique1/MSX-Sublime-Syntax/blob/master/Images/Syntax-Overview.jpg)  

### *Some Features*  
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
