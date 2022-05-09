# Subtitle Matcher

Most of players will only load the subtitle file automatically when it has exactly the same file name as the video.

But that's just not the case, as the video and subtitle may be downloaded from different sites, with different file names.

And renaming subtitle files can be tough when there's too many files, such as a TV show, so I wrote this script to ease my life.

## Usage

```bash
./sub-match [path]
```

And it will rename subtitle file automatically based on some schemas:

1. only 1 video and 1 subtitle
   
   Just match them!

2. multiple videos and subtitles
   
   We guess this is a TV show suite, then videos and subtitles should follow episode naming like S01E01.
   
   The program will search for the matching subtitles and renames it.
