echo "Configuring Advent of Code files"

RED='\033[0;31m'
GREEN='\033[0;32m'
OFF='\033[0m'

for i in {1..25}; do
	# Name directory
	directory_name="$i"
	if [[ $i -lt 10 ]]; then
		directory_name="0$i"
	fi

	# Check if directory already exists
	if ! [[ -d "$directory_name" ]]; then
		# Create directory
		mkdir "$directory_name"

		# Copy template.py to new main.py file in directory
		cat template.py >> "$directory_name/main.py"

		# Create empty input.in in directory
		touch "$directory_name/input.in"

		echo "${GREEN}Created $directory_name directory!${OFF}"
	else
		echo "${RED}$directory_name directory already exists...${GREEN}"
	fi
done
