

def einlesen(file):

    str_vm = open(file, "r+").read()
    return str_vm

#def filename_ohne_endung (file):
    #return file.replace(".hack", "")
           


#def create_document(finished_array, name):
   # finished_string = "\n".join(finished_array)     ## Noch nicht importiert
   # file = open(f"{name}.asm", "w")
   # file.write(finished_string)