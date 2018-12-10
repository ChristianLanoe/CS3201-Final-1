# CS3201-Final

1) Accessing the code <br>
1.1) Navigate to https://github.com/ERElli/CS3201-Final <br>
1.2) Click on “# branches” <br>
1.3) Click on “locations”<br>
1.4) Click on “Clone or Download” <br>
1.5) Download as a zip file of clone the repository<br>

2) Running the Code
2.1) Dependencies<br>
2.1.1) Navigate to https://matplotlib.org/users/installing.html and follow the build instructions that apply to your system<br>
2.2) In your terminal, navigate to the code directory in the project<br>
2.3) Type the following command:
		python3 main.py CountryName
Where CountryName is WesternSahara, Uruguay or Canada (please see section 3 if you wish to run using Canada)<br>
2.4) Both the minimum path length and average path length for each generation is printed to the terminal<br>
2.5) Once the code has finished executing, all the individuals who have the best fitness are displayed and one of these paths are plotted<br>

3) Generating Distance Files<br>
	Because the Canada.pickle file was so large, we were not able to upload it to github.
	Please follow instruction 3.3 below to generate the Canada.pickle file.

	The main code requires a serialized array of the distances of each city to all other cities
	If you wish to incorporate more countries you can follow the following instructions<br>
3.1) Given a text file with lines of the form:<br>
	CityNumber X-Coordinate Y-Coordinate<br>
3.2) Make sure the text file is in the same directory as the code<br>
3.3) In the terminal, navigate to the directory containing the code<br>
3.3) Type the following command:<br>
	   	python3 TSPTextFilename CountryName.pickle<br>
3.4) In main.py, in the getTSPfilename function you will have to add the following lines:<br>
			elif countryName == "CountryName":<br>
        		filename = "pathToTSPTextfile"<br>
