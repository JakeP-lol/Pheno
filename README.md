# Pheno
Pheno test
Step 1. Ensure you are creating the enviroment in python 3

Step 2. Run the "Run on startup" file by copy and pasting the contents             into a terminal

Step 3. Run the "CV2fix" file by copy and pasting the contents into a               terminal

Step 4. Go into "arabidopsis_multiplant_tutorial (1).ipynb" and insert a           image path into the class options self image section for use in             testing thresholds and rotation, the image may need to be inserted         into the enviroment

Step 5. Check the image in cell 6 and change the rotation value so that the         plants are in a straight line horizontally and vertically

Step 6. In cell 10 adjust the threshold value so that the plants are               highlighted in white and the background is highlighted in black,           the value should be near 120

Step 7. In cell 11 adjust the fill size so that the noise gets filled in           but the plants remain intact

Step 8. In cell 13 adjust the ROI values so that each plant has one circle,         do not overlap circles

Step 9. Create a file named "imgs" and put the pictures to be scanned               into the program

Step 10. (optional) Go into the multi-plant-analysis.config and change the           memory usage depending on the enviroment constrictions, for                 mybinder use 900MB, can also change output from json to other               text formats or change the output location and name

Step 11. Run the "Command for parallel" file by copy and pasting the                 contents into a terminal, wait for the command to fully finish             before continuing

Step 12. Examine or export "multi-plant-results.json" as these are the raw           results

Extra notes. 

            Use "arabidopsis_multiplant_tutorial (1).ipynb" for getting images and learning the code step by step, it is well documented

            Ignore both "output_images" and "completed_multi_plant_notebook (1) (2)" as they do not work
            
            The "Hello.py" can be used to test if you are running python
            
            Parallel_config can be used to get a raw config sheet
            
            Other versions of the program can be found on PlantCV's website, the code was taken from the multi plant analysis arabadopsis tutorial and from the danforthcenter "NAPPN 2021 Conference PlantCV virtual workshop materials", Code was compiled by Jacob Petronack
