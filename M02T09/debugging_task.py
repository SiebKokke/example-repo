# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) #k is not defined, switch to key 

# Print dictionary values from simpson_catch_phrases
#switch the d'oh! to double quotes ""
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!",                      
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer']) #need to put [] around the keys 

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

