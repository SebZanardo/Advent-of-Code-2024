RED='\033[0;31m'
GREEN='\033[0;32m'
MAGENTA='\033[0;35m'
OFF='\033[0m'

echo "\n${MAGENTA}Configuring Advent of Code files${OFF}"

for i in {1..25}; do
	# Name directory
	directory_name="$i"
	if [[ $i -lt 10 ]]; then
		directory_name="0$i"
	fi

	echo ""

	# Check if directory already exists
	if ! [[ -d "$directory_name" ]]; then
		# Create directory
		mkdir "$directory_name"
		echo "${GREEN}Created $directory_name directory!${OFF}"

		# Copy template.py to new part1.py file in directory
		cat template.py >> "$directory_name/part1.py"
		echo "${GREEN}---->\tCreated $directory_name/part1.py${OFF}"

		# Create empty input.in in directory
		touch "$directory_name/input.in"
		echo "${GREEN}---->\tCreated $directory_name/input.in${OFF}"
	else
		echo "${RED}$directory_name directory already exists...${OFF}"
	fi
done

echo "\n${MAGENTA}Goodluck with this year's Advent of Code!${OFF}\n"
