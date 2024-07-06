# Find Files

## Description

The "find_files" scripts are small utilities (67 to 68 bytes) designed to list files that match a given list of wildcards.

- **find_files_v1.py** (68 bytes):
    - Finds files matching the specified patterns and does not print anything if no files are found.

- **find_files_v2.py** (67 bytes):
    - Finds files matching the specified patterns and prints a blank line if no files are found.

- **find_files_v3.py** (68 bytes):
    - Similar to **find_files_v2.py**, this script finds files matching the specified patterns and prints a blank line if no files are found.

The scripts are useful for finding files with specific extensions or patterns in directories and their subdirectories.

## Authors

- Petr Alexandrovich Sabanov <pasabanov@murena.io> (2024-07-07)

## License

The "find_files" scripts are distributed under the GNU General Public License v3.0. Additional information about the license can be found on the [official website](https://www.gnu.org/licenses/gpl-3.0.html).

## Usage

Usage: `python find_files_v*.py [PATTERN]...`  
Outputs the list of files matching the provided patterns.

## Examples

Using any `find_files_v*.py` file as `find_files.py`, you can run:

```
python find_files.py "dir/**/*.cpp" "resources/images/*.png"
```
will find all `.cpp`-files in directory `dir` and all subdirectories of `dir` recursively and also all `.png`-files in directory `resources/images`.