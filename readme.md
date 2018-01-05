## Usage

```Python

from isupdated import is_updated

is_updated('https://github.com/chroming/pdfdir', 'v0.2.1')

# If you want return download link when has update

is_updated('https://github.com/chroming/pdfdir', 'v0.2.1', with_dl=True)

# If the version string is split with character "|"

is_updated('https://github.com/chroming/pdfdir', 'v0|2|1', split='|')

```