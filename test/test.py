#!/usr/bin/env python3

import subprocess

def run_script(name, *args, interpreter=None):
	result = subprocess.run(
		([interpreter] if interpreter else []) + [name] + list(args),
		capture_output=True,
		text=True
	)
	return result.stdout

def print_script_output(script_path, *args):
	print(f"Running '{script_path}' with args: {args}")
	output = run_script(script_path, *args)
	print(f"Output:\n{output}")
	print()
	return output

def main():

	scripts = ['../python/find_files_canonical_x.py',
			   '../python/find_files_relative_x.py',
			   '../bash/find_files_canonical_x.sh',
			   '../bash/find_files_relative_x.sh']

	args_list = [
		['test_data/**/*.cpp', 'test_data/**/*.h'],
		['test_data/**/*.txt'],
		['test_data/**/*'],
		['test_date/non_existing_dir/**/*'],
	]

	for script in scripts:
		for args in args_list:
			print_script_output(script, *args)

if __name__ == "__main__":
	main()