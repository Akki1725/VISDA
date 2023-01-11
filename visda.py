# VISDA
# Importing Modules
from Body.listen import recognize
from Body.listen import refine
from Features.tasks import execute

# Main loop
if __name__ == "__main__":
    while True:
        # Taking query
        query = recognize()
        queryText = refine(query)
        task = execute(query)