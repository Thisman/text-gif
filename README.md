## Dependencies### Dependencies
- Python 3.7.3
- Pillow https://pillow.readthedocs.io/en/stable/
- argparse https://docs.python.org/3/library/argparse.html#module-argparse

### Usage
```bash
usage: main.py [-h] -t TEXT -s SOURCE [-f FONT] [-r RESULT]

Create gif with text mask

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Text for mask
  -s SOURCE, --source SOURCE
                        Path to source gif
  -f FONT, --font FONT  Path to font using for mask
  -r RESULT, --result RESULT
                        Path for result gif
```

##### For quick result you cun run

```bash
python3 main.py -t "HELLO" -s ./example.gif
```

### TODO
- Better position for text
- Crop whitespace around text mask
- Get gif duration from oiriginal source