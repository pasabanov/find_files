# Find Files

## Description

The "find_files" scripts are small utilities designed to list files that match a given list of wildcards.

- **find_files_canonical.sh** (66 bytes):
    - Finds files matching the specified patterns and prints the **CANONICAL** paths.

- **find_files_relative.sh** (62 bytes):
    - Finds files matching the specified patterns and prints the **RELATIVE** paths.

- The scripts with suffix `_x` after name are executable.

The scripts are useful for finding files with specific extensions or patterns in directories and their subdirectories.

## Authors

- Petr Alexandrovich Sabanov <pasabanov@murena.io> (2024-07-07)

## License

The "find_files" scripts are distributed under the GNU General Public License v3.0. Additional information about the license can be found on the [official website](https://www.gnu.org/licenses/gpl-3.0.html).

## Usage

Usage: `bash find_files_*.sh [PATTERN]...`  
Outputs the list of files matching the provided patterns.

## Examples

Using any `find_files_*.sh` file as `find_files.sh`, you can run:

```
bash find_files.sh "dir/**/*.cpp" "resources/images/*.png"
```
will find all `.cpp`-files in `dir` and all subdirectories of `dir` recursively and also all `.png`-files in directory `resources/images`.