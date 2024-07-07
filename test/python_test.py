#!/usr/bin/python3


import subprocess


def run_script(script_name, *args):
	"""Function to run a script and get its output."""
	result = subprocess.run(
		['python', script_name] + list(args),
		capture_output=True,
		text=True
	)
	return result.stdout


def print_script_output(script_path, *args):
	"""Function to run a script and print its output."""
	print(f"Running {script_path} with args: {args}")
	output = run_script(script_path, *args)
	print(f"Output: `{output}`")
	print()
	return output


def args_to_string(args):
	"""Function to convert a list of arguments to a string."""
	return ' '.join(args)


def main():

	# Tests show that v2 and v3 print blank line if they do not find any files.
	# v1 does not print anything.
	do_strip_output = True

	scripts = ['../python/find_files_v1.py',
			   '../python/find_files_v2.py',
			   '../python/find_files_v3.py']

	args_list = [
		['test_data/**/*.cpp', 'test_data/**/*.h'],
		['test_data/**/*.txt'],
		['test_data/**/*'],
		['test_date/non_existing_dir/**/*'],
	]

	results = {}

	for script in scripts:
		results[script] = {}
		for args in args_list:
			output = print_script_output(script, *args)
			results[script][args_to_string(args)] = output if not do_strip_output else output.strip()

	for i, s1 in enumerate(scripts):
		for s2 in scripts[i+1:]:
			for args in args_list:
				print(f"Comparing outputs of {s1} and {s2} with args: {args}")
				output1 = results[s1][args_to_string(args)]
				output2 = results[s2][args_to_string(args)]
				assert output1 == output2, "Outputs are not equal."
				if output1 == output2:
					print("Outputs are equal.")


if __name__ == "__main__":
	main()