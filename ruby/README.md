# Find Files

## Description

The "find_files" scripts are small utilities designed to list files that match a given list of wildcards.

- **find_files_canonical.rb** (49 bytes):
    - Finds files matching the specified patterns and prints the **CANONICAL** paths.

- **find_files_relative.rb** (24 bytes):
    - Finds files matching the specified patterns and prints the **RELATIVE** paths.

- The scripts with suffix `_x` after name are executable.

The scripts are useful for finding files with specific extensions or patterns in directories and their subdirectories.

## Usage

Usage: `bash find_files_*.rb [PATTERN]...`  
Outputs the list of files matching the provided patterns.

## Examples

Using any `find_files_*.rb` file as `find_files.rb`, you can run:

```
ruby find_files.rb "dir/**/*.cpp" "resources/images/*.png"
```
will find all `.cpp`-files in `dir` and all subdirectories of `dir` recursively and also all `.png`-files in directory `resources/images`.

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Copyright

2024 Petr Alexandrovich Sabanov