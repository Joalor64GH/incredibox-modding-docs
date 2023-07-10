# 5. Creating a mod
> **Warning**
> This is not a 'quick' or 'easy' process. Good mods take work.

## Step 1: A mod skeleton
Starting with a mod skeleton helps with starting, I recommend starting with something like Travis. It contains only one pack and is easily modifyable. The Travis Files are here in the 'ModTemplate' folder.
1. Download it and get familiar with the contents of the folders. You can generally ignore everything outside of the `app` folder.

## Step 2: The structure of an Incredibox Mod
### The contents of the `app` folder
| File/Folder         | Purpose/Contents                               |
|---------------------|------------------------------------------------|
| asset-v1            | Contents of the first pack.                    |
| css                 | Style sheets, generally can be left alone.     |
| font                | Font files, generally can be left alone.       |
| img                 | Menu images and tutorial images.               |
| js                  | Javascript files, generally can be left alone. |
| lang                | Language files and different translations.     |
| snd                 | Sound test file.                               |
| app.html/index.html | Website file to run Incredibox.                |

### The contents of the `asset-v1` folder
| File/Folder | Purpose/Contents                                                                          |
|-------------|-------------------------------------------------------------------------------------------|
| anime       | Animation files and sprite sheets.                                                        |
| img         | Menu items, default polo sheets, backgrounds and other GUI images.                        |
| sound/ogg   | Music files, bonus audio and bonus aspire audios.                                         |
| splash      | Home screen images.                                                                       |
| video       | Bonus videos.                                                                             |
| app.js      | All technical customization of character file names, source folder, colors, bpm and more. |

### `app.js`: broken down
`app.js` is a JavaScript file that controls the settings of the pack, I plan to make a builder for this later. The ExampleMod includes a nicely formatted version of `app.js` for easier understanding.
| Variable           | Purpose                                                                                |
|--------------------|----------------------------------------------------------------------------------------|
| this.name          | The name of the pack, keep inside double quotes.                                       |
| this.version       | Versioning, keep as is generally, change if your updating, v1, v2, etc.                |
| this.date          | The date of release, just the year generally.                                          |
| this.folder        | The folder its stored in, if the pack is in `assets-v2` change this to `"assets-v2/"`. |
| this.looptime      | The time it take to loop.                                                              |
| this.bpm           | The beats per minute.                                                                  |
| this.totalframe    | The amount of frames per character per loop.                                           |
| this.nbpolo        | ?                                                                                      |
| this.nbloopbonus   | ?                                                                                      |
| this.bonusloopA    | ?                                                                                      |
| this.bonusendloopA | ?                                                                                      |
| this.recmaxloop    | The maximum amount of loops for a recording (unsure)                                   |
| this.recminloop    | The minimum amount of loops for a recording (unsure)                                   |
| this.recmintime    | A math function to determine the minimum amount of time for a recording (don't change) |
| this.spritepolo    | The name of the file for the blank polo.                                               |
| this.spritepicto   | The name of the file for the icons in the pack.                                        |
| this.colBck        | The hex color code of the background.                                                  |
| this.col0-4        | Potentially other hex codes used for the background?                                   |
| this.animearray    | Contains the characters, expanded on below.                                            |
| this.bonusarray    | Contains the bonuses, expanded on below.                                               |

#### `animearray`
| Variable | Purpose                                                                                            |
|----------|----------------------------------------------------------------------------------------------------|
| name     | Name of the animation files in the anime folder.                                                   |
| color    | Color that appears on the bonus wheel when the character is placed.                                |
| uniqsnd  | If set to `!1` this character has an 'a' and a 'b' track, if set to `!0` it only has an 'a' track. |

#### `bonusarray`
| Variable | Purpose                                                     |
|----------|-------------------------------------------------------------|
| name     | Name of the bonus.                                          |
| src      | Name of the source video file in the video folder.          |
| code     | Numbers of the polo's to be selected to activate the bonus. |
| sound    | Name of the sound file for the bonus.                       |
| aspire   | Name of the sound file for the aspire.                      |

## Step 3: Building it and utilising previous skills!
Using the guides in steps 2, 3, and 4, you know how to swap out all these files, you can continue to do the same with your mod, take a look around and don't be afraid to experiment and break things. Learnings about mistakes. Good luck!